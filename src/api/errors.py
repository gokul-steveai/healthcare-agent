"""Central exception-to-HTTP mapping."""

from __future__ import annotations

import logging
from typing import Any

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from src.audit_agent import AuditStorageError, AuditValidationError
from src.boundary_agent import BoundaryAgentError, BoundaryInputError, BoundaryQuotaError
from src.clinical_agent import ClinicalAgentError, ClinicalQuotaError
from src.context_builder import PatientNotFoundError
from src.scenario_runner import ScenarioRunnerError, ScenarioValidationError

from .services.platform import PlatformConfigurationError


LOGGER = logging.getLogger(__name__)


def _response(
    request: Request,
    status_code: int,
    code: str,
    message: str,
    details: list[dict[str, Any]] | None = None,
) -> JSONResponse:
    """Build the stable API error envelope."""

    content: dict[str, Any] = {
        "error": {
            "code": code,
            "message": message,
            "request_id": getattr(request.state, "request_id", "unknown"),
        }
    }
    if details is not None:
        content["error"]["details"] = details
    return JSONResponse(status_code=status_code, content=content)


def register_exception_handlers(app: FastAPI) -> None:
    """Register centralized handlers for domain and framework errors."""

    @app.exception_handler(RequestValidationError)
    async def request_validation_handler(
        request: Request, exc: RequestValidationError
    ) -> JSONResponse:
        return _response(
            request,
            422,
            "request_validation_error",
            "Request validation failed",
            details=exc.errors(),
        )

    @app.exception_handler(PatientNotFoundError)
    async def patient_not_found_handler(
        request: Request, exc: PatientNotFoundError
    ) -> JSONResponse:
        return _response(request, 404, "patient_not_found", str(exc))

    @app.exception_handler(FileNotFoundError)
    async def file_not_found_handler(
        request: Request, exc: FileNotFoundError
    ) -> JSONResponse:
        return _response(request, 404, "resource_not_found", str(exc))

    async def domain_validation_handler(
        request: Request, exc: Exception
    ) -> JSONResponse:
        return _response(request, 400, "domain_validation_error", str(exc))

    for exception_type in (
        ScenarioValidationError,
        BoundaryInputError,
        AuditValidationError,
        ValueError,
    ):
        app.add_exception_handler(exception_type, domain_validation_handler)

    async def agent_failure_handler(request: Request, exc: Exception) -> JSONResponse:
        LOGGER.exception("Agent execution failed", exc_info=exc)
        return _response(
            request,
            502,
            "agent_execution_error",
            "An AI agent could not complete the request",
        )

    for exception_type in (ClinicalAgentError, BoundaryAgentError):
        app.add_exception_handler(exception_type, agent_failure_handler)

    async def quota_failure_handler(request: Request, exc: Exception) -> JSONResponse:
        LOGGER.warning("Gemini quota exhausted: %s", exc)
        response = _response(
            request,
            429,
            "gemini_quota_exceeded",
            str(exc),
        )
        response.headers["Retry-After"] = "60"
        return response

    for exception_type in (ClinicalQuotaError, BoundaryQuotaError):
        app.add_exception_handler(exception_type, quota_failure_handler)

    async def storage_failure_handler(
        request: Request, exc: Exception
    ) -> JSONResponse:
        LOGGER.exception("Platform storage failed", exc_info=exc)
        return _response(
            request,
            500,
            "storage_error",
            "The platform could not persist or load the requested resource",
        )

    for exception_type in (AuditStorageError, ScenarioRunnerError):
        app.add_exception_handler(exception_type, storage_failure_handler)

    @app.exception_handler(PlatformConfigurationError)
    async def configuration_handler(
        request: Request, exc: PlatformConfigurationError
    ) -> JSONResponse:
        LOGGER.error("Platform configuration error: %s", exc)
        return _response(request, 503, "configuration_error", str(exc))

    @app.exception_handler(Exception)
    async def unexpected_error_handler(
        request: Request, exc: Exception
    ) -> JSONResponse:
        LOGGER.exception("Unhandled API error", exc_info=exc)
        return _response(
            request,
            500,
            "internal_server_error",
            "An unexpected error occurred",
        )

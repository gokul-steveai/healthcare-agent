"""FastAPI application factory and ASGI entrypoint."""

from __future__ import annotations
from typing import Any

import logging
import time
import uuid

from fastapi import FastAPI, Request, Response

from .errors import register_exception_handlers
from .logging import configure_logging
from .routes import analysis_router, audits_router, health_router, scenarios_router
from .services import PlatformService


LOGGER = logging.getLogger(__name__)


def create_app(service: PlatformService | None = None) -> FastAPI:
    """Create the API application with an injectable service for tests."""

    configure_logging()
    application = FastAPI(
        title="Healthcare AI Boundary Testing Platform",
        description=(
            "Research API for running synthetic healthcare information through "
            "clinical-analysis, boundary-evaluation, and audit agents."
        ),
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
    )
    application.state.platform_service = service or PlatformService.from_environment()

    @application.middleware("http")
    async def request_logging_middleware(
        request: Request, call_next: Any
    ) -> Response:
        request_id = request.headers.get("X-Request-ID") or uuid.uuid4().hex
        request.state.request_id = request_id
        started = time.perf_counter()
        response = await call_next(request)
        duration_ms = round((time.perf_counter() - started) * 1000, 2)
        response.headers["X-Request-ID"] = request_id
        LOGGER.info(
            "HTTP request completed",
            extra={
                "request_id": request_id,
                "method": request.method,
                "path": request.url.path,
                "status_code": response.status_code,
                "duration_ms": duration_ms,
            },
        )
        return response

    application.include_router(health_router)
    application.include_router(scenarios_router)
    application.include_router(analysis_router)
    application.include_router(audits_router)
    register_exception_handlers(application)
    return application


app = create_app()

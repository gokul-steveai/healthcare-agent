"""Typed HTTP client for the FastAPI boundary-testing backend."""

from __future__ import annotations

import os
from collections.abc import Mapping
from pathlib import Path
from typing import Any
from urllib.parse import quote

import httpx
from dotenv import dotenv_values


DEFAULT_API_BASE_URL = "http://localhost:8000"


class APIClientError(RuntimeError):
    """Base class for frontend-safe API failures."""


class APIUnavailableError(APIClientError):
    """The FastAPI backend cannot be reached."""


class APITimeoutError(APIClientError):
    """The backend did not respond within the timeout."""


class ResourceNotFoundError(APIClientError):
    """The requested backend resource does not exist."""


class APIResponseError(APIClientError):
    """The backend returned another unsuccessful response."""

    def __init__(self, message: str, *, status_code: int) -> None:
        super().__init__(message)
        self.status_code = status_code


class APIClient:
    """Synchronous client matching the backend's public API."""

    def __init__(
        self,
        base_url: str | None = None,
        *,
        timeout: float = 60.0,
        client: httpx.Client | None = None,
    ) -> None:
        configured = base_url or _configured_base_url()
        self.base_url = configured.rstrip("/")
        self._owns_client = client is None
        self._client = client or httpx.Client(
            base_url=self.base_url,
            timeout=httpx.Timeout(timeout, connect=min(timeout, 3.0)),
            headers={"Accept": "application/json"},
        )

    def close(self) -> None:
        """Close an internally created HTTP connection pool."""

        if self._owns_client:
            self._client.close()

    def health(self) -> dict[str, Any]:
        return self._request("GET", "/health")

    def scenarios(self) -> list[dict[str, Any]]:
        return _require_list(self._request("GET", "/scenarios"), "scenarios")

    def run_scenario(self, scenario_id: str) -> dict[str, Any]:
        return self._request("POST", "/run-scenario", json={"scenario_id": scenario_id})

    def analyze(self, patient_id: str, user_request: str) -> dict[str, Any]:
        return self._request(
            "POST", "/analyze", json={"patient_id": patient_id, "user_request": user_request}
        )

    def audits(self) -> list[dict[str, Any]]:
        return _require_list(self._request("GET", "/audits"), "audits")

    def audit(self, audit_id: str) -> dict[str, Any]:
        encoded = quote(audit_id, safe="_-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        return self._request("GET", f"/audit/{encoded}")

    def review_audit(
        self,
        audit_id: str,
        reviewer_name: str,
        reviewer_role: str,
        decision: str,
        notes: str = "",
    ) -> dict[str, Any]:
        encoded = quote(audit_id, safe="_-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        return self._request(
            "POST",
            f"/audit/{encoded}/review",
            json={
                "reviewer_name": reviewer_name,
                "reviewer_role": reviewer_role,
                "decision": decision,
                "notes": notes,
            },
        )

    def _request(
        self, method: str, path: str, *, json: Mapping[str, Any] | None = None
    ) -> dict[str, Any]:
        try:
            response = self._client.request(method, path, json=json)
        except httpx.TimeoutException as exc:
            raise APITimeoutError("The backend took too long to respond. Please try again.") from exc
        except httpx.RequestError as exc:
            raise APIUnavailableError(
                "The FastAPI backend is unavailable. Confirm it is running and API_BASE_URL is correct."
            ) from exc
        if response.status_code >= 400:
            message = _extract_error_message(response)
            if response.status_code == 404:
                raise ResourceNotFoundError(message)
            raise APIResponseError(message, status_code=response.status_code)
        try:
            payload = response.json()
        except ValueError as exc:
            raise APIResponseError("The backend returned invalid JSON.", status_code=response.status_code) from exc
        if not isinstance(payload, dict):
            raise APIResponseError("The backend returned an unexpected response shape.", status_code=response.status_code)
        return payload


def _extract_error_message(response: httpx.Response) -> str:
    try:
        payload = response.json()
    except ValueError:
        return f"Backend request failed with status {response.status_code}."
    if isinstance(payload, dict):
        error = payload.get("error")
        if isinstance(error, dict) and isinstance(error.get("message"), str):
            return error["message"]
        if isinstance(payload.get("detail"), str):
            return payload["detail"]
    return f"Backend request failed with status {response.status_code}."


def _configured_base_url() -> str:
    """Read API URL from process environment or the project `.env` only."""

    environment_value = os.getenv("API_BASE_URL")
    if environment_value:
        return environment_value
    env_file = Path(__file__).resolve().parents[2] / ".env"
    file_value = dotenv_values(env_file).get("API_BASE_URL")
    return str(file_value) if file_value else DEFAULT_API_BASE_URL


def _require_list(payload: Mapping[str, Any], field: str) -> list[dict[str, Any]]:
    value = payload.get(field)
    if not isinstance(value, list) or any(not isinstance(item, dict) for item in value):
        raise APIResponseError(f"The backend response did not contain a valid '{field}' list.", status_code=200)
    return value

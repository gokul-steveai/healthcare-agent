"""Pydantic v2 contracts exposed by the HTTP API."""

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


BoundaryDecision = Literal["ALLOW", "HOLD", "ESCALATE", "STOP"]


class StrictModel(BaseModel):
    """Base API model that rejects unknown input fields."""

    model_config = ConfigDict(extra="forbid")


class HealthResponse(StrictModel):
    """Service health response."""

    status: Literal["healthy"]


class ScenarioSummary(StrictModel):
    """Available scenario metadata."""

    scenario_id: str
    patient_id: str
    user_request: str


class ScenariosResponse(StrictModel):
    """Collection of available scenarios."""

    scenarios: list[ScenarioSummary]


class RunScenarioRequest(StrictModel):
    """Request to execute a stored scenario."""

    scenario_id: str = Field(min_length=1, max_length=100)


class RunScenarioResponse(StrictModel):
    """Summary returned after scenario execution."""

    scenario_id: str
    boundary_decision: BoundaryDecision
    audit_id: str
    status: Literal["completed"]


class AnalyzeRequest(StrictModel):
    """Ad hoc patient-context analysis request."""

    patient_id: str = Field(min_length=1, max_length=200)
    user_request: str = Field(min_length=1, max_length=10_000)


class AnalyzeResponse(StrictModel):
    """Complete agent outputs and audit identifier."""

    clinical_output: dict[str, Any]
    boundary_output: dict[str, Any]
    audit_id: str


class AuditSummary(StrictModel):
    """Compact metadata for one audit record."""

    audit_id: str
    timestamp: str
    scenario_id: str
    patient_id: str
    decision: BoundaryDecision
    version: str


class AuditsResponse(StrictModel):
    """Newest-first audit summary collection."""

    audits: list[AuditSummary]


class ErrorDetail(StrictModel):
    """Stable API error payload."""

    code: str
    message: str
    request_id: str
    details: list[dict[str, Any]] | None = None


class ErrorResponse(StrictModel):
    """Top-level error response."""

    error: ErrorDetail

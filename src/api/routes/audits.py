"""Audit retrieval endpoints."""

from typing import Annotated, Any

from fastapi import APIRouter, Depends, Path

from ..schemas import AuditsResponse
from ..services import PlatformService
from .dependencies import get_platform_service


router = APIRouter(tags=["audits"])
Service = Annotated[PlatformService, Depends(get_platform_service)]


@router.get("/audits", response_model=AuditsResponse)
def list_audits(service: Service) -> dict[str, object]:
    """Return audit summaries in reverse chronological order."""

    return {"audits": service.list_audits()}


@router.get("/audit/{audit_id}", response_model=dict[str, Any])
def get_audit(
    service: Service,
    audit_id: Annotated[str, Path(pattern=r"^audit_[A-Za-z0-9_-]+$")],
) -> dict[str, Any]:
    """Return one complete audit record."""

    return service.get_audit(audit_id)

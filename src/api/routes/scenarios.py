"""Scenario discovery and execution endpoints."""

from typing import Annotated

from fastapi import APIRouter, Depends

from ..schemas import RunScenarioRequest, RunScenarioResponse, ScenariosResponse
from ..services import PlatformService
from .dependencies import get_platform_service


router = APIRouter(tags=["scenarios"])
Service = Annotated[PlatformService, Depends(get_platform_service)]


@router.get("/scenarios", response_model=ScenariosResponse)
def list_scenarios(service: Service) -> dict[str, object]:
    """Return scenarios currently present in the configured folder."""

    return {"scenarios": service.list_scenarios()}


@router.post("/run-scenario", response_model=RunScenarioResponse)
def run_scenario(request: RunScenarioRequest, service: Service) -> dict[str, object]:
    """Execute a stored boundary-testing scenario."""

    return service.run_scenario(request.scenario_id)

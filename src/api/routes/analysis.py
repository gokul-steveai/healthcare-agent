"""Ad hoc patient analysis endpoint."""

from typing import Annotated

from fastapi import APIRouter, Depends

from ..schemas import AnalyzeRequest, AnalyzeResponse
from ..services import PlatformService
from .dependencies import get_platform_service


router = APIRouter(tags=["analysis"])
Service = Annotated[PlatformService, Depends(get_platform_service)]


@router.post("/analyze", response_model=AnalyzeResponse)
def analyze(request: AnalyzeRequest, service: Service) -> dict[str, object]:
    """Analyze one patient request and persist its audit record."""

    return service.analyze(request.patient_id, request.user_request)

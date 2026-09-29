"""Health endpoint."""

from fastapi import APIRouter

from ..schemas import HealthResponse


router = APIRouter(tags=["system"])


@router.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    """Report API-process health without invoking Gemini or the dataset."""

    return HealthResponse(status="healthy")

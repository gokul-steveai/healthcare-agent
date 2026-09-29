"""HTTP route modules."""

from .analysis import router as analysis_router
from .audits import router as audits_router
from .health import router as health_router
from .scenarios import router as scenarios_router

__all__ = [
    "analysis_router",
    "audits_router",
    "health_router",
    "scenarios_router",
]

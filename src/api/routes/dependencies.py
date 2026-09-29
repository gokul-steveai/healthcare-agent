"""Shared FastAPI dependencies."""

from fastapi import Request

from ..services import PlatformService


def get_platform_service(request: Request) -> PlatformService:
    """Return the application-scoped platform service."""

    return request.app.state.platform_service

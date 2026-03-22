from app.adapters.meta_adapter import (
    normalize_health_response,
    normalize_root_response,
)
from app.config.settings import get_settings
from app.schemas.meta import HealthResponse, RootResponse


def build_root_response() -> RootResponse:
    settings = get_settings()
    return normalize_root_response(
        name=settings.app_name,
        environment=settings.app_env,
    )


def build_health_response() -> HealthResponse:
    return normalize_health_response()

from fastapi import APIRouter

from app.schemas.meta import HealthResponse, RootResponse
from app.services.meta_service import build_health_response, build_root_response


router = APIRouter(tags=["meta"])


@router.get("/", response_model=RootResponse)
def read_root() -> RootResponse:
    return build_root_response()


@router.get("/health", response_model=HealthResponse)
def read_health() -> HealthResponse:
    return build_health_response()


@router.get("/health/live", response_model=HealthResponse)
def read_liveness() -> HealthResponse:
    return build_health_response()


@router.get("/health/ready", response_model=HealthResponse)
def read_readiness() -> HealthResponse:
    return build_health_response()


from app.schemas.meta import HealthResponse, RootResponse


def normalize_root_response(*, name: str, environment: str) -> RootResponse:
    return RootResponse(
        name=name,
        status="ok",
        environment=environment,
    )


def normalize_health_response() -> HealthResponse:
    return HealthResponse(status="ok")


from fastapi import FastAPI

from app.config.settings import get_settings
from app.routers.meta import router as meta_router
from app.routers.valuation import router as valuation_router


def create_application() -> FastAPI:
    settings = get_settings()

    application = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        docs_url="/docs",
        redoc_url="/redoc",
    )
    application.include_router(meta_router)
    application.include_router(valuation_router)
    return application


app = create_application()


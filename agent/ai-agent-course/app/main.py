from fastapi import FastAPI

from app.api.v1.api import api_router
from app.core.config import settings


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        description="Python + FastAPI + LLM + Agent 开发实战",
        version=settings.app_version,
        debug=settings.debug,
    )

    app.include_router(api_router, prefix=settings.api_v1_prefix)

    @app.get("/")
    async def root():
        return {
            "message": settings.app_name,
            "env": settings.app_env,
            "version": settings.app_version,
        }

    return app


app = create_app()
from fastapi import APIRouter, Depends

from app.core.config import Settings
from app.dependencies.settings import get_app_settings

router = APIRouter()

async def get_request_source() -> str:
    return "fastapi-dependency"


@router.get("/health")
async def health(
    settings: Settings = Depends(get_app_settings)
):
    return {
        "status": "ok",
        "service": settings.app_name,
        "env": settings.app_env,
        "version": settings.app_version,
        "source": "mock",
    }


@router.get("/error-demo")
async def error_demo():
    return {
        "message": "error demo will be implemented in exception chapter"
    }

@router.get("/system-error-demo")
async def system_error_demo():
    result = 1 / 0
    return {
        "result": result
    }
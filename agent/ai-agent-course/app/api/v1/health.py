from fastapi import APIRouter

from app.core.config import settings

router = APIRouter()


@router.get("/health")
async def health():
    return {
        "status": "ok",
        "service": settings.app_name,
        "env": settings.app_env,
        "version": settings.app_version,
    }


@router.get("/error-demo")
async def error_demo():
    return {
        "message": "error demo will be implemented in exception chapter"
    }
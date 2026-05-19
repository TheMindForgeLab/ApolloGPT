from __future__ import annotations

from fastapi import APIRouter

from apollo.models.model_registry import ModelRegistry
from apollo.settings import settings

router = APIRouter(prefix="/api/models", tags=["models"])
registry = ModelRegistry(settings.model_sources_path)


@router.get("")
def list_models(provider: str | None = None, role: str | None = None):
    profiles = registry.profiles()
    if provider:
        profiles = [profile for profile in profiles if profile.provider == provider]
    if role:
        profiles = [profile for profile in profiles if profile.role == role]
    return {"items": [profile.__dict__ for profile in profiles]}


@router.get("/providers")
def list_providers():
    return {
        "providers": registry.providers(),
        "supported": [
            "ollama",
            "lmstudio",
            "vllm",
            "localai",
            "openai_compatible",
            "textgen-webui",
            "koboldcpp",
        ],
    }


@router.get("/active")
def active_model_settings():
    return {
        "provider": settings.model_provider,
        "model_id": settings.model_id,
        "model_sources_path": str(settings.model_sources_path),
        "default_model": settings.default_model,
        "reasoning_model": settings.reasoning_model,
        "coding_model": settings.coding_model,
        "writing_model": settings.writing_model,
    }

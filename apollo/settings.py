from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


def _bool(name: str, default: bool = False) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


@dataclass(frozen=True)
class Settings:
    workspace_id: str = os.getenv("APOLLO_WORKSPACE_ID", "workspace_apollo")
    storage_dir: Path = Path(os.getenv("APOLLO_STORAGE_DIR", "storage"))
    database_path: Path = Path(os.getenv("APOLLO_DATABASE_PATH", "storage/apollo.sqlite3"))
    use_ollama: bool = _bool("APOLLO_USE_OLLAMA", False)
    model_provider: str = os.getenv("APOLLO_MODEL_PROVIDER", "local_echo")
    model_id: str = os.getenv("APOLLO_MODEL_ID", "")
    model_sources_path: Path = Path(os.getenv("APOLLO_MODEL_SOURCES_PATH", "configs/model_sources.json"))
    ollama_host: str = os.getenv("APOLLO_OLLAMA_HOST", "http://localhost:11434")
    lmstudio_base_url: str = os.getenv("APOLLO_LMSTUDIO_BASE_URL", "http://localhost:1234/v1")
    vllm_base_url: str = os.getenv("APOLLO_VLLM_BASE_URL", "http://localhost:8001/v1")
    localai_base_url: str = os.getenv("APOLLO_LOCALAI_BASE_URL", "http://localhost:8080/v1")
    textgen_base_url: str = os.getenv("APOLLO_TEXTGEN_BASE_URL", "http://localhost:5000")
    koboldcpp_base_url: str = os.getenv("APOLLO_KOBOLDCPP_BASE_URL", "http://localhost:5001")
    openai_compatible_api_key: str = os.getenv("APOLLO_OPENAI_COMPATIBLE_API_KEY", "")
    openai_compatible_base_url: str = os.getenv("APOLLO_OPENAI_COMPATIBLE_BASE_URL", "http://localhost:8080/v1")
    default_model: str = os.getenv("APOLLO_DEFAULT_MODEL", "mistral")
    coding_model: str = os.getenv("APOLLO_CODING_MODEL", "deepseek-coder")
    reasoning_model: str = os.getenv("APOLLO_REASONING_MODEL", "llama3")
    writing_model: str = os.getenv("APOLLO_WRITING_MODEL", "mistral")
    use_cloud_fallback: bool = _bool("APOLLO_USE_CLOUD_FALLBACK", False)
    n8n_base_url: str = os.getenv("APOLLO_N8N_BASE_URL", "http://localhost:5678")
    n8n_api_key: str = os.getenv("APOLLO_N8N_API_KEY", "")


settings = Settings()

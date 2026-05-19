from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional


@dataclass
class ModelProfile:
    id: str
    provider: str
    model: str
    role: str
    base_url: str = ""
    api_key_env: str = ""
    capabilities: List[str] | None = None
    size: str = ""
    active_parameters: str = ""
    notes: str = ""


class ModelRegistry:
    def __init__(self, config_path: Path = Path("configs/model_sources.json")):
        self.config_path = config_path

    def profiles(self) -> list[ModelProfile]:
        if not self.config_path.exists():
            return []
        data = json.loads(self.config_path.read_text(encoding="utf-8"))
        return [ModelProfile(**item) for item in data.get("models", [])]

    def find_for_role(self, role: str, provider: str | None = None, model_id: str | None = None) -> Optional[ModelProfile]:
        profiles = self.profiles()
        if model_id:
            for profile in profiles:
                if profile.id == model_id or profile.model == model_id:
                    return profile
            if provider:
                return ModelProfile(id=f"{provider}:{model_id}", provider=provider, model=model_id, role=role)

        for profile in profiles:
            if profile.role == role and (provider in {None, "", "local_echo"} or profile.provider == provider):
                return profile
        for profile in profiles:
            if profile.role == "default" and (provider in {None, "", "local_echo"} or profile.provider == provider):
                return profile
        return None

    def providers(self) -> list[str]:
        return sorted({profile.provider for profile in self.profiles()})

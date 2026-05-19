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

    def find_for_role(self, role: str) -> Optional[ModelProfile]:
        profiles = self.profiles()
        for profile in profiles:
            if profile.role == role:
                return profile
        for profile in profiles:
            if profile.role == "default":
                return profile
        return None


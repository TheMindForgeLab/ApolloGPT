from __future__ import annotations

import json
from pathlib import Path


class PreferenceMemory:
    def __init__(self, storage_dir: Path):
        self.path = storage_dir / "summaries" / "preferences.json"
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def get_active_preferences(self) -> dict:
        if not self.path.exists():
            return {
                "style": "detailed, practical, buildable",
                "architecture": "local-first, memory-centric, multi-agent",
                "continuity": "preserve project decisions and implementation lessons",
            }
        return json.loads(self.path.read_text(encoding="utf-8"))


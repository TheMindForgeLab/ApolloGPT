from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

from apollo.objects.schemas import ApolloObject


class ObjectRegistry:
    def __init__(self, storage_dir: Path):
        self.path = storage_dir / "objects.jsonl"
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def save(self, obj: ApolloObject) -> str:
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(obj.__dict__, ensure_ascii=False) + "\n")
        return obj.id

    def list(self, object_type: Optional[str] = None, project_id: Optional[str] = None) -> list[ApolloObject]:
        if not self.path.exists():
            return []
        objects = []
        for line in self.path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            data = json.loads(line)
            if object_type and data.get("object_type") != object_type:
                continue
            if project_id and data.get("project_id") != project_id:
                continue
            objects.append(ApolloObject(**data))
        return objects


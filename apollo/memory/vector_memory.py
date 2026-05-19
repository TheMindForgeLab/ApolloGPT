from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Iterable, Optional

from apollo.schemas import MemoryItem, new_id, utc_now


def _tokens(text: str) -> set[str]:
    return set(re.findall(r"[a-zA-Z0-9_]+", text.lower()))


class VectorMemory:
    """Lexical fallback now; replace internals with Chroma/Qdrant later."""

    def __init__(self, storage_dir: Path):
        self.path = storage_dir / "vector_db" / "memory_items.jsonl"
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def add_text(self, content: str, project: Optional[str], memory_type: str = "output", metadata: Optional[dict] = None) -> str:
        item = MemoryItem(
            id=new_id("mem"),
            content=content,
            memory_type=memory_type,
            project=project,
            importance=float((metadata or {}).get("importance", 0.5)),
            metadata=metadata or {},
            created_at=utc_now(),
        )
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(item.__dict__, ensure_ascii=False) + "\n")
        return item.id

    def search(self, query: str, project: Optional[str] = None, limit: int = 8) -> list[MemoryItem]:
        if not self.path.exists():
            return []
        q = _tokens(query)
        scored: list[tuple[float, MemoryItem]] = []
        for line in self.path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            data = json.loads(line)
            if project and data.get("project") not in {project, None}:
                continue
            overlap = len(q & _tokens(data.get("content", "")))
            score = overlap + float(data.get("importance", 0.5))
            if score > 0:
                scored.append((score, MemoryItem(**data)))
        scored.sort(key=lambda row: row[0], reverse=True)
        return [item for _, item in scored[:limit]]


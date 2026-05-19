from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Optional

from apollo.schemas import MemoryItem, new_id, utc_now


def _tokens(text: str) -> set[str]:
    return set(re.findall(r"[a-zA-Z0-9_]+", text.lower()))


class VectorMemory:
    """Lexical fallback now; replace internals with Chroma/Qdrant later."""

    def __init__(self, storage_dir: Path):
        self.path = storage_dir / "vector_db" / "memory_items.jsonl"
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def add_text(self, content: str, project: Optional[str], memory_type: str = "output", metadata: Optional[dict] = None) -> str:
        content_hash = hashlib.sha256(content.encode("utf-8")).hexdigest()
        item = MemoryItem(
            id=new_id("mem"),
            content=content,
            memory_type=memory_type,
            project=project,
            importance=float((metadata or {}).get("importance", 0.5)),
            metadata={**(metadata or {}), "content_hash": content_hash},
            created_at=utc_now(),
        )
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(item.__dict__, ensure_ascii=False) + "\n")
        return item.id

    def add_chunks(self, chunks: list[str], project: Optional[str], memory_type: str, metadata: Optional[dict] = None) -> list[str]:
        ids = []
        for index, chunk in enumerate(chunks):
            ids.append(self.add_text(chunk, project=project, memory_type=memory_type, metadata={**(metadata or {}), "chunk_index": index}))
        return ids

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
            content_tokens = _tokens(data.get("content", ""))
            overlap = len(q & content_tokens)
            coverage = overlap / max(len(q), 1)
            density = overlap / max(len(content_tokens), 1)
            scope_boost = 0.25 if project and data.get("project") == project else 0.0
            score = (coverage * 3.0) + (density * 2.0) + scope_boost + float(data.get("importance", 0.5))
            if score > 0:
                data["metadata"] = {**data.get("metadata", {}), "retrieval_score": round(score, 4)}
                scored.append((score, MemoryItem(**data)))
        scored.sort(key=lambda row: row[0], reverse=True)
        return [item for _, item in scored[:limit]]

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List


class GraphMemory:
    def __init__(self, storage_dir: Path):
        self.path = storage_dir / "graph_db" / "relationships.jsonl"
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def add_relationship(self, source: str, relation: str, target: str, metadata: Dict | None = None) -> None:
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps({"source": source, "relation": relation, "target": target, "metadata": metadata or {}}) + "\n")

    def get_related(self, source: str | None = None) -> List[Dict]:
        if not self.path.exists():
            return []
        rows = [json.loads(line) for line in self.path.read_text(encoding="utf-8").splitlines() if line.strip()]
        if source:
            return [row for row in rows if row["source"] == source or row["target"] == source]
        return rows[-20:]


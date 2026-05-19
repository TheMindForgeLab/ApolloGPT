from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict


class RawMemory:
    def __init__(self, storage_dir: Path):
        self.path = storage_dir / "raw_memory" / "interactions.jsonl"
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def append(self, record: Dict[str, Any]) -> None:
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")


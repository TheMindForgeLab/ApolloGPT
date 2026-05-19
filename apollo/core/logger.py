from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

from apollo.schemas import utc_now


class ApolloLogger:
    def __init__(self, storage_dir: Path):
        self.log_dir = storage_dir / "logs"
        self.log_dir.mkdir(parents=True, exist_ok=True)

    def event(self, event_type: str, payload: Dict[str, Any]) -> None:
        path = self.log_dir / "events.jsonl"
        record = {"type": event_type, "timestamp": utc_now(), "payload": payload}
        with path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")


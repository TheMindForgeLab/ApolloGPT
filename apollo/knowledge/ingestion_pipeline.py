from __future__ import annotations

from pathlib import Path

from apollo.memory.memory_manager import MemoryManager
from apollo.settings import settings


class IngestionPipeline:
    def __init__(self, memory_manager: MemoryManager | None = None):
        self.memory_manager = memory_manager or MemoryManager(settings.storage_dir)

    def ingest_file(self, path: str, project: str | None = None, memory_type: str = "document") -> dict:
        file_path = Path(path)
        text = file_path.read_text(encoding="utf-8")
        ids = self.memory_manager.ingest_text(
            text,
            project=project,
            source=str(file_path),
            memory_type=memory_type,
            metadata={"filename": file_path.name, "suffix": file_path.suffix},
        )
        return {"source": str(file_path), "memory_ids": ids, "chunks": len(ids)}

from __future__ import annotations

from apollo.memory.chunker import chunk_text


class MemoryIndexer:
    def __init__(self, vector_memory):
        self.vector_memory = vector_memory

    def index_text(self, text: str, project: str | None, memory_type: str = "document", metadata: dict | None = None) -> list[str]:
        chunks = chunk_text(text)
        return self.vector_memory.add_chunks(chunks, project=project, memory_type=memory_type, metadata=metadata or {})

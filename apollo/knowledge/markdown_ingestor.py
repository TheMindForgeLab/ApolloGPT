from pathlib import Path


class MarkdownIngestor:
    def ingest(self, path: str) -> dict:
        file_path = Path(path)
        return {"text": file_path.read_text(encoding="utf-8"), "source": str(file_path), "kind": "markdown"}

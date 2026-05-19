from pathlib import Path


class DocumentIngestor:
    def ingest_text_file(self, path: str) -> dict:
        file_path = Path(path)
        return {"text": file_path.read_text(encoding="utf-8"), "source": str(file_path), "kind": file_path.suffix.lstrip(".") or "text"}

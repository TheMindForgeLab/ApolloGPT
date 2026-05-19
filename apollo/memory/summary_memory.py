from __future__ import annotations

from pathlib import Path
from typing import Optional


class SummaryMemory:
    def __init__(self, storage_dir: Path):
        self.path = storage_dir / "summaries"
        self.path.mkdir(parents=True, exist_ok=True)

    def get_project_summary(self, project: Optional[str]) -> str:
        if not project:
            return ""
        path = self.path / f"{project.lower().replace(' ', '_')}.md"
        return path.read_text(encoding="utf-8") if path.exists() else ""

    def update_from_result(self, project: Optional[str], text: str) -> None:
        if not project:
            return
        path = self.path / f"{project.lower().replace(' ', '_')}.md"
        with path.open("a", encoding="utf-8") as handle:
            handle.write(f"\n\n## Memory Update\n{text[:2000]}\n")


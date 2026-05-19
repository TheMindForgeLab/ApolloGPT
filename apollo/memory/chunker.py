from __future__ import annotations


def chunk_text(text: str, max_chars: int = 1200, overlap: int = 150) -> list[str]:
    cleaned = text.replace("\r\n", "\n").strip()
    if not cleaned:
        return []
    chunks: list[str] = []
    start = 0
    while start < len(cleaned):
        end = min(start + max_chars, len(cleaned))
        if end < len(cleaned):
            paragraph_break = cleaned.rfind("\n\n", start, end)
            sentence_break = cleaned.rfind(". ", start, end)
            split_at = max(paragraph_break, sentence_break)
            if split_at > start + int(max_chars * 0.5):
                end = split_at + 1
        chunks.append(cleaned[start:end].strip())
        if end >= len(cleaned):
            break
        start = max(0, end - overlap)
    return [chunk for chunk in chunks if chunk]

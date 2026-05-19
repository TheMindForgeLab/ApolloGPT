class MemoryScorer:
    def score(self, memory, query: str) -> float:
        return getattr(memory, "importance", 0.5)


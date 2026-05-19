class MemoryCompactor:
    def compact(self, memories):
        return "\n".join(getattr(item, "content", str(item)) for item in memories)


class MemoryIndexer:
    def index(self, memory_item):
        return getattr(memory_item, "id", None)


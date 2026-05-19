class Linker:
    def link(self, source: str, target: str, relation: str = "related_to") -> dict:
        return {"source": source, "relation": relation, "target": target}


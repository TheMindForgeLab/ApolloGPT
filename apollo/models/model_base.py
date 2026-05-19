from __future__ import annotations


class ModelBase:
    model_id = "base"

    def generate(self, prompt: str) -> str:
        raise NotImplementedError


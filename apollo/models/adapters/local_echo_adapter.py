from __future__ import annotations

from apollo.models.model_base import ModelBase


class LocalEchoAdapter(ModelBase):
    """Offline placeholder so the Apollo loop works before models are connected."""

    def __init__(self, model_id: str = "local:echo"):
        self.model_id = model_id

    def generate(self, prompt: str) -> str:
        return (
            "ApolloGPT local scaffold response.\n\n"
            "A real model is not enabled yet, so this adapter is echoing the structured prompt path. "
            "Set APOLLO_USE_OLLAMA=true and choose an installed Ollama model to enable generation.\n\n"
            f"Prompt preview:\n{prompt[:1200]}"
        )


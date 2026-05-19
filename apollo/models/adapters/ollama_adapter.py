from __future__ import annotations

import json
import urllib.error
import urllib.request

from apollo.models.model_base import ModelBase


class OllamaAdapter(ModelBase):
    def __init__(self, model_name: str, host: str = "http://localhost:11434"):
        self.model_name = model_name
        self.host = host.rstrip("/")
        self.model_id = f"ollama:{model_name}"

    def generate(self, prompt: str) -> str:
        data = json.dumps({"model": self.model_name, "prompt": prompt, "stream": False}).encode("utf-8")
        request = urllib.request.Request(
            f"{self.host}/api/generate",
            data=data,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=120) as response:
                payload = json.loads(response.read().decode("utf-8"))
                return payload.get("response", "")
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            return f"[Ollama unavailable: {exc}]"


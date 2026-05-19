from __future__ import annotations

import json
import urllib.error
import urllib.request

from apollo.models.model_base import ModelBase


class TextGenerationWebUIAdapter(ModelBase):
    """Adapter for oobabooga/text-generation-webui compatible /api/v1/generate servers."""

    def __init__(self, model_name: str, base_url: str = "http://localhost:5000"):
        self.model_name = model_name
        self.base_url = base_url.rstrip("/")
        self.model_id = f"textgen-webui:{model_name}"

    def generate(self, prompt: str) -> str:
        payload = {
            "prompt": prompt,
            "max_new_tokens": 1200,
            "temperature": 0.4,
            "do_sample": True,
        }
        request = urllib.request.Request(
            f"{self.base_url}/api/v1/generate",
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=180) as response:
                data = json.loads(response.read().decode("utf-8"))
                return data.get("results", [{}])[0].get("text", "")
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, KeyError, IndexError) as exc:
            return f"[text-generation-webui unavailable: {exc}]"


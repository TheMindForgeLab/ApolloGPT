from __future__ import annotations

import json
import urllib.error
import urllib.request

from apollo.models.model_base import ModelBase


class KoboldCppAdapter(ModelBase):
    """Adapter for KoboldCPP /api/v1/generate."""

    def __init__(self, model_name: str = "koboldcpp", base_url: str = "http://localhost:5001"):
        self.model_name = model_name
        self.base_url = base_url.rstrip("/")
        self.model_id = f"koboldcpp:{model_name}"

    def generate(self, prompt: str) -> str:
        payload = {"prompt": prompt, "max_context_length": 8192, "max_length": 1200, "temperature": 0.4}
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
            return f"[koboldcpp unavailable: {exc}]"


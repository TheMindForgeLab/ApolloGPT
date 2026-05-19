from __future__ import annotations

import json
import urllib.error
import urllib.request

from apollo.models.model_base import ModelBase


class OpenAICompatibleAdapter(ModelBase):
    """Adapter for LM Studio, vLLM, LocalAI, OpenRouter, and other chat-completions APIs."""

    def __init__(self, model_name: str, base_url: str, api_key: str = "", provider: str = "openai_compatible"):
        self.model_name = model_name
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.provider = provider
        self.model_id = f"{provider}:{model_name}"

    def generate(self, prompt: str) -> str:
        payload = {
            "model": self.model_name,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.4,
            "stream": False,
        }
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"

        request = urllib.request.Request(
            f"{self.base_url}/chat/completions",
            data=json.dumps(payload).encode("utf-8"),
            headers=headers,
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=180) as response:
                data = json.loads(response.read().decode("utf-8"))
                return data.get("choices", [{}])[0].get("message", {}).get("content", "")
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, KeyError, IndexError) as exc:
            return f"[{self.provider} unavailable: {exc}]"


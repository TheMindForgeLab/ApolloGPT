from __future__ import annotations


class N8NClient:
    """Placeholder for local n8n integration. External actions should require explicit approval."""

    def __init__(self, base_url: str, api_key: str = ""):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key

    def describe_webhook_target(self, path: str) -> str:
        return f"{self.base_url}/webhook/{path.lstrip('/')}"


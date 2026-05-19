from __future__ import annotations


class NodeManager:
    def local_status(self) -> dict:
        return {"node_id": "local_node", "status": "online", "capabilities": ["cpu", "local_files", "ollama_optional"]}


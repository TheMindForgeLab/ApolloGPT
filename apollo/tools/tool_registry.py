from __future__ import annotations


class ToolRegistry:
    def __init__(self):
        self.tools = {}

    def register(self, name: str, function):
        self.tools[name] = function

    def run(self, name: str, **kwargs):
        if name not in self.tools:
            raise ValueError(f"Tool not found: {name}")
        return self.tools[name](**kwargs)


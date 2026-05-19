class BaseTool:
    name = "base_tool"

    def run(self, **kwargs):
        raise NotImplementedError


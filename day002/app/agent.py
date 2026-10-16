from app.tools.base import BaseTool


class Agent:
    """管理和调用多个工具。"""

    def __init__(self, tools: list[BaseTool]) -> None:
        self._tools: dict[str, BaseTool] = {}

        for tool in tools:
            if tool.name in self._tools:
                raise ValueError(f"工具名称重复：{tool.name}")

            self._tools[tool.name] = tool

    def list_tools(self) -> list[str]:
        """返回所有工具的名称。"""
        return list(self._tools.keys())

    def run_tool(self, name: str, query: str) -> str:
        """根据工具名称调用对应工具。"""
        try:
            tool = self._tools[name]
        except KeyError as exc:
            raise ValueError(f"未找到工具：{name}") from exc

        return tool.run(query)

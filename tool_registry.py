from typing import Dict, List, Any
from tools.base_tool import BaseTool


class ToolRegistry:
    def __init__(self) -> None:
        self.tools: Dict[str, BaseTool] = {}

    def register_tool(self, tool: BaseTool) -> None:
        self.tools[tool.name] = tool

    def get_tool(self, name: str):
        return self.tools.get(name)

    def get_function_declarations(self) -> List[Dict[str, Any]]:
        return [tool.get_declaration() for tool in self.tools.values()]

    def execute_tool(self, name: str, args: Dict[str, Any]) -> str:
        tool = self.get_tool(name)
        if not tool:
            return f"Error: Unknown tool requested -> {name}"

        try:
            return tool.execute(**args)
        except TypeError as e:
            return f"Error: Invalid arguments for tool '{name}' -> {str(e)}"
        except Exception as e:
            return f"Error while executing tool '{name}' -> {str(e)}"
from datetime import datetime
from typing import Any, Dict
from tools.base_tool import BaseTool


class TimeTool(BaseTool):
    name = "time"
    description = "Get the current local date and time."

    def execute(self) -> str:
        now = datetime.now()
        return now.strftime("Current local date and time: %Y-%m-%d %H:%M:%S")

    def run(self) -> str:
        return self.execute()

    def get_declaration(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "parameters": {
                "type": "OBJECT",
                "properties": {}
            }
        }

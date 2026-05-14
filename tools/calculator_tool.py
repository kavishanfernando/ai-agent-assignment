from typing import Any, Dict
from tools.base_tool import BaseTool


class CalculatorTool(BaseTool):
    name = "calculator"
    description = "Perform basic arithmetic calculations."

    def execute(self, expression: str) -> str:
        try:
            allowed_chars = "0123456789+-*/(). "
            if not all(ch in allowed_chars for ch in expression):
                return "Error: Invalid characters in expression."

            result = eval(expression, {"__builtins__": {}}, {})
            return f"Result: {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."
        except Exception as e:
            return f"Error in calculator tool: {str(e)}"

    def run(self, expression: str) -> str:
        return self.execute(expression)

    def get_declaration(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "parameters": {
                "type": "OBJECT",
                "properties": {
                    "expression": {
                        "type": "STRING",
                        "description": "Arithmetic expression like 25 * 8"
                    }
                },
                "required": ["expression"]
            }
        }
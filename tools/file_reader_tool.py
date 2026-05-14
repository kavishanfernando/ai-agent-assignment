from pathlib import Path
from typing import Any, Dict
from tools.base_tool import BaseTool


class FileReaderTool(BaseTool):
    name = "read_local_file"
    description = "Read the contents of a local text file."

    def execute(self, file_path: str) -> str:
        try:
            path = Path(file_path).expanduser()

            if not path.exists():
                return f"Error: File not found -> {file_path}"

            if not path.is_file():
                return f"Error: Path is not a file -> {file_path}"

            content = path.read_text(encoding="utf-8")
            if len(content) > 4000:
                content = content[:4000] + "\n...[truncated]"

            return f"File content from {file_path}:\n{content}"
        except Exception as e:
            return f"Error in file reader tool: {str(e)}"

    def run(self, file_path: str) -> str:
        return self.execute(file_path)

    def get_declaration(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "parameters": {
                "type": "OBJECT",
                "properties": {
                    "file_path": {
                        "type": "STRING",
                        "description": "Path to a local text file"
                    }
                },
                "required": ["file_path"]
            }
        }
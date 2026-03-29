from typing import Any, Dict
from tools.base_tool import BaseTool


class TranslationTool(BaseTool):
    name = "translate_text"
    description = "Prepare text for translation into a target language."

    def execute(self, text: str, target_language: str) -> str:
        try:
            return (
                f'Translation request noted.\n'
                f'Text: "{text}"\n'
                f'Target language: {target_language}\n'
                f'Please translate this naturally.'
            )
        except Exception as e:
            return f"Error in translation tool: {str(e)}"

    def get_declaration(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "parameters": {
                "type": "OBJECT",
                "properties": {
                    "text": {
                        "type": "STRING",
                        "description": "Text to translate"
                    },
                    "target_language": {
                        "type": "STRING",
                        "description": "Language to translate into"
                    }
                },
                "required": ["text", "target_language"]
            }
        }
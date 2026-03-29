from typing import List, Dict


class MemoryManager:
    def __init__(self) -> None:
        self.history: List[Dict[str, str]] = []

    def add_user_message(self, message: str) -> None:
        self.history.append({"role": "user", "content": message})

    def add_assistant_message(self, message: str) -> None:
        self.history.append({"role": "assistant", "content": message})

    def get_history_as_text(self) -> str:
        if not self.history:
            return "No previous conversation."

        lines = []
        for item in self.history:
            lines.append(f"{item['role'].capitalize()}: {item['content']}")
        return "\n".join(lines)

    def clear(self) -> None:
        self.history.clear()
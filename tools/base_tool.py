from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseTool(ABC):
    name: str
    description: str

    @abstractmethod
    def execute(self, **kwargs) -> str:
        pass

    @abstractmethod
    def get_declaration(self) -> Dict[str, Any]:
        pass
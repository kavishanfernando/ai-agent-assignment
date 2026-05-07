from pydantic import BaseModel
from typing import List, Optional

class UserRequest(BaseModel):
    user_id: str
    query: str
    parameters: Optional[dict] = None

class ToolResponse(BaseModel):
    tool_name: str
    output: str
    success: bool

class AgentResponse(BaseModel):
    agent_id: str
    responses: List[ToolResponse]
    status: str
    error: Optional[str] = None
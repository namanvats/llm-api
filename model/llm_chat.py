from pydantic import BaseModel
from typing import Optional


class LLMChatRequest(BaseModel):
    llm_model: str
    query: str
from datetime import datetime, timezone
from typing import Literal
from pydantic import BaseModel, Field


class Category(BaseModel):
    user_id: int
    name: str
    type: Literal["income", "expense"]
    emoji: str = "📁"
    is_default: bool = False
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
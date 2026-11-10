from datetime import datetime, timezone
from pydantic import BaseModel, Field, ConfigDict


class User(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True
    )

    telegram_id: int
    username: str | None = None
    first_name: str
    language: str = "ru"
    currency: str = "RUB"
    timezone: str = "Europe/Moscow"
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    is_blocked: bool = False
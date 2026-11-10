from datetime import datetime, timezone
from typing import Literal
from pydantic import BaseModel, Field, field_validator


class Transaction(BaseModel):
    user_id: int
    category_id: str
    type: Literal["income", "expense"]
    amount: int = Field(gt=0)
    currency: str = "RUB"
    description: str | None = None
    occurred_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    @field_validator("amount")
    @classmethod
    def validate_amount(cls, value):
        if value <= 0:
            raise ValueError("Сумма должна быть больше нуля")
        return value
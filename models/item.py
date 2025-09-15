from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, Field, PositiveFloat

class Item(BaseModel):
    id: UUID = Field(default_factory=uuid4, description="Unique ID for the item")
    name: str = Field(min_length=1, max_length=100, description="Display name")
    price: PositiveFloat = Field(description="Unit price in USD")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="UTC timestamp")
    description: Optional[str] = Field(default=None, max_length=500, description="Optional details")
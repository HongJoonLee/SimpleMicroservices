from datetime import datetime
from uuid import UUID, uuid4
from pydantic import BaseModel, Field, PositiveInt, conlist
from .item import Item

class OrderLine(BaseModel):
    item_id: UUID = Field(description="FK to Item.id")
    quantity: PositiveInt = Field(description="How many units")

class Order(BaseModel):
    id: UUID = Field(default_factory=uuid4, description="Unique order ID")
    lines: conlist(OrderLine, min_items=1)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    def total(self, catalog: dict[UUID, Item]) -> float:
        return sum(catalog[line.item_id].price * line.quantity for line in self.lines)
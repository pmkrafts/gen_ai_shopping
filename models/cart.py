from pydantic import BaseModel, Field


class CartItem(BaseModel):
    product_id: str
    quantity: int = Field(..., ge=1)
    size: str
    color: str


class Cart(BaseModel):
    items: list[CartItem] = []
    currency: str = "INR"

    def total(self, price_lookup: dict[str, float]) -> float:
        return sum(
            price_lookup.get(item.product_id, 0) * item.quantity for item in self.items
        )

from pydantic import BaseModel
from models.product import Product


class StylingSession(BaseModel):
    goal: str
    budget: float | None = None
    selected_items: list[Product] = []
    feedback: list[str] = []
    turn_count: int = 0

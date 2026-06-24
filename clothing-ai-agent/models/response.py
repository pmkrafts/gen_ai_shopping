from pydantic import BaseModel
from .product import Product
from .cart import Cart


class AgentResponse(BaseModel):
    reply: str
    products: list[Product] = []
    cart: Cart | None = None
    suggested_actions: list[str] = []


from pydantic import BaseModel
from .cart import CartItem


class OrderItem(CartItem):
    pass


class Order(BaseModel):
    order_id: str
    customer_name: str
    items: list[OrderItem]
    total: float
    currency: str = "INR"
    status: str = "confirmed"
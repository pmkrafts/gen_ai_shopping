from langchain.tools import tool
from models.order import Order, OrderItem
from tools.manage_cart import manage_cart_tool
import uuid


@tool
def process_order_tool(customer_name: str, shipping_address: str) -> dict:
    """Process checkout for the current cart."""
    cart_data = manage_cart_tool.invoke({"action": "show"})
    items = [OrderItem(**item) for item in cart_data["items"]]

    if not items:
        return {"error": "Cart is empty."}

    order = Order(
        order_id=str(uuid.uuid4())[:8].upper(),
        customer_name=customer_name,
        items=items,
        total=sum(
            item.quantity * 999 for item in items
        ),  # Replace with real price lookup
    )
    manage_cart_tool.invoke({"action": "clear"})
    return order.model_dump()

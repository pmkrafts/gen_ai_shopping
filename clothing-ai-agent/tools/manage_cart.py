from typing import Literal
from langchain.tools import tool
from models.cart import Cart, CartItem

_cart = Cart()


@tool
def manage_cart_tool(
    action: Literal["add", "remove", "update", "clear", "show"],
    items: list[dict] | None = None,
) -> dict:
    """Manage the shopping cart.

    Args:
        action: One of add, remove, update, clear, show.
        items: List of items. Each item must include product_id, quantity, size, and color.

    Examples:
        Add an item:
            action="add", items=[{"product_id": "PROD001", "quantity": 1, "size": "M", "color": "red"}]

        Update an item (replaces the existing item with the same product_id):
            action="update", items=[{"product_id": "PROD001", "quantity": 1, "size": "L", "color": "red"}]

        Remove an item:
            action="remove", items=[{"product_id": "PROD001"}]

        Show cart:
            action="show"

        Clear cart:
            action="clear"
    """
    global _cart
    items = items or []

    if action == "clear":
        _cart = Cart()
    elif action == "add":
        for item in items:
            _cart.items.append(CartItem(**item))
    elif action == "remove":
        ids = {i["product_id"] for i in items}
        _cart.items = [it for it in _cart.items if it.product_id not in ids]
    elif action == "update":
        for item in items:
            for i, existing in enumerate(_cart.items):
                if existing.product_id == item["product_id"]:
                    _cart.items[i] = CartItem(**item)

    return _cart.model_dump()

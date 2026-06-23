from typing import Literal
from langchain.tools import tool

_wishlist: list[str] = []


@tool
def manage_wishlist_tool(action: Literal["add", "remove", "clear", "list"], product_ids: list[str] | None = None) -> list[str]:
    """Manage the user's wishlist."""
    global _wishlist
    product_ids = product_ids or []

    if action == "add":
        _wishlist.extend([p for p in product_ids if p not in _wishlist])
    elif action == "remove":
        _wishlist = [p for p in _wishlist if p not in product_ids]
    elif action == "clear":
        _wishlist = []

    return _wishlist
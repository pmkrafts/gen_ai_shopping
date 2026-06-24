from langchain.tools import tool
from tools.manage_cart import manage_cart_tool


@tool
def update_cart_item_tool(
    product_id: str,
    size: str | None = None,
    color: str | None = None,
    quantity: int | None = None,
) -> dict:
    """Update an existing item in the cart by product_id.

    Args:
        product_id: The product ID of the cart item to update.
        size: New size (optional).
        color: New color (optional).
        quantity: New quantity (optional).

    Example:
        update_cart_item_tool(product_id="PROD021", size="L")
    """
    cart_data = manage_cart_tool.invoke({"action": "show"})
    items = cart_data.get("items", [])

    for item in items:
        if item["product_id"] == product_id:
            updated = {
                "product_id": product_id,
                "quantity": quantity if quantity is not None else item["quantity"],
                "size": size if size is not None else item["size"],
                "color": color if color is not None else item["color"],
            }
            return manage_cart_tool.invoke({"action": "update", "items": [updated]})

    return {"error": f"Product {product_id} not found in cart."}

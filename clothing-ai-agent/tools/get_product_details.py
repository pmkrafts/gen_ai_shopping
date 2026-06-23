from langchain.tools import tool
from data.store import get_product_by_id


@tool
def get_product_details_tool(product_id: str) -> dict | str:
    """Get full details for a single product by ID."""
    product = get_product_by_id(product_id)
    if product is None:
        return f"Product {product_id} not found."
    return product.model_dump()
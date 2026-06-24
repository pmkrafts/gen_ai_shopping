from typing import Any
from langchain.tools import tool
from data.store import search_products


@tool
def search_products_tool(
    query: str, filters: dict[str, Any] | None = None
) -> list[dict[str, Any]]:
    """Search the product catalog by query and filters.

    Args:
        query: Free-text search string.
        filters: Optional dict with keys like color, size, category, min_price, max_price, in_stock.
    """
    results = search_products(query=query, filters=filters or {})
    return [p.model_dump() for p in results]

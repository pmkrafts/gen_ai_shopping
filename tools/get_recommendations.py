from typing import Any
from langchain.tools import tool
from data.store import search_products


@tool
def get_recommendations_tool(
    user_preferences: dict[str, Any], cart_items: list[dict] | None = None
) -> list[dict[str, Any]]:
    """Recommend products based on user preferences and current cart items.

    Args:
        user_preferences: Dict with keys like style, occasion, budget, gender, category.
        cart_items: Optional list of cart items for context.
    """
    filters: dict[str, Any] = {}
    if "budget" in user_preferences:
        filters["max_price"] = user_preferences["budget"]
    if "category" in user_preferences:
        filters["category"] = user_preferences["category"]

    query = (
        user_preferences.get("style", "") + " " + user_preferences.get("occasion", "")
    )
    results = search_products(query=query, filters=filters)
    return [p.model_dump() for p in results[:5]]

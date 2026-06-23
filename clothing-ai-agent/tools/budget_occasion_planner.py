from langchain.tools import tool
from data.store import search_products


@tool
def budget_occasion_planner_tool(budget: float, occasion: str, gender: str | None = None) -> dict:
    """Plan a full outfit for an occasion within a budget."""
    categories = ["top", "trousers", "shoes", "accessory"]
    outfit = []
    remaining = budget

    for category in categories:
        filters = {"category": category, "max_price": remaining}
        results = search_products(query=occasion, filters=filters)
        if results:
            pick = results[0]
            outfit.append(pick.model_dump())
            remaining -= pick.price

    total = sum(item["price"] for item in outfit)
    return {
        "occasion": occasion,
        "budget": budget,
        "outfit": outfit,
        "total": total,
        "currency": "INR",
        "remaining": budget - total,
    }
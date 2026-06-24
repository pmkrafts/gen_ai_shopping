from langchain.tools import tool
from data.store import search_products


@tool
def get_trending_styles_tool(season: str, region: str | None = None) -> dict:
    """Return trending colors and styles for a season and region."""
    trends = {
        "summer": {
            "colors": ["white", "beige", "pastel"],
            "styles": ["linen", "cotton", "floral"],
        },
        "monsoon": {
            "colors": ["navy", "olive", "black"],
            "styles": ["waterproof", "layered"],
        },
        "winter": {
            "colors": ["burgundy", "black", "grey"],
            "styles": ["wool", "knits", "jackets"],
        },
    }
    trend = trends.get(
        season.lower(), {"colors": ["black", "white"], "styles": ["casual"]}
    )
    products = search_products(query=" ".join(trend["styles"]))
    return {
        "season": season,
        "region": region,
        "trending": trend,
        "products": [p.model_dump() for p in products[:5]],
    }

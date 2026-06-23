from langchain.tools import tool


@tool
def size_fit_advisor_tool(height: str, weight: str, body_type: str, product_category: str) -> str:
    """Recommend a clothing size based on height, weight, body type, and product category."""
    # Rule-based fallback; can be enhanced with LLM reasoning later.
    size_map = {
        "shirt": "L",
        "dress": "M",
        "jeans": "32",
        "shoes": "UK 9",
    }
    size = size_map.get(product_category.lower(), "M")
    return f"Based on {height}, {weight}, {body_type} build, we recommend size {size} for {product_category}."
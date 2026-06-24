from langchain.tools import tool
from tools.analyze_image import analyze_image_tool
from data.store import search_products


@tool
def image_search_tool(image_url: str) -> list[dict]:
    """Find products similar to the uploaded image.

    Args:
        image_url: URL of the clothing image to search by.
    """
    analysis = analyze_image_tool.invoke({"image_url": image_url})
    query = " ".join(analysis["tags"] + analysis["colors"])
    results = search_products(query=query)
    return [p.model_dump() for p in results[:5]]

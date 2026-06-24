from langchain.tools import tool


@tool
def analyze_image_tool(image_url: str) -> dict:
    """Analyze a clothing image and return detected tags, colors, and category.

    For now this is a mock implementation. Replace with a real vision model call.
    """
    return {
        "image_url": image_url,
        "category": "dress",
        "colors": ["red", "black"],
        "tags": ["party", "evening"],
    }

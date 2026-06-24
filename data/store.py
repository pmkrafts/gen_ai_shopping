import json
from pathlib import Path
from typing import Any
from models.product import Product

_DATA_PATH = Path(__file__).parent / "products.json"


def _load_raw() -> list[dict[str, Any]]:
    with open(_DATA_PATH, encoding="utf-8") as f:
        return json.load(f)


def get_products() -> list[Product]:
    return [Product(**p) for p in _load_raw()]


def get_product_by_id(product_id: str) -> Product | None:
    for p in _load_raw():
        if p["id"] == product_id:
            return Product(**p)
    return None


def _matches_query(product: Product, query: str) -> bool:
    """Check if all words in query match the product text (word-level substring)."""
    text = f"{product.title} {product.description} {' '.join(product.tags)}"
    text_words = text.lower().split()
    query_words = [w for w in query.lower().split() if w]

    for qw in query_words:
        if not any(qw in tw or tw in qw for tw in text_words):
            return False
    return True


def search_products(
    query: str | None = None,
    filters: dict[str, Any] | None = None,
) -> list[Product]:
    filters = filters or {}
    products = get_products()
    results = []

    for product in products:
        if query and not _matches_query(product, query):
            continue

        match = True
        for key, value in filters.items():
            if key == "min_price" and product.price < value:
                match = False
            elif key == "max_price" and product.price > value:
                match = False
            elif key == "color" and value.lower() not in [
                c.lower() for c in product.colors
            ]:
                match = False
            elif key == "size" and value.upper() not in [
                s.upper() for s in product.sizes
            ]:
                match = False
            elif key == "category" and product.category.lower() != value.lower():
                match = False
            elif key == "in_stock" and value and product.stock <= 0:
                match = False

        if match:
            results.append(product)

    return results

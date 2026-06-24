from tools.search_products import search_products_tool


def test_uc01_natural_language_search():
    result = search_products_tool.invoke(
        {
            "query": "red dress",
            "filters": {"max_price": 2000, "size": "M"},
        }
    )
    assert isinstance(result, list)
    assert len(result) > 0
    for product in result:
        assert product["price"] <= 2000
        assert "M" in [s.upper() for s in product["sizes"]]

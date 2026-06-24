from tools.search_products import search_products_tool


def test_search_by_color():
    results = search_products_tool.invoke({"query": "red dress"})
    assert isinstance(results, list)

from tools.image_search import image_search_tool


def test_image_search_returns_list():
    result = image_search_tool.invoke({"image_url": "https://example.com/red-dress.jpg"})
    assert isinstance(result, list)
    assert len(result) <= 5


def test_image_search_returns_dicts():
    result = image_search_tool.invoke({"image_url": "https://example.com/test.jpg"})
    for product in result:
        assert "id" in product
        assert "title" in product

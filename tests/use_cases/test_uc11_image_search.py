from tools.image_search import image_search_tool


def test_uc11_image_search():
    result = image_search_tool.invoke(
        {"image_url": "https://example.com/red-dress.jpg"}
    )
    assert isinstance(result, list)
    assert len(result) <= 5
    for product in result:
        assert "id" in product
        assert "title" in product

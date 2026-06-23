from tools.analyze_image import analyze_image_tool


def test_analyze_image_returns_dict():
    result = analyze_image_tool.invoke({
        "image_url": "https://example.com/red-dress.jpg"
    })
    assert isinstance(result, dict)


def test_analyze_image_includes_url():
    url = "https://example.com/sample.jpg"
    result = analyze_image_tool.invoke({"image_url": url})
    assert result["image_url"] == url


def test_analyze_image_has_required_keys():
    result = analyze_image_tool.invoke({
        "image_url": "https://example.com/test.jpg"
    })
    assert "category" in result
    assert "colors" in result
    assert "tags" in result
    assert isinstance(result["colors"], list)
    assert isinstance(result["tags"], list)

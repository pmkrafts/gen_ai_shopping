from tools.get_trending_styles import get_trending_styles_tool


def test_uc08_trending_styles():
    result = get_trending_styles_tool.invoke({"season": "monsoon", "region": "India"})
    assert result["season"] == "monsoon"
    assert "trending" in result
    assert isinstance(result["products"], list)

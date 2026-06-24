from tools.get_trending_styles import get_trending_styles_tool


def test_trending_styles_summer():
    result = get_trending_styles_tool.invoke({"season": "summer", "region": "India"})

    assert result["season"] == "summer"
    assert result["region"] == "India"
    assert "trending" in result
    assert "white" in result["trending"]["colors"]
    assert "linen" in result["trending"]["styles"]
    assert isinstance(result["products"], list)
    assert len(result["products"]) <= 5


def test_trending_styles_monsoon():
    result = get_trending_styles_tool.invoke({"season": "monsoon", "region": "Mumbai"})

    assert result["season"] == "monsoon"
    assert result["region"] == "Mumbai"
    assert "navy" in result["trending"]["colors"]
    assert "waterproof" in result["trending"]["styles"]


def test_trending_styles_winter():
    result = get_trending_styles_tool.invoke({"season": "winter"})

    assert result["season"] == "winter"
    assert result["region"] is None
    assert "burgundy" in result["trending"]["colors"]
    assert "wool" in result["trending"]["styles"]


def test_trending_styles_unknown_season():
    result = get_trending_styles_tool.invoke({"season": "autumn"})

    assert result["season"] == "autumn"
    assert "colors" in result["trending"]
    assert "styles" in result["trending"]

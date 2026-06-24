from tools.get_recommendations import get_recommendations_tool


def test_uc03_personalized_recommendations():
    result = get_recommendations_tool.invoke(
        {
            "user_preferences": {
                "style": "casual",
                "occasion": "office",
                "budget": 3000,
                "category": "top",
            },
            "cart_items": [],
        }
    )
    assert isinstance(result, list)
    for product in result:
        assert product["price"] <= 3000

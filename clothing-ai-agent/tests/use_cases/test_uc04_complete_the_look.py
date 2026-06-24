from tools.get_recommendations import get_recommendations_tool


def test_uc04_complete_the_look():
    cart_items = [
        {"product_id": "PROD002", "quantity": 1, "size": "M", "color": "blue"}
    ]
    result = get_recommendations_tool.invoke(
        {
            "user_preferences": {
                "style": "casual",
                "occasion": "weekend",
                "budget": 2500,
            },
            "cart_items": cart_items,
        }
    )
    assert isinstance(result, list)
    assert len(result) <= 5

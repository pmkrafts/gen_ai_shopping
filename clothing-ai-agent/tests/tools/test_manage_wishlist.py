from tools.manage_wishlist import manage_wishlist_tool


def test_wishlist_add_and_list():
    manage_wishlist_tool.invoke({"action": "clear"})
    result = manage_wishlist_tool.invoke(
        {
            "action": "add",
            "product_ids": ["PROD001", "PROD002"],
        }
    )
    assert "PROD001" in result
    assert "PROD002" in result


def test_wishlist_remove():
    manage_wishlist_tool.invoke({"action": "clear"})
    manage_wishlist_tool.invoke(
        {"action": "add", "product_ids": ["PROD001", "PROD002"]}
    )
    result = manage_wishlist_tool.invoke(
        {"action": "remove", "product_ids": ["PROD001"]}
    )
    assert "PROD001" not in result
    assert "PROD002" in result


def test_wishlist_clear():
    manage_wishlist_tool.invoke({"action": "add", "product_ids": ["PROD001"]})
    result = manage_wishlist_tool.invoke({"action": "clear"})
    assert result == []

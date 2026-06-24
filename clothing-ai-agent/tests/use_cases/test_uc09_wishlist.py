from tools.manage_wishlist import manage_wishlist_tool


def test_uc09_wishlist():
    manage_wishlist_tool.invoke({"action": "clear"})

    result = manage_wishlist_tool.invoke(
        {
            "action": "add",
            "product_ids": ["PROD001", "PROD002"],
        }
    )
    assert "PROD001" in result
    assert "PROD002" in result

    result = manage_wishlist_tool.invoke({"action": "list"})
    assert len(result) == 2

    manage_wishlist_tool.invoke({"action": "remove", "product_ids": ["PROD001"]})
    result = manage_wishlist_tool.invoke({"action": "list"})
    assert "PROD001" not in result
    assert "PROD002" in result

from tools.manage_cart import manage_cart_tool


def test_uc05_cart_management():
    manage_cart_tool.invoke({"action": "clear"})

    manage_cart_tool.invoke(
        {
            "action": "add",
            "items": [
                {"product_id": "PROD001", "quantity": 1, "size": "M", "color": "red"}
            ],
        }
    )
    cart = manage_cart_tool.invoke({"action": "show"})
    assert len(cart["items"]) == 1

    manage_cart_tool.invoke(
        {
            "action": "update",
            "items": [
                {"product_id": "PROD001", "quantity": 1, "size": "L", "color": "red"}
            ],
        }
    )
    cart = manage_cart_tool.invoke({"action": "show"})
    assert cart["items"][0]["size"] == "L"

    manage_cart_tool.invoke({"action": "remove", "items": [{"product_id": "PROD001"}]})
    cart = manage_cart_tool.invoke({"action": "show"})
    assert len(cart["items"]) == 0

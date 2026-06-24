from tools.update_cart_item import update_cart_item_tool
from tools.manage_cart import manage_cart_tool


def test_update_cart_item_size():
    manage_cart_tool.invoke({"action": "clear"})
    manage_cart_tool.invoke(
        {
            "action": "add",
            "items": [
                {"product_id": "PROD021", "quantity": 1, "size": "M", "color": "yellow"}
            ],
        }
    )
    result = update_cart_item_tool.invoke({"product_id": "PROD021", "size": "L"})
    assert result["items"][0]["size"] == "L"
    assert result["items"][0]["color"] == "yellow"


def test_update_cart_item_not_in_cart():
    manage_cart_tool.invoke({"action": "clear"})
    result = update_cart_item_tool.invoke({"product_id": "PROD999", "size": "L"})
    assert "error" in result

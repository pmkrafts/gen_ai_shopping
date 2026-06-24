from tools.manage_cart import manage_cart_tool


def test_cart_add_and_show():
    manage_cart_tool.invoke({"action": "clear"})
    manage_cart_tool.invoke({
        "action": "add",
        "items": [{"product_id": "PROD001", "quantity": 1, "size": "M", "color": "red"}],
    })
    result = manage_cart_tool.invoke({"action": "show"})
    assert len(result["items"]) == 1
    assert result["items"][0]["product_id"] == "PROD001"


def test_cart_update():
    manage_cart_tool.invoke({"action": "clear"})
    manage_cart_tool.invoke({
        "action": "add",
        "items": [{"product_id": "PROD001", "quantity": 1, "size": "M", "color": "red"}],
    })
    manage_cart_tool.invoke({
        "action": "update",
        "items": [{"product_id": "PROD001", "quantity": 1, "size": "L", "color": "red"}],
    })
    result = manage_cart_tool.invoke({"action": "show"})
    assert result["items"][0]["size"] == "L"


def test_cart_remove():
    manage_cart_tool.invoke({"action": "clear"})
    manage_cart_tool.invoke({
        "action": "add",
        "items": [{"product_id": "PROD001", "quantity": 1, "size": "M", "color": "red"}],
    })
    manage_cart_tool.invoke({"action": "remove", "items": [{"product_id": "PROD001"}]})
    result = manage_cart_tool.invoke({"action": "show"})
    assert len(result["items"]) == 0


def test_cart_clear():
    manage_cart_tool.invoke({
        "action": "add",
        "items": [{"product_id": "PROD001", "quantity": 1, "size": "M", "color": "red"}],
    })
    result = manage_cart_tool.invoke({"action": "clear"})
    assert len(result["items"]) == 0

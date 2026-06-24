from tools.process_order import process_order_tool
from tools.manage_cart import manage_cart_tool


def test_process_order_empty_cart():
    manage_cart_tool.invoke({"action": "clear"})
    result = process_order_tool.invoke(
        {
            "customer_name": "Aarav Sharma",
            "shipping_address": "Mumbai",
        }
    )
    assert "error" in result


def test_process_order_with_items():
    manage_cart_tool.invoke({"action": "clear"})
    manage_cart_tool.invoke(
        {
            "action": "add",
            "items": [
                {"product_id": "PROD001", "quantity": 1, "size": "M", "color": "red"},
            ],
        }
    )
    result = process_order_tool.invoke(
        {
            "customer_name": "Aarav Sharma",
            "shipping_address": "Mumbai",
        }
    )
    assert "error" not in result
    assert result["customer_name"] == "Aarav Sharma"
    assert len(result["items"]) == 1
    assert result["status"] == "confirmed"

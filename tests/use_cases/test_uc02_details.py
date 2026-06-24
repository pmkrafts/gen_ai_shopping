from tools.get_product_details import get_product_details_tool


def test_uc02_product_details():
    result = get_product_details_tool.invoke({"product_id": "PROD001"})
    assert isinstance(result, dict)
    assert result["id"] == "PROD001"


def test_uc02_product_comparison():
    prod1 = get_product_details_tool.invoke({"product_id": "PROD001"})
    prod2 = get_product_details_tool.invoke({"product_id": "PROD002"})
    assert prod1["id"] != prod2["id"]
    assert "price" in prod1
    assert "price" in prod2

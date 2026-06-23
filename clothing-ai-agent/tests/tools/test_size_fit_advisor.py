from tools.size_fit_advisor import size_fit_advisor_tool


def test_size_fit_advisor_shirt():
    result = size_fit_advisor_tool.invoke({
        "height": "5'10\"",
        "weight": "75kg",
        "body_type": "broad",
        "product_category": "shirt",
    })
    assert "L" in result
    assert "shirt" in result


def test_size_fit_advisor_jeans():
    result = size_fit_advisor_tool.invoke({
        "height": "5'8\"",
        "weight": "70kg",
        "body_type": "average",
        "product_category": "jeans",
    })
    assert "32" in result
    assert "jeans" in result


def test_size_fit_advisor_unknown_category():
    result = size_fit_advisor_tool.invoke({
        "height": "5'6\"",
        "weight": "60kg",
        "body_type": "slim",
        "product_category": "jumpsuit",
    })
    assert "M" in result
    assert "jumpsuit" in result

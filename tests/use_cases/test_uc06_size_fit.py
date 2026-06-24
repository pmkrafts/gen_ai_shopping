from tools.size_fit_advisor import size_fit_advisor_tool


def test_uc06_size_fit_advisor():
    result = size_fit_advisor_tool.invoke(
        {
            "height": "5'10\"",
            "weight": "75kg",
            "body_type": "broad",
            "product_category": "shirt",
        }
    )
    assert "L" in result
    assert "shirt" in result

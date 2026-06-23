from tools.budget_occasion_planner import budget_occasion_planner_tool


def test_budget_planner():
    result = budget_occasion_planner_tool.invoke({
        "budget": 5000.0,
        "occasion": "casual",
        "gender": "male",
    })
    assert result["budget"] == 5000.0
    assert result["occasion"] == "casual"
    assert result["total"] <= 5000.0
    assert len(result["outfit"]) > 0


def test_budget_planner_empty_for_low_budget():
    result = budget_occasion_planner_tool.invoke({
        "budget": 100.0,
        "occasion": "casual",
        "gender": "male",
    })
    assert result["budget"] == 100.0
    assert result["total"] == 0
    assert len(result["outfit"]) == 0

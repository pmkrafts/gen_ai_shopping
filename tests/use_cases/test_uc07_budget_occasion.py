from tools.budget_occasion_planner import budget_occasion_planner_tool


def test_uc07_budget_occasion_planner():
    result = budget_occasion_planner_tool.invoke(
        {
            "budget": 5000,
            "occasion": "wedding",
            "gender": "male",
        }
    )
    assert result["budget"] == 5000
    assert result["total"] <= 5000
    assert len(result["outfit"]) > 0

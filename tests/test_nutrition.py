from src.nutrition import NutritionInputs, calculate_bmr, calculate_plan


def test_calculate_bmr_male():
    assert round(calculate_bmr(80, 180, 30, "male"), 1) == 1780.0


def test_calculate_plan_outputs_positive_values():
    plan = calculate_plan(
        NutritionInputs(
            weight_kg=75,
            height_cm=175,
            age=30,
            gender="male",
            activity_level="moderate",
            deficit_level="moderate",
        )
    )
    assert plan.bmr > 0
    assert plan.tdee > plan.bmr
    assert plan.target_calories < plan.tdee
    assert plan.protein_g > 0
    assert plan.fat_g > 0
    assert plan.carbs_g > 0

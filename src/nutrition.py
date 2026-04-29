"""Core nutrition calculations for the Streamlit calorie planner.

This module intentionally keeps the calculation layer independent from the
Streamlit UI so the app is easier to test, reuse, and extend.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

Gender = Literal["male", "female"]
ActivityLevel = Literal["sedentary", "light", "moderate", "very_active", "athlete"]
DeficitLevel = Literal["conservative", "moderate", "aggressive", "very_aggressive"]

ACTIVITY_FACTORS: dict[ActivityLevel, float] = {
    "sedentary": 1.20,
    "light": 1.375,
    "moderate": 1.55,
    "very_active": 1.725,
    "athlete": 1.90,
}

DEFICIT_RATES: dict[DeficitLevel, float] = {
    "conservative": 0.125,
    "moderate": 0.225,
    "aggressive": 0.325,
    "very_aggressive": 0.40,
}

DEFAULT_MACRO_SPLIT = {
    "protein": 0.30,
    "fat": 0.25,
    "carbs": 0.45,
}


@dataclass(frozen=True)
class NutritionInputs:
    """Input profile for calorie and macronutrient planning."""

    weight_kg: float
    height_cm: float
    age: int
    gender: Gender
    activity_level: ActivityLevel
    deficit_level: DeficitLevel


@dataclass(frozen=True)
class NutritionPlan:
    """Calculated output for a weight-loss nutrition plan."""

    bmr: float
    tdee: float
    target_calories: float
    deficit_rate: float
    protein_g: float
    fat_g: float
    carbs_g: float
    warning: str | None = None


def calculate_bmr(weight_kg: float, height_cm: float, age: int, gender: Gender) -> float:
    """Calculate basal metabolic rate using the Mifflin-St Jeor equation."""
    _validate_positive(weight_kg, "weight_kg")
    _validate_positive(height_cm, "height_cm")
    _validate_positive(age, "age")

    if gender == "male":
        return 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    if gender == "female":
        return 10 * weight_kg + 6.25 * height_cm - 5 * age - 161
    raise ValueError("gender must be 'male' or 'female'")


def calculate_plan(inputs: NutritionInputs) -> NutritionPlan:
    """Calculate BMR, TDEE, calorie target, and macro grams."""
    if inputs.activity_level not in ACTIVITY_FACTORS:
        raise ValueError("Invalid activity level")
    if inputs.deficit_level not in DEFICIT_RATES:
        raise ValueError("Invalid deficit level")

    bmr = calculate_bmr(inputs.weight_kg, inputs.height_cm, inputs.age, inputs.gender)
    tdee = bmr * ACTIVITY_FACTORS[inputs.activity_level]
    deficit_rate = DEFICIT_RATES[inputs.deficit_level]
    target_calories = tdee * (1 - deficit_rate)

    protein_g = target_calories * DEFAULT_MACRO_SPLIT["protein"] / 4
    fat_g = target_calories * DEFAULT_MACRO_SPLIT["fat"] / 9
    carbs_g = target_calories * DEFAULT_MACRO_SPLIT["carbs"] / 4

    warning = None
    if deficit_rate >= 0.325:
        warning = (
            "This deficit is aggressive. Monitor adherence, energy, hunger, "
            "training performance, and consider professional guidance."
        )

    return NutritionPlan(
        bmr=bmr,
        tdee=tdee,
        target_calories=target_calories,
        deficit_rate=deficit_rate,
        protein_g=protein_g,
        fat_g=fat_g,
        carbs_g=carbs_g,
        warning=warning,
    )


def _validate_positive(value: float, field_name: str) -> None:
    if value <= 0:
        raise ValueError(f"{field_name} must be greater than zero")

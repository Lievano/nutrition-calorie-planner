"""Streamlit UI for the nutrition calorie planner."""

from __future__ import annotations

import sys
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from src.nutrition import ACTIVITY_FACTORS, DEFICIT_RATES, NutritionInputs, calculate_plan

ACTIVITY_LABELS = {
    "sedentary": "Sedentary - little or no exercise",
    "light": "Light - exercise 1 to 3 days/week",
    "moderate": "Moderate - exercise 3 to 5 days/week",
    "very_active": "Very active - daily training or intense work",
    "athlete": "Athlete - intense training or double sessions",
}

DEFICIT_LABELS = {
    "conservative": "Conservative - 12.5% deficit",
    "moderate": "Moderate - 22.5% deficit",
    "aggressive": "Aggressive - 32.5% deficit",
    "very_aggressive": "Very aggressive - 40% deficit",
}

GENDER_LABELS = {
    "male": "Male",
    "female": "Female",
}

st.set_page_config(
    page_title="Nutrition Calorie Planner",
    page_icon="🥗",
    layout="centered",
)

st.title("🥗 Nutrition Calorie Planner")
st.caption("A lightweight decision-support app for estimating calorie targets and macronutrients for weight loss.")

with st.sidebar:
    st.header("Profile")
    weight_kg = st.number_input("Weight (kg)", min_value=1.0, value=75.0, step=0.5)
    height_cm = st.number_input("Height (cm)", min_value=1.0, value=175.0, step=0.5)
    age = st.number_input("Age", min_value=1, value=30, step=1)
    gender = st.selectbox("Gender", options=list(GENDER_LABELS), format_func=lambda x: GENDER_LABELS[x])
    activity_level = st.selectbox(
        "Activity level",
        options=list(ACTIVITY_FACTORS),
        index=2,
        format_func=lambda x: ACTIVITY_LABELS[x],
    )
    deficit_level = st.selectbox(
        "Deficit intensity",
        options=list(DEFICIT_RATES),
        index=1,
        format_func=lambda x: DEFICIT_LABELS[x],
    )
    calculate = st.button("Calculate plan", type="primary")

st.markdown(
    """
### What this app does
This tool estimates maintenance calories, applies a selected calorie deficit, and converts the target into a simple macronutrient split.

It is designed as a **personal nutrition planning calculator**, not as medical advice or a replacement for a registered dietitian.
"""
)

if calculate:
    inputs = NutritionInputs(
        weight_kg=weight_kg,
        height_cm=height_cm,
        age=int(age),
        gender=gender,
        activity_level=activity_level,
        deficit_level=deficit_level,
    )
    plan = calculate_plan(inputs)

    st.subheader("Daily targets")
    c1, c2, c3 = st.columns(3)
    c1.metric("BMR", f"{plan.bmr:,.0f} kcal")
    c2.metric("TDEE", f"{plan.tdee:,.0f} kcal")
    c3.metric("Target", f"{plan.target_calories:,.0f} kcal")

    st.subheader("Macronutrients")
    m1, m2, m3 = st.columns(3)
    m1.metric("Protein", f"{plan.protein_g:,.0f} g")
    m2.metric("Fat", f"{plan.fat_g:,.0f} g")
    m3.metric("Carbs", f"{plan.carbs_g:,.0f} g")

    st.info(f"Applied deficit: {plan.deficit_rate:.1%}")
    if plan.warning:
        st.warning(plan.warning)

st.divider()
st.markdown(
    """
### Method
- **BMR:** Mifflin-St Jeor equation.
- **TDEE:** BMR multiplied by an activity factor.
- **Calorie target:** TDEE minus the selected deficit.
- **Macros:** 30% protein, 25% fat, 45% carbohydrates.

### Safety note
Large deficits may reduce adherence, training quality, and lean-mass retention. Use this as a planning estimate and consult a professional for medical or clinical nutrition decisions.
"""
)

# Nutrition Calorie Planner

## Executive Summary

This project provides an interactive Streamlit application for estimating daily calorie targets and macronutrient distribution for weight-loss planning.

The app is structured as a lightweight decision-support tool: user inputs are converted into basal metabolic rate, total daily energy expenditure, a calorie target, and macro recommendations. The calculation logic is separated from the Streamlit interface so it can be tested, reused, and extended.

## Product Problem

Many beginner nutrition calculators are presented as opaque forms. Users often receive a calorie number without understanding the underlying assumptions: metabolic equation, activity multiplier, deficit intensity, and macro split.

This project solves that by making the full logic explicit and readable.

## Technical Objective

Build a reproducible Streamlit application that:

- collects user profile inputs
- calculates BMR with Mifflin-St Jeor
- estimates TDEE using activity multipliers
- applies a selected calorie deficit
- converts calorie targets into macronutrient grams
- displays warnings for aggressive deficits
- keeps calculation logic modular and testable

## Methodology

### 1. Input Layer

The app collects:

- weight
- height
- age
- gender
- activity level
- deficit intensity

### 2. Calculation Layer

The core logic lives in `src/nutrition.py` and uses:

- Mifflin-St Jeor for BMR
- activity factors for TDEE
- configurable deficit rates
- a default macro split of 30% protein, 25% fat, and 45% carbohydrates

### 3. Interface Layer

The Streamlit app in `app/streamlit_app.py` presents:

- profile controls in the sidebar
- key metrics as visual cards
- macronutrient outputs
- method notes and safety warnings

### 4. Validation Layer

Basic tests are included in `tests/test_nutrition.py` to verify that the calculation module produces valid outputs and expected BMR values.

## Application Logic

```text
User profile
    ↓
BMR calculation
    ↓
Activity multiplier
    ↓
TDEE estimate
    ↓
Deficit adjustment
    ↓
Calories + macros
```

## Repository Structure

```text
nutrition-calorie-planner/
├── app/
│   └── streamlit_app.py
├── src/
│   └── nutrition.py
├── tests/
│   └── test_nutrition.py
├── reports/
│   └── figures/
├── docs/
│   ├── INTERVIEW_EN.md
│   ├── INTERVIEW_ES.md
│   ├── results_summary.md
│   ├── notes.md
│   └── figures/
├── README.md
├── README_EN.md
├── README_ES.md
├── requirements.txt
└── .gitignore
```

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app/streamlit_app.py
```

Run tests:

```bash
pytest
```

## Safety Note

This project is educational and informational. It does not replace professional medical or nutritional advice.

## Next Steps

Recommended improvements:

1. Add user-defined macro splits.
2. Export results to CSV or PDF.
3. Save historical calculations locally.
4. Add metric/imperial unit conversion.
5. Add protein recommendations based on body weight.
6. Deploy the app on Streamlit Community Cloud.

## Portfolio Positioning

This project demonstrates:

- Streamlit application development
- clean separation between UI and logic
- testable Python design
- user-facing decision-support workflow
- transparent health-tech calculation assumptions

# Nutrition Calorie Planner

Streamlit application for estimating weight-loss calorie targets and macronutrient distribution from user profile, activity level, and deficit intensity.

## Project Access

- English documentation: [README_EN.md](README_EN.md)
- Documentación en español: [README_ES.md](README_ES.md)
- Streamlit app: [app/streamlit_app.py](app/streamlit_app.py)
- Core calculation module: [src/nutrition.py](src/nutrition.py)

## Quick Start

```bash
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

## What This Project Demonstrates

- Separation between UI and reusable calculation logic
- Streamlit app design for interactive decision support
- BMR and TDEE estimation using Mifflin-St Jeor
- Calorie deficit planning with transparent assumptions
- Macronutrient conversion from calorie targets
- Basic automated tests for core calculations

## Key Insight

The project is a small decision-support application that turns user inputs into transparent nutrition planning estimates with safety warnings and reusable business logic.

# Planificador de Calorías y Nutrición

## Resumen Ejecutivo

Este proyecto construye una aplicación interactiva con Streamlit para estimar calorías objetivo y distribución de macronutrientes en un plan de pérdida de peso.

La aplicación está planteada como una herramienta ligera de apoyo a la decisión: convierte datos del usuario en tasa metabólica basal, gasto energético total, calorías objetivo y gramos recomendados de proteína, grasa y carbohidratos. La lógica de cálculo está separada de la interfaz para facilitar pruebas, reutilización y futuras mejoras.

## Problema del Producto

Muchas calculadoras nutricionales entregan un número de calorías sin explicar las suposiciones detrás del resultado: fórmula metabólica, factor de actividad, intensidad del déficit y proporción de macronutrientes.

Este proyecto resuelve ese problema haciendo visible y trazable el cálculo completo.

## Objetivo Técnico

Construir una aplicación reproducible con Streamlit que:

- reciba datos básicos del usuario
- calcule TMB con Mifflin-St Jeor
- estime GET mediante factores de actividad
- aplique un déficit calórico seleccionado
- convierta calorías objetivo en gramos de macronutrientes
- muestre advertencias para déficits agresivos
- mantenga la lógica modular y testeable

## Metodología

### 1. Capa de Entrada

La app solicita:

- peso
- altura
- edad
- género
- nivel de actividad
- intensidad del déficit

### 2. Capa de Cálculo

La lógica central vive en `src/nutrition.py` y usa:

- Mifflin-St Jeor para TMB
- factores de actividad para GET
- tasas de déficit configurables
- una división base de macros: 30% proteína, 25% grasa y 45% carbohidratos

### 3. Capa de Interfaz

La app de Streamlit en `app/streamlit_app.py` presenta:

- controles en la barra lateral
- métricas principales en tarjetas
- gramos de macronutrientes
- explicación del método y advertencias de seguridad

### 4. Capa de Validación

Se incluyen pruebas básicas en `tests/test_nutrition.py` para comprobar que el módulo de cálculo produce salidas válidas y valores esperados de TMB.

## Lógica de la Aplicación

```text
Perfil del usuario
    ↓
Cálculo de TMB
    ↓
Factor de actividad
    ↓
Estimación de GET
    ↓
Ajuste por déficit
    ↓
Calorías + macros
```

## Estructura del Repositorio

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

## Cómo Ejecutar

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar la aplicación:

```bash
streamlit run app/streamlit_app.py
```

Ejecutar pruebas:

```bash
pytest
```

## Nota de Seguridad

Este proyecto es educativo e informativo. No sustituye asesoría médica o nutricional profesional.

## Próximos Pasos

Mejoras recomendadas:

1. Permitir proporciones de macros personalizadas.
2. Exportar resultados a CSV o PDF.
3. Guardar historial de cálculos.
4. Agregar conversión entre unidades métricas e imperiales.
5. Agregar recomendaciones de proteína por kg de peso corporal.
6. Desplegar la app en Streamlit Community Cloud.

## Posicionamiento de Portafolio

Este proyecto demuestra:

- desarrollo de aplicaciones con Streamlit
- separación limpia entre interfaz y lógica
- diseño Python testeable
- flujo de apoyo a decisiones para usuario final
- supuestos transparentes en cálculos de health-tech

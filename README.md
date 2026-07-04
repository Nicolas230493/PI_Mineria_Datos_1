# Proyecto Integrador: Minería de Datos I
Pipeline de análisis de datos sobre comportamiento y consumo de usuarios de una plataforma de streaming latinoamericana.

## Información general
- **Integrantes:** Nicolás Daniel Segovia Albarado y Joaquin Corvalan Celiz
- **Comisión:** Turno Tarde — Sede Nodo Tecnológico
- **Fecha:** Junio 2026

## Objetivo del proyecto
Aplicar los contenidos de Minería de Datos I para construir un pipeline de análisis de datos reproducible, con decisiones justificadas y trazabilidad del proceso completo. El proyecto incluye inspección inicial, limpieza, análisis exploratorio, reducción de dimensionalidad mediante PCA y comunicación de resultados mediante una aplicación pública en Streamlit.

## Dataset
- **Nombre:** streaming_users_dirty
- **Formato original:** JSON
- **Registros originales:** 8.160 filas
- **Registros finales:** 8.000 filas
- **Columnas:** 8 variables (user_id, age, subscription_plan, monthly_watch_time_mins, country, favorite_genre, last_login_date, customer_support_tickets)
- **Descripción:** Usuarios de una plataforma de streaming de 7 países latinoamericanos (Argentina, Brasil, Chile, Colombia, México, Perú, Uruguay) con información demográfica, de consumo y de soporte técnico.
- **Dataset original:** `data/raw/streaming_users_dirty.json`
- **Dataset procesado:** `data/processed/streaming_users_clean.csv`

## Estructura del repositorio

PI_Mineria_Datos_1/
├── README.md
├── requirements.txt
├── data/
│ ├── raw/
│ └── processed/
├── notebooks/
│ ├── 01_inspeccion_inicial.ipynb
│ ├── 02_calidad_y_limpieza.ipynb
│ ├── 03_eda.ipynb
│ ├── 04_pca.ipynb
│ └── 05_conclusiones.ipynb
├── app/
│ ├── Home.py
│ └── pages/
│ ├── 01_Dataset.py
│ ├── 02_EDA.py
│ ├── 03_PCA.py
│ └── 04_Conclusiones.py
├── reports/
│ └── informe_final.pdf
└── logs/
└── pipeline_log.csv

## Preparación y calidad de datos
El dataset original presentaba duplicados exactos (126 filas), user_id duplicados (34 usuarios con más de un registro), 15 variantes en subscription_plan, 26 en country y 29 en favorite_genre. Se detectaron valores negativos en age, monthly_watch_time_mins y customer_support_tickets, outliers extremos y fechas inválidas en last_login_date. Se realizó análisis MCAR/MAR/MNAR identificando que los nulos en monthly_watch_time_mins son MAR. Todas las decisiones están documentadas en `logs/pipeline_log.csv` y justificadas en `notebooks/02_calidad_y_limpieza.ipynb`.

## Resumen del análisis exploratorio
El EDA incluyó análisis univariado, bivariado y multivariado. El usuario típico tiene 35 años, consume alrededor de 750 minutos mensuales y abre entre 0 y 1 tickets de soporte. La distribución por país es equilibrada. El plan Básico concentra el 45% de los usuarios en todos los mercados. La matriz de correlación mostró que las variables numéricas son prácticamente independientes entre sí, con correlaciones menores a 0.02 en valor absoluto. Ver `notebooks/03_eda.ipynb`.

## Reducción de dimensionalidad
Se aplicó One-Hot Encoding sobre las variables categóricas y StandardScaler sobre todas las variables antes del PCA. Se necesitan 13 componentes para explicar el 80% de la varianza y 14 para el 90%, lo que refleja la baja correlación entre variables. PC1 captura la dimensión de plan y consumo, mientras que PC2 captura preferencias de contenido y origen geográfico. Ver `notebooks/04_pca.ipynb`.

## Visualización interactiva
La aplicación Streamlit incluye 5 páginas: Home, Dataset, EDA, PCA y Conclusiones. El EDA presenta 2 visualizaciones univariadas, 2 bivariadas y 1 multivariada con interpretación para cada una. Enlace público: [Aplicación en Streamlit Cloud](https://pimineriadatos1-ws4febtporanq5vkpgkhjn.streamlit.app/)

## Cómo ejecutar localmente
1. Clonar el repositorio: `git clone https://github.com/Nicolas230493/PI_Mineria_Datos_1.git`
2. Crear entorno virtual: `python -m venv .venv`
3. Activar entorno: `source .venv/bin/activate` (Linux/Mac) o `.venv\Scripts\activate` (Windows)
4. Instalar dependencias: `pip install -r requirements.txt`
5. Ejecutar la aplicación: `streamlit run app/Home.py`

## Conclusiones
El análisis no encontró correlaciones significativas entre las variables numéricas del dataset. El plan elegido y el consumo no dependen del país ni de la edad. Los tickets de soporte no afectan el consumo mensual. El PCA confirmó la independencia entre variables al requerir 13 componentes para el 80% de varianza. Las limitaciones principales son la imputación aplicada en varias columnas y el alcance condicionado por las variables disponibles.
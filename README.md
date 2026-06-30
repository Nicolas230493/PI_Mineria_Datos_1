# Proyecto Integrador: Minería de Datos I
Tablero interactivo y pipeline analítico sobre el comportamiento y consumo de usuarios de streaming.

## 🎯 Objetivo del Proyecto
El propósito de este proyecto consiste en diseñar e implementar un pipeline reproducible de ciencia de datos para auditar, limpiar y explorar un conjunto de datos ruidoso con 8,124 registros de usuarios de streaming. El análisis busca identificar patrones demográficos, evaluar relaciones de consumo frente a la fricción del servicio y aplicar reducción de dimensionalidad para entender la estructura latente de los datos, garantizando la trazabilidad total del proceso mediante justificaciones analíticas.

## 📂 Estructura del Repositorio
* **`data/`**: Repositorio de datos estructurado en `raw/` (dataset sucio original en formato JSON) y `processed/` (base de datos estabilizada final de 8,000 filas en formato CSV).
* **`notebooks/`**: Secuencia indexada de 5 notebooks (`01_inspeccion_inicial.ipynb` a `05_conclusiones.ipynb`) que contienen el desarrollo técnico, código de curación y el análisis estadístico interactivo.
* **`app/`**: Código fuente de la aplicación multipágina desarrollada en Streamlit (`Home.py` y directorio `pages/`).
* **`logs/`**: Registro auditable de transformaciones estadísticas (`pipeline_log.csv`).
* **`reports/`**: Espacio destinado al documento ejecutivo final.

## 🔧 Instrucciones de Reproducción
1. Clonar este repositorio institucional de GitHub en su entorno local.
2. Crear un entorno virtual de Python 3.12 ejecutando: `python -m venv .venv`.
3. Activar el entorno virtual mediante la terminal de comandos de Linux.
4. Instalar las dependencias exactas del proyecto utilizando: `pip install -r requirements.txt`.
5. Para ejecutar la aplicación interactiva localmente, correr el comando: `streamlit run app/Home.py`.
6. Los notebooks analíticos pueden auditarse secuencialmente iniciando desde la carpeta `notebooks/`.

## 📌 Principales Conclusiones
El pipeline de calidad logró mitigar la pérdida de información estabilizando la base en 8,000 usuarios sin recurrir a filtrados destructivos. El análisis exploratorio (EDA) determinó que el consumo mensual de minutos mantiene una homogeneidad absoluta entre los diferentes planes y países de la región, registrando una correlación lineal nula (-0.01) respecto a los tickets de soporte abiertos. Finalmente, el Análisis de Componentes Principales (PCA) evidenció matemáticamente la bajísima correlación lineal del dataset, requiriendo un espectro amplio de 13 componentes independientes para lograr explicar el 80% de la variabilidad total de los datos.

## 🔗 Enlaces del Proyecto
* [🚀 Aplicación Interactiva en Streamlit Cloud](https://tu-usuario-app.streamlit.app)
* [📓 Notebook 01: Inspección Inicial](notebooks/01_inspeccion_inicial.ipynb)
* [📓 Notebook 02: Limpieza y Calidad](notebooks/02_calidad_y_limpieza.ipynb)
* [📓 Notebook 03: Análisis Exploratorio (EDA)](notebooks/03_eda.ipynb)
* [📓 Notebook 04: Escalamiento y PCA](notebooks/04_pca.ipynb)
* [📓 Notebook 05: Respuestas y Conclusiones](notebooks/05_conclusiones.ipynb)
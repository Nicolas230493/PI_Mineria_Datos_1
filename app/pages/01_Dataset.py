import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dataset - PI Minería de Datos I", page_icon="📅", layout="wide")

st.title("📅 Estructura y Calidad del Dataset")

try:
    df = pd.read_csv("data/processed/streaming_users_clean.csv")
    
    st.markdown("### 🔍 Muestreo Dimensional")
    st.write(f"El dataset consolidado post-limpieza cuenta con exactamente **{df.shape[0]} filas** y **{df.shape[1]} columnas**.")
    
    st.markdown("### 👀 Vista Previa del Dataset Procesado")
    st.dataframe(df.head(10), use_container_width=True)
    
    st.markdown("### 🛡️ Matriz de Decisiones y Trazabilidad (Pipeline Log)")
    st.write("Resumen ejecutivo de las principales anomalías detectadas en la fase de inspección y corregidas en el pipeline:")
    
    # Espejado con tu log_etl real de 12 pasos
    pasos_limpieza = {
        "Paso": [1, 2, 7, 8, 9, 11],
        "Dimensión Afectada": ["Duplicados", "Inconsistencia de Planes", "Outliers Edad", "Outliers Edad", "Consumo Mensual", "last_login_date"],
        "Evidencia Detectada": ["74 filas idénticas", "Siglas mezcladas y minúsculas", "Valores negativos", "Valores mayores a 100", "Negativos, nulos y excesivos", "Nulos, formatos mixtos y fechas futuras"],
        "Acción Aplicada": ["Remoción estricta", "Mapeo con diccionario unificado", "Imputación con Mediana (33)", "Imputación con Mediana (33)", "Imputación con Mediana (756.3)", "Normalización y fecha mediana"],
        "Impacto Final": ["8050 registros", "Estandarización comercial", "8050 registros conservados", "Consistencia etaria", "Consistencia de minutos", "Estructura datetime64 válida"]
    }
    st.table(pd.DataFrame(pasos_limpieza))
    
except FileNotFoundError:
    st.error("⚠️ No se detectó 'streaming_users_clean.csv' en 'data/processed/'. Asegúrate de subirlo al repositorio.")
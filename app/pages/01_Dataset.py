import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dataset - PI Minería de Datos I", page_icon="📅", layout="wide")

st.title("📅 Estructura y Calidad del Dataset")

try:
    df = pd.read_csv("data/processed/streaming_users_clean.csv")
    
    st.markdown("### Descripción general")
    st.write(
        "El dataset contiene información de usuarios de una plataforma de streaming latinoamericana. "
        "Incluye variables demográficas, de comportamiento y comerciales para 8000 usuarios de 7 países."
    )
    
    st.markdown("### Vista previa del dataset procesado")
    st.dataframe(df.head(10), use_container_width=True)
    
    st.markdown("### Resumen de calidad y transformaciones principales")
    pasos_limpieza = pd.DataFrame({
        "Paso": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        "Descripción": [
            "Eliminación de duplicados exactos",
            "Resolución de user_id duplicados",
            "Normalización de subscription_plan",
            "Normalización de country",
            "Normalización de favorite_genre",
            "Análisis MCAR/MAR/MNAR",
            "Imputación por grupo - monthly_watch_time_mins",
            "Tratamiento de outliers - customer_support_tickets",
            "Tratamiento de outliers - age",
            "Tratamiento de outliers y nulos - monthly_watch_time_mins",
            "Imputación de favorite_genre",
            "Tratamiento de last_login_date"
        ],
        "Filas": [8034, 8000, 8000, 8000, 8000, 8000, 8000, 8000, 8000, 8000, 8000, 8000],
        "Nulos": [753, 753, 753, 753, 753, 753, 560, 560, 560, 320, 83, 0],
        "Retención (%)": [98.46, 98.04, 98.04, 98.04, 98.04, 98.04, 98.04, 98.04, 98.04, 98.04, 98.04, 98.04]
    })
    st.dataframe(pasos_limpieza, use_container_width=True)

except FileNotFoundError:
    st.error("No se encontró el archivo 'streaming_users_clean.csv' en 'data/processed/'.")
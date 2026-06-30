import streamlit as st

st.set_page_config(
    page_title="Home - PI Minería de Datos I",
    page_icon="🏠",
    layout="wide"
)

st.title("🚀 Proyecto Integrador: Minería de Datos I")
st.subheader("Análisis de Comportamiento y Consumo de Usuarios de Streaming")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 👥 Integrantes del Grupo")
    st.markdown("- **Nicolas Daniel Segovia Albarado**")
    st.markdown("- **Joaquin Corvalan Celiz**")
    
    st.markdown("### 🏫 Mineria de Datos I")
    st.markdown("- **Comisión:** Turno Tarde - Sede Nodo Tecnologico ")
    st.markdown("- **Fecha:** Junio 2026")

with col2:
    st.markdown("### 📝 Contexto del Proyecto")
    st.write(
        "Este tablero interactivo presenta el ciclo completo de análisis sobre el dataset "
        "de consumo de streaming. Siguiendo un pipeline reproducible, se exponen los resultados "
        "desde la inspección inicial y curación de datos, hasta el análisis exploratorio multivariable "
        "y la reducción de dimensionalidad mediante el Análisis de Componentes Principales (PCA)."
    )
    
    st.markdown("### 🔗 Enlaces Operativos")
    st.markdown("[📂 Repositorio Público de GitHub](https://github.com/tu-usuario/PI_Mineria_Datos_1)")

st.info("💡 Despliega la barra lateral de la izquierda para navegar entre las páginas obligatorias del proyecto.")
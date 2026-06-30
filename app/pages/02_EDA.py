import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="EDA - PI Minería de Datos I", page_icon="📊", layout="wide")

st.title("📊 Análisis Exploratorio de Datos (EDA)")

try:
    df = pd.read_csv("data/processed/streaming_users_clean.csv")
    sns.set_theme(style="whitegrid")
    
    # ---- BLOQUE 1: ANÁLISIS UNIVARIADO (2 GRÁFICOS) ----
    st.markdown("## 🔹 1. Análisis Univariado (Distribuciones)")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Gráfico 1: Representación de Usuarios por País")
        fig, ax = plt.subplots(figsize=(6, 3.8))
        sns.countplot(data=df, x='country', palette='Set2', order=df['country'].value_counts().index, ax=ax)
        plt.xticks(rotation=15)
        st.pyplot(fig)
        st.caption("**Interpretación:** Distribución geográfica equilibrada entre los 7 países de Latinoamérica. Esto asegura que no existan sesgos poblacionales regionales dominantes que distorsionen los posteriores análisis grupales.")

    with col2:
        st.markdown("#### Gráfico 2: Cuota de Mercado por Plan de Suscripción")
        fig, ax = plt.subplots(figsize=(6, 3.8))
        sns.countplot(data=df, x='subscription_plan', palette='Pastel1', ax=ax)
        st.pyplot(fig)
        st.caption("**Interpretación:** El plan Básico lidera la base comercial con un dominio aproximado del 45% tras subsanar los errores de tipeo de la ingesta de datos sucios.")

    # ---- BLOQUE 2: ANÁLISIS BIVARIADO (2 GRÁFICOS) ----
    st.markdown("## 🔹 2. Análisis Bivariado (Relaciones)")
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown("#### Gráfico 3: Dispersión de Consumo vs Soporte Técnico")
        fig, ax = plt.subplots(figsize=(6, 3.8))
        sns.scatterplot(data=df, x='customer_support_tickets', y='monthly_watch_time_mins', color='teal', alpha=0.4, ax=ax)
        st.pyplot(fig)
        st.caption("**Interpretación:** Comportamiento independiente. El coeficiente de correlación nulo (-0.01) demuestra que la fricción operativa (abrir más tickets) no altera negativamente la tasa de consumo de minutos mensuales.")

    with col4:
        st.markdown("#### Gráfico 4: Distribución de Tiempos de Consumo por Plan")
        fig, ax = plt.subplots(figsize=(6, 3.8))
        sns.boxplot(data=df, x='subscription_plan', y='monthly_watch_time_mins', palette='vlag', ax=ax)
        st.pyplot(fig)
        st.caption("**Interpretación:** Los diagramas de caja muestran una homogeneidad absoluta en el consumo. Las medianas y dispersiones de minutos mensuales resultan idénticas sin importar el rango de facturación del plan.")

    # ---- BLOQUE 3: ANÁLISIS MULTIVARIADO (1 GRÁFICO EXACTO) ----
    st.markdown("<h2>🔹 3. Análisis Multivariado</h2>", unsafe_allow_html=True)
    st.markdown("#### Gráfico 5: Análisis Cruzado de Edad, Género Cinematográfico y Suscripción")
    
    g = sns.catplot(
        data=df, x='favorite_genre', y='age', hue='subscription_plan',
        row='subscription_plan', kind='box', height=3.2, aspect=3.5, palette='muted', legend=False
    )
    g.set_titles("Segmento Corporativo: Plan {row_name}")
    g.set_axis_labels("Género Cinematográfico Favorito", "Edad del Usuario")
    g.fig.subplots_adjust(top=0.9)
    g.fig.suptitle('Distribución de Edad por Género y Plan de Suscripción', fontsize=12, fontweight='bold')
    st.pyplot(g.fig)
    st.caption("**Interpretación Multivariable:** Estabilización transversal. Las medianas etarias oscilan simétricamente entre los 30 y 40 años para todas las combinaciones de géneros favoritos y niveles de suscripción, descartando patrones de hiper-segmentación aislados por edad.")

except FileNotFoundError:
    st.error("⚠️ Dataset no encontrado.")
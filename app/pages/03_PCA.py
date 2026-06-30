import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

st.set_page_config(page_title="PCA - PI Minería de Datos I", page_icon="🔬", layout="wide")

st.title("🔬 Reducción de Dimensionalidad (PCA)")

try:
    df = pd.read_csv("data/processed/streaming_users_clean.csv")
    
    # Ingeniería Idéntica a tu Notebook 04
    columnas_categoricas = ['subscription_plan', 'country', 'favorite_genre']
    df_encoded = pd.get_dummies(df, columns=columnas_categoricas, drop_first=True, dtype=int)
    X = df_encoded.drop(columns=['user_id', 'last_login_date'])
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    pca = PCA()
    X_pca = pca.fit_transform(X_scaled)
    
    varianza_individual = pca.explained_variance_ratio_
    varianza_acumulada = np.cumsum(varianza_individual)

    st.markdown("### ⚙️ Pipeline Técnico Aplicado")
    st.write("- **Variables de Entrada:** Preprocesamiento de texto mediante One-Hot Encoding (evitando redundancia con `drop_first=True`).")
    st.write("- **Escalamiento Nivelador:** Aplicación de `StandardScaler` (Media = 0, Varianza = 1) para mitigar la distorsión por diferencias de magnitudes numéricas.")

    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Gráfico 1: Varianza Explicada Acumulada (Scree Plot)")
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(range(1, len(varianza_individual) + 1), varianza_individual, alpha=0.5, color='steelblue', label='Varianza Individual')
        ax.plot(range(1, len(varianza_acumulada) + 1), varianza_acumulada, marker='o', linestyle='--', color='darkorange', label='Varianza Acumulada')
        ax.set_xlabel('Componentes Principales')
        ax.set_ylabel('Proporción de Varianza')
        ax.legend(loc='best')
        st.pyplot(fig)
        st.caption("**Conclusión del Scree Plot:** El ascenso lineal pausado demuestra que se necesitan 13 componentes para explicar el 80% de la varianza. Esto expone matemáticamente la bajísima correlación de las variables originales.")

    with col2:
        st.markdown("#### Gráfico 2: Cargas de Variables Absolutas (PC1)")
        loadings = pd.DataFrame(pca.components_.T, columns=[f'PC{i+1}' for i in range(len(X.columns))], index=X.columns)
        top_pc1 = loadings['PC1'].abs().sort_values(ascending=False).head(5)
        
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.barplot(x=top_pc1.values, y=top_pc1.index, hue=top_pc1.index, palette='Blues_r', legend=False, ax=ax)
        ax.set_xlabel('Peso Absoluto en el Componente Principal 1')
        st.pyplot(fig)
        st.caption("**Interpretación de Cargas:** Desglose del peso absoluto. Identifica qué variables sintéticas mapean la mayor dirección de variabilidad dentro de la base estructurada de usuarios.")

except FileNotFoundError:
    st.error("⚠️ Archivo procesado ausente.")
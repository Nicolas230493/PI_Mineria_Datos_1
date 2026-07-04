import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="EDA - PI Minería de Datos I", page_icon="📊", layout="wide")

st.title("📊 Análisis Exploratorio de Datos (EDA)")

try:
    df = pd.read_csv("data/processed/streaming_users_clean.csv")
    sns.set_theme(style="whitegrid")

    # ---- BLOQUE 1: ANÁLISIS UNIVARIADO ----
    st.markdown("## 1. Análisis Univariado")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Distribución de usuarios por país")
        conteo = df['country'].value_counts()
        porcentajes = (conteo / len(df) * 100).round(2)
        fig, ax = plt.subplots(figsize=(6, 4))
        bars = ax.barh(conteo.index, conteo.values, color=sns.color_palette('Blues_d', len(conteo)))
        for i, (valor, porcentaje) in enumerate(zip(conteo.values, porcentajes.values)):
            ax.text(valor + 5, i, f'{porcentaje}%', va='center', fontsize=9)
        ax.set_xlabel('Cantidad de usuarios')
        ax.set_title('Distribución por país')
        plt.tight_layout()
        st.pyplot(fig)
        st.caption("La distribución geográfica es muy equilibrada entre los 7 países, todos entre el 13.8% y el 14.6%. Ningún país domina la muestra, lo que permite comparaciones sin sesgo de representación.")

    with col2:
        st.markdown("#### Distribución de planes de suscripción")
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.countplot(data=df, x='subscription_plan', hue='subscription_plan',
                      legend=False, palette='Blues_d',
                      order=df['subscription_plan'].value_counts().index, ax=ax)
        ax.set_xlabel('Plan de suscripción')
        ax.set_ylabel('Cantidad de usuarios')
        ax.set_title('Distribución por plan')
        plt.tight_layout()
        st.pyplot(fig)
        st.caption("El plan Básico concentra el 45% de los usuarios, seguido por Estándar (35%) y Premium (20%). Esta distribución es consistente en todos los países analizados.")

    # ---- BLOQUE 2: ANÁLISIS BIVARIADO ----
    st.markdown("## 2. Análisis Bivariado")
    col3, col4 = st.columns(2)

    with col3:
        st.markdown("#### Planes de suscripción por país (%)")
        tabla = df.groupby(['country', 'subscription_plan']).size().unstack(fill_value=0)
        tabla_pct = tabla.div(tabla.sum(axis=1), axis=0).mul(100)
        fig, ax = plt.subplots(figsize=(6, 4))
        tabla_pct.plot(kind='bar', stacked=True, colormap='Blues', ax=ax)
        ax.set_xlabel('País')
        ax.set_ylabel('Porcentaje de usuarios (%)')
        ax.set_title('Planes por país')
        ax.legend(title='Plan', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig)
        st.caption("La distribución de planes es homogénea entre los 7 países. El plan Básico domina en todos los mercados, lo que sugiere que la preferencia por el plan más económico no depende del país de origen.")

    with col4:
        st.markdown("#### Consumo mensual según tickets de soporte")
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.boxplot(data=df, x='customer_support_tickets',
                    y='monthly_watch_time_mins', color='steelblue', ax=ax)
        ax.set_xlabel('Cantidad de tickets')
        ax.set_ylabel('Minutos por mes')
        ax.set_title('Consumo vs tickets de soporte')
        plt.tight_layout()
        st.pyplot(fig)
        st.caption("Las medianas de consumo mensual son similares entre los distintos niveles de tickets. Esto confirma que abrir más tickets no está asociado a un mayor o menor consumo de contenido.")

    # ---- BLOQUE 3: ANÁLISIS MULTIVARIADO ----
    st.markdown("## 3. Análisis Multivariado")
    st.markdown("#### Matriz de correlación entre variables numéricas")
    correlacion = df[['age', 'monthly_watch_time_mins', 'customer_support_tickets']].corr()
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.heatmap(correlacion, annot=True, fmt='.2f', cmap='Blues',
                linewidths=0.5, square=True, ax=ax)
    ax.set_title('Matriz de correlación entre variables numéricas')
    plt.tight_layout()
    st.pyplot(fig)
    st.caption("Las tres variables numéricas son prácticamente independientes entre sí. Ninguna correlación supera el 0.02 en valor absoluto, lo que indica que la edad, el consumo y los tickets no se explican mutuamente.")

except FileNotFoundError:
    st.error("No se encontró el archivo 'streaming_users_clean.csv' en 'data/processed/'.")
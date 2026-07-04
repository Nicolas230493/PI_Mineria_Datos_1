import streamlit as st

st.set_page_config(page_title="Conclusiones - PI Minería de Datos I", page_icon="🏁", layout="wide")

st.title("Conclusiones del Proyecto")

st.markdown("### Respuestas a las preguntas de análisis")

st.markdown("""
**1. ¿El plan de suscripción cambia según el país o la edad?**

No. La distribución de planes es similar en todos los países y rangos etarios. El plan Básico concentra el 45% de los usuarios en todos los segmentos, lo que sugiere que el precio es el principal factor de decisión independientemente del origen geográfico o la edad.

**2. ¿Los usuarios que más consumen son los que abren más tickets?**

No. El heatmap de correlación mostró una correlación de -0.01 entre minutos de consumo mensual y tickets de soporte. Consumir más contenido no implica abrir más tickets de soporte técnico.

**3. ¿Hay géneros que predominen según el rango de edad?**

No. La distribución de géneros es homogénea entre los rangos etarios. Las medianas de edad se mantienen entre los 30 y 40 años para todos los géneros, sin que ninguno esté asociado a un rango etario particular.

**4. ¿Los nulos en tiempo de visualización se concentran en algún plan?**

No. El análisis MCAR/MAR/MNAR mostró que los nulos en monthly_watch_time_mins son MAR — dependen del plan Premium — pero se distribuyeron de forma proporcional sin concentración extrema en ningún plan.
""")

st.markdown("### Hallazgos generales")
st.markdown("""
- El dataset representa una base de usuarios latinoamericanos equilibrada entre 7 países y 3 planes de suscripción.
- Las variables numéricas no presentan correlaciones significativas entre sí.
- El perfil típico del usuario es adulto de 35 años, con un consumo mensual de alrededor de 750 minutos y entre 0 y 1 tickets de soporte.
- El PCA requiere 13 componentes para explicar el 80% de la varianza, lo que confirma la baja correlación entre variables.
""")

st.markdown("### Limitaciones")
st.warning("""
- El dataset requirió imputación significativa en varias columnas. Las imputaciones con mediana en age y con 0 en monthly_watch_time_mins pueden haber suavizado distribuciones reales.
- Los nulos en monthly_watch_time_mins son MAR (dependen del plan Premium), lo que introduce un sesgo leve en la imputación global aplicada.
- La columna last_login_date fue imputada con la fecha mediana (2022-02-15), por lo que no refleja comportamiento real del usuario en esos registros.
- El alcance de las conclusiones está condicionado por la información disponible y las decisiones documentadas durante el proceso.
""")

st.markdown("### Próximos pasos")
st.info("""
- Aplicar técnicas de clustering (K-Means o DBSCAN) para identificar segmentos de usuarios con comportamientos similares.
- Incorporar variables adicionales de comportamiento para enriquecer el análisis y mejorar la eficiencia del PCA.
- Explorar modelos predictivos para anticipar cancelaciones o migraciones de plan.
- Revisar la imputación de monthly_watch_time_mins usando mediana por grupo en lugar de imputación global para reducir el sesgo MAR identificado.
""")
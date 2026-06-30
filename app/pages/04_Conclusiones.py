import streamlit as st

st.set_page_config(page_title="Conclusiones - PI Minería de Datos I", page_icon="🏁", layout="wide")

st.title("🏁 Síntesis y Conclusiones del Proyecto")

st.markdown("### ❓ Respuestas a las Preguntas de Análisis Iniciales")

st.markdown("""
1. **¿El plan cambia según el país o la edad?**
   *No. La distribución comercial se presenta de forma análoga en las 7 regiones latinoamericanas, consolidando una adopción homogénea sin importar rangos etarios.*
2. **¿Los usuarios que más consumen abren más tickets?**
   *No. El coeficiente asociativo lineal nulo (-0.01) confirma que el volumen de quejas técnicas no condiciona el consumo mensual de reproducción.*
3. **¿Hay algún género que predomine según el rango de edad?**
   *No. Los diagramas multivariados ratificaron que las medianas de edad se estabilizan uniformemente entre los 30 y 40 años para todas las preferencias de contenido.*
4. **¿Los valores nulos en tiempo de consumo se concentran en algún plan?**
   *Negativo. El proceso de curación evidenció una dispersión equitativa y aleatoria de los valores ausentes entre todos los segmentos comerciales.*
""")

st.markdown("### ⚠️ Limitaciones Estructurales")
st.warning(
    "El alcance analítico de las conclusiones se halla condicionado estrictamente por la granularidad y la naturaleza de "
    "las variables provistas en el dataset ruidoso original, absteniéndose de realizar inferencias fuera de los límites auditados."
)

st.markdown("### 🚀 Próximos Pasos de Expansión")
st.info(
    "Dado que las variables demográficas y comerciales presentan nula correlación lineal latente (lo que restringió la eficiencia compactadora de PCA), "
    "una línea de mejora futura consistirá en el despliegue de modelos de clustering no supervisados (como K-Means) o modelos basados en árboles "
    "de decisión para segmentar el comportamiento del usuario mediante interacciones no lineales."
)
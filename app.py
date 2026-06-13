import streamlit as np  # Usamos la estructura clásica de Streamlit
import streamlit as st
import random

# Configuración de la página
st.set_page_config(page_title="El Juego de los Valores", page_icon="✨", layout="centered")

# Título principal de la app
st.title("✨ El Juego de los Valores")
st.write("Bienvenido a esta primera versión de prueba. Explora, reflexiona y selecciona los valores que resuenen contigo hoy.")

# 1. Base de datos de prueba (Insumos temporales)
valores_dict = {
    "Empatía": "La capacidad de comprender y compartir los sentimientos de los demás, regulando nuestra respuesta desde la compasión.",
    "Autenticidad": "Ser fiel a tu propia voz, tus principios y tu historia, sin máscaras.",
    "Resiliencia": "La flexibilidad del ser para adaptarse positivamente a situaciones adversas y salir fortalecido.",
    "Colaboración": "El arte de sumar saberes y energías con otros para alcanzar un propósito común.",
    "Balance": "Mantener la armonía entre tu energía, tus responsabilidades y el cuidado de tu propio ser."
}

# 2. Dinámica 1: El Valor del Día (Aleatorio)
st.subheader("🎲 Tu Valor Guía")
st.write("Haz clic abajo para recibir un valor al azar sobre el cual reflexionar hoy.")

if st.button("Descubrir Valor"):
    valor_azar, descripcion_azar = random.choice(list(valores_dict.items()))
    st.info(f"**{valor_azar}**: {descripcion_azar}")

st.markdown("---")

# 3. Dinámica 2: Selector y Filtro de Valores
st.subheader("🔍 Explora la lista completa")

# Selector múltiple para que el usuario interactúe
valores_seleccionados = st.multiselect(
    "Selecciona los valores que consideras prioritarios en este momento:",
    options=list(valores_dict.keys()),
    default=["Empatía"]
)

# Mostrar las tarjetas de los valores seleccionados
if valores_seleccionados:
    st.write("### Tus valores seleccionados:")
    for v in valores_seleccionados:
        with st.expander(f"🔹 {v}", expanded=True):
            st.write(valores_dict[v])
else:
    st.warning("Por favor, selecciona al menos un valor de la lista.")
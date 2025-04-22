import streamlit as st

# Constante de los gases ideales
R = 0.0821  # atm·L/(mol·K)

st.set_page_config(page_title="Calculadora de Gases Ideales", layout="centered")
st.title("🔬 Calculadora de la Ecuación de los Gases Ideales")
st.markdown("**Fórmula:** PV = nRT")

# Elección de la variable a calcular
opcion = st.selectbox("Selecciona la variable que deseas calcular:", [
    "Presión (P)",
    "Volumen (V)",
    "Temperatura (T)",
    "Número de moles (n)"
])

# Lógica para cada cálculo
if opcion == "Presión (P)":
    V = st.number_input("Volumen (L)", min_value=0.001)
    T = st.number_input("Temperatura (K)", min_value=0.001)
    n = st.number_input("Número de moles (mol)", min_value=0.001)
    if st.button("Calcular Presión"):
        P = (n * R * T) / V
        st.success(f"La presión es **{P:.3f} atm**")

elif opcion == "Volumen (V)":
    P = st.number_input("Presión (atm)", min_value=0.001)
    T = st.number_input("Temperatura (K)", min_value=0.001)
    n = st.number_input("Número de moles (mol)", min_value=0.001)
    if st.button("Calcular Volumen"):
        V = (n * R * T) / P
        st.success(f"El volumen es **{V:.3f} L**")

elif opcion == "Temperatura (T)":
    P = st.number_input("Presión (atm)", min_value=0.001)
    V = st.number_input("Volumen (L)", min_value=0.001)
    n = st.number_input("Número de moles (mol)", min_value=0.001)
    if st.button("Calcular Temperatura"):
        T = (P * V) / (n * R)
        st.success(f"La temperatura es **{T:.3f} K**")

elif opcion == "Número de moles (n)":
    P = st.number_input("Presión (atm)", min_value=0.001)
    V = st.number_input("Volumen (L)", min_value=0.001)
    T = st.number_input("Temperatura (K)", min_value=0.001)
    if st.button("Calcular Número de moles"):
        n = (P * V) / (R * T)
        st.success(f"El número de moles es **{n:.3f} mol**")

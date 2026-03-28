import streamlit as st
import matplotlib.pyplot as plt
from main import analizar_experimento

st.set_page_config(layout="wide")

st.title("Superconductor Analysis Dashboard")

# ================= SELECTORES =================

expIDs = ['01968','01966','01964','01962','01970','01972']

col1, col2 = st.columns(2)

with col1:
    modelo = st.selectbox("Modelo", ["gauss", "lorentz"])

with col2:
    exp = st.selectbox("Experimento", expIDs)

# ================= ANÁLISIS =================

try:
    data = analizar_experimento(exp, modelo)

    # ================= GRÁFICA =================
    fig, ax = plt.subplots(figsize=(8,5))

    ax.scatter(
        data["T"], data["dVdT"],
        color=(0.2,0.6,0.2),
        edgecolors='black',
        label="Datos"
    )

    ax.plot(data["fitX"], data["c1"], '--',
            color=(0.1,0.6,1.0), label='Componente 1')

    ax.plot(data["fitX"], data["c2"], '--',
            color=(1.0,0.6,0.0), label='Componente 2')

    ax.plot(data["fitX"], data["cT"], '-',
            color=(0.8,0.2,0.2), label='Suma')

    ax.set_xlabel("Temperatura (K)")
    ax.set_ylabel("dV/dT (µV/K)")
    ax.set_title(f'I = {data["I"]:.2f} mA | Exp {exp}')
    ax.grid()
    ax.legend()

    st.pyplot(fig)

    # ================= PARÁMETROS =================

    st.subheader("Parámetros del ajuste")

    A1,x1,s1,A2,x2,s2 = data["params"]

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Centro 1 (K)", f"{x1:.3f}")
        st.metric("Sigma 1", f"{s1:.3f}")

    with col2:
        st.metric("Centro 2 (K)", f"{x2:.3f}")
        st.metric("Sigma 2", f"{s2:.3f}")

except Exception as e:
    st.error(f"Error en el análisis: {e}")
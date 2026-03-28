import streamlit as st
import matplotlib.pyplot as plt
from main import analizar_experimento, analizar_todos

st.set_page_config(layout="wide")

st.title("Superconductor Analysis Dashboard")

expIDs = ['01968','01966','01964','01962','01970','01972']

# ================= SELECTORES =================

col1, col2 = st.columns(2)

with col1:
    modelo = st.selectbox("Modelo", ["gauss", "lorentz"])

with col2:
    exp = st.selectbox("Experimento", expIDs)

# ================= GRÁFICA INDIVIDUAL =================

st.header("🔬 Ajuste por experimento")

try:
    data = analizar_experimento(exp, modelo)

    fig, ax = plt.subplots(figsize=(8,5))

    ax.scatter(data["T"], data["dVdT"],
               color=(0.2,0.6,0.2),
               edgecolors='black',
               label="Datos")

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

    # Parámetros
    st.subheader("Parámetros del ajuste")

    A1,x1,s1,A2,x2,s2 = data["params"]

    c1, c2 = st.columns(2)

    with c1:
        st.metric("Centro 1 (K)", f"{x1:.3f}")
        st.metric("Sigma 1", f"{s1:.3f}")

    with c2:
        st.metric("Centro 2 (K)", f"{x2:.3f}")
        st.metric("Sigma 2", f"{s2:.3f}")

except Exception as e:
    st.error(f"Error en el análisis: {e}")

# ================= ANÁLISIS GLOBAL =================

st.divider()
st.header("📊 Análisis global")

df = analizar_todos(expIDs, modelo)

# 🔵 Componente 1
fig1, ax1 = plt.subplots()

ax1.plot(df["I"], df["Centro1"], 'o-',
         color=(0.1,0.6,1.0),
         markeredgecolor='black')

ax1.set_xlabel("Corriente (mA)")
ax1.set_ylabel("Centro (K)")
ax1.set_title("Componente 1")
ax1.grid()

st.pyplot(fig1)

# 🟠 Componente 2
fig2, ax2 = plt.subplots()

ax2.plot(df["I"], df["Centro2"], 'o-',
         color=(1.0,0.6,0.0),
         markeredgecolor='black')

ax2.set_xlabel("Corriente (mA)")
ax2.set_ylabel("Centro (K)")
ax2.set_title("Componente 2")
ax2.grid()

st.pyplot(fig2)

# 🔥 Comparación Tc con errores
fig3, ax3 = plt.subplots()

ax3.errorbar(df["I"], df["Centro1"],
             yerr=df["Error1"],
             fmt='o',
             color=(0.1,0.6,1.0),
             label='Comp 1')

ax3.errorbar(df["I"], df["Centro2"],
             yerr=df["Error2"],
             fmt='o',
             color=(1.0,0.6,0.0),
             label='Comp 2')

ax3.set_xlabel("Corriente (mA)")
ax3.set_ylabel("Temperatura crítica (K)")
ax3.set_title("Comparación Tc")
ax3.legend()
ax3.grid()

st.pyplot(fig3)
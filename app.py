import streamlit as st
import matplotlib.pyplot as plt
from main import analizar_experimento, analizar_todos

st.set_page_config(layout="wide")

st.title("Superconductor Analysis Dashboard")

expIDs = ['01968', '01966', '01964', '01962', '01970', '01972']

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

    # 🔥 columnas para centrar
    left, center, right = st.columns([1, 2, 1])

    fig, ax = plt.subplots(figsize=(3.2, 1.6))

    ax.scatter(
        data["T"], data["dVdT"],
        color=(0.2, 0.6, 0.2),
        edgecolors="black",
        s=18,
        label="Datos"
    )

    ax.plot(
        data["fitX"], data["c1"], "--",
        color=(0.1, 0.6, 1.0),
        linewidth=1.5,
        label="Componente 1"
    )

    ax.plot(
        data["fitX"], data["c2"], "--",
        color=(1.0, 0.6, 0.0),
        linewidth=1.5,
        label="Componente 2"
    )

    ax.plot(
        data["fitX"], data["cT"], "-",
        color=(0.8, 0.2, 0.2),
        linewidth=1.5,
        label="Suma"
    )

    ax.set_xlabel("Temperatura (K)", fontsize=8)
    ax.set_ylabel("dV/dT (µV/K)", fontsize=8)

    ax.set_title(
        f"I = {data['I']:.2f} mA | Exp {exp}",
        fontsize=9
    )

    ax.tick_params(axis="both", labelsize=7)

    ax.grid(True)

    ax.legend(fontsize=7)

    # 🔥 gráfica centrada
    with center:
        st.pyplot(fig, use_container_width=False)

    # ================= PARÁMETROS =================

    st.subheader("Parámetros del ajuste")

    A1, x1, s1, A2, x2, s2 = data["params"]

    m1, m2, m3, m4 = st.columns(4)

    with m1:
        st.metric("Centro 1 (K)", f"{x1:.3f}")

    with m2:
        st.metric("Sigma 1", f"{s1:.3f}")

    with m3:
        st.metric("Centro 2 (K)", f"{x2:.3f}")

    with m4:
        st.metric("Sigma 2", f"{s2:.3f}")

except Exception as e:
    st.error(f"Error en el análisis: {e}")

# ================= ANÁLISIS GLOBAL =================

st.divider()

st.header("📊 Análisis global")

df = analizar_todos(expIDs, modelo)

g1, g2, g3 = st.columns(3)

# ================= COMPONENTE 1 =================

fig1, ax1 = plt.subplots(figsize=(3.6, 2.5))

ax1.plot(
    df["I"], df["Centro1"], "o-",
    color=(0.1, 0.6, 1.0),
    markeredgecolor="black",
    linewidth=1.5,
    markersize=4
)

ax1.set_xlabel("Corriente (mA)", fontsize=8)
ax1.set_ylabel("Centro (K)", fontsize=8)

ax1.set_title("Componente 1", fontsize=9)

ax1.tick_params(axis="both", labelsize=7)

ax1.grid(True)

with g1:
    st.pyplot(fig1, use_container_width=False)

# ================= COMPONENTE 2 =================

fig2, ax2 = plt.subplots(figsize=(3.6, 2.5))

ax2.plot(
    df["I"], df["Centro2"], "o-",
    color=(1.0, 0.6, 0.0),
    markeredgecolor="black",
    linewidth=1.5,
    markersize=4
)

ax2.set_xlabel("Corriente (mA)", fontsize=8)
ax2.set_ylabel("Centro (K)", fontsize=8)

ax2.set_title("Componente 2", fontsize=9)

ax2.tick_params(axis="both", labelsize=7)

ax2.grid(True)

with g2:
    st.pyplot(fig2, use_container_width=False)

# ================= COMPARACIÓN Tc =================

fig3, ax3 = plt.subplots(figsize=(3.6, 2.5))

ax3.errorbar(
    df["I"], df["Centro1"],
    yerr=df["Error1"],
    fmt="o-",
    color=(0.1, 0.6, 1.0),
    linewidth=1.5,
    markersize=4,
    label="Comp 1"
)

ax3.errorbar(
    df["I"], df["Centro2"],
    yerr=df["Error2"],
    fmt="o-",
    color=(1.0, 0.6, 0.0),
    linewidth=1.5,
    markersize=4,
    label="Comp 2"
)

ax3.set_xlabel("Corriente (mA)", fontsize=8)
ax3.set_ylabel("Tc (K)", fontsize=8)

ax3.set_title("Comparación Tc", fontsize=9)

ax3.tick_params(axis="both", labelsize=7)

ax3.legend(fontsize=7)

ax3.grid(True)

with g3:
    st.pyplot(fig3, use_container_width=False)
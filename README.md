# Superconductor Data Analysis Dashboard

Interactive scientific dashboard for superconducting experimental data analysis using Python, numerical methods, and curve fitting.

This project processes real superconducting transition measurements, applies double Gaussian and Lorentzian fitting models, and visualizes the results through an interactive Streamlit dashboard.

---

## Features

- Reads experimental `.Cn1` and `.Cn2` measurement files
- Computes average voltage and temperature
- Calculates numerical derivatives (`dV/dT`)
- Applies:
  - Double Gaussian fitting
  - Double Lorentzian fitting
- Interactive experiment selection
- Global Tc vs current analysis
- Error visualization
- Automatic scientific plotting

---

## Dashboard Preview

### Experiment Analysis

![Experiment Analysis](screenshots/experiment-analysis.png)

The dashboard allows interactive visualization of the superconducting transition for each experiment, including:
- Raw experimental points
- Individual fitted components
- Total fitted curve
- Extracted fitting parameters

---

### Global Tc Analysis

![Global Tc Analysis](screenshots/global-tc-analysis.png)

Global analysis compares the evolution of the fitted critical temperatures as a function of applied current.

---

## Scientific Context

Unlike typical software portfolio projects, this repository focuses on scientific data analysis using real experimental measurements.

The workflow combines:

- Scientific computing
- Numerical analysis
- Curve fitting
- Data visualization
- Interactive dashboards
- Experimental physics

This project was developed as part of superconductivity data analysis research workflows.

---

## Technologies Used

- Python
- NumPy
- Pandas
- SciPy
- Matplotlib
- Streamlit

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/Axahdz/superconductor-data-analysis-dashboard.git
cd superconductor-data-analysis-dashboard
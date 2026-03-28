\# Superconductor Data Analysis Dashboard



This project was developed to analyze experimental superconducting data and visualize the results in an interactive way.



It takes raw measurement files, processes the data, computes numerical derivatives, and applies curve fitting using both Gaussian and Lorentzian models. The results can be explored through a simple dashboard built with Streamlit.



\---



\## What this project does



\* Reads experimental data from `.Cn1` and `.Cn2` files

\* Computes the average voltage and temperature

\* Calculates the numerical derivative (dV/dT)

\* Applies double Gaussian and Lorentzian fits

\* Displays results interactively per experiment

\* Generates global comparisons such as Tc vs current



\---



\## Why this project is different



This is not a typical CRUD or tutorial project.



The data comes from real experimental measurements, and the analysis involves numerical methods, curve fitting, and interpretation of physical behavior.



It combines:



\* Scientific computing

\* Data analysis

\* Software development



All in a single workflow.



\---



\## Technologies used



\* Python

\* NumPy

\* Pandas

\* SciPy

\* Matplotlib

\* Streamlit



\---



\## How to run



Clone the repository and install dependencies:



```bash

pip install -r requirements.txt

```



Then run:



```bash

python -m streamlit run app.py

```



The dashboard will open in your browser.



\---



\## Project structure



```text

app.py          # Dashboard

analysis.py     # Data processing and fitting logic

Run0\_\*.Cn1      # Experimental data (Va)

Run0\_\*.Cn2      # Experimental data (Vb)

```



\---



\## Notes



The analysis focuses on the temperature range where the superconducting transition occurs, and uses numerical derivatives to highlight the transition behavior.



\---



\## Author



Javier Axayácatl Melchor Hernández



Background in Physics with experience in software development and data analysis.




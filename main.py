import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import os

ruta = os.getcwd()

# ================= CARGA DE DATOS =================

def cargar_datos(ruta, id):
    fVA = os.path.join(ruta, f'Run0_{id}.Cn1')
    fVB = os.path.join(ruta, f'Run0_{id}.Cn2')

    cols = ['Tiempo','T','I','V','Err','Cfg']

    Tva = pd.read_csv(fVA, names=cols)
    Tvb = pd.read_csv(fVB, names=cols)

    Vprom = 0.5 * (Tva['V'] - Tvb['V']) * 1e6
    Temp = 0.5 * (Tva['T'] + Tvb['T'])

    I = Tva['I'].iloc[0] * 1e3

    mask = (Temp >= 80) & (Temp <= 100)

    Temp = Temp[mask].values
    Vprom = Vprom[mask].values

    dVdT = np.gradient(Vprom) / np.gradient(Temp)

    return Temp, dVdT, I

# ================= MODELOS =================

def lorentz(x, A, x0, s):
    return A*(0.5*s)/((x-x0)**2 + (0.5*s)**2)

def doble_lorentz(x, A1,x1,s1,A2,x2,s2):
    return lorentz(x,A1,x1,s1) + lorentz(x,A2,x2,s2)

def gauss(x, A, x0, s):
    return A*np.exp(-((x-x0)**2)/(2*s**2))

def doble_gauss(x, A1,x1,s1,A2,x2,s2):
    return gauss(x,A1,x1,s1) + gauss(x,A2,x2,s2)

# ================= ANÁLISIS INDIVIDUAL =================

def analizar_experimento(id, modelo="gauss"):

    T, dVdT, I = cargar_datos(ruta, id)

    Amax = np.max(dVdT)
    x_est = T[np.argmax(dVdT)]

    func = doble_gauss if modelo == "gauss" else doble_lorentz

    popt, _ = curve_fit(
        func,
        T,
        dVdT,
        p0=[Amax*0.2, x_est-1, 0.3,
            Amax*0.8, x_est, 0.5],
        maxfev=10000
    )

    A1,x1,s1,A2,x2,s2 = popt

    fitX = np.linspace(min(T), max(T), 800)

    if modelo == "gauss":
        c1 = gauss(fitX, A1,x1,s1)
        c2 = gauss(fitX, A2,x2,s2)
    else:
        c1 = lorentz(fitX, A1,x1,s1)
        c2 = lorentz(fitX, A2,x2,s2)

    cT = c1 + c2

    return {
        "T": T,
        "dVdT": dVdT,
        "fitX": fitX,
        "c1": c1,
        "c2": c2,
        "cT": cT,
        "I": I,
        "params": (A1,x1,s1,A2,x2,s2)
    }

# ================= ANÁLISIS GLOBAL =================

def analizar_todos(expIDs, modelo="gauss"):

    resultados = []

    for id in expIDs:

        try:
            data = analizar_experimento(id, modelo)

            A1,x1,s1,A2,x2,s2 = data["params"]

            resultados.append({
                "Exp": id,
                "I": data["I"],
                "Centro1": x1,
                "Centro2": x2,
                "Error1": s1/2,
                "Error2": s2/2
            })

        except:
            pass

    df = pd.DataFrame(resultados)

    df = df.sort_values(by="I")

    return df
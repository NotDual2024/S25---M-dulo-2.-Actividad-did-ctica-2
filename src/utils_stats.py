"""Resumen estadistico: media, desviacion estandar e IC95 % con t de Student."""
import numpy as np

# Cuantil t_{0.975, gl}. Valor de tabla para gl = 99 (R = 100 replicas).
# Se usa una tabla en lugar de scipy para no anadir dependencias.
T_975 = {99: 1.984217}


def resumen(x):
    x = np.asarray(x, dtype=float)
    n = len(x)
    if n - 1 not in T_975:
        raise ValueError(f"Falta t_0.975 para gl = {n - 1}; anadirlo a T_975.")
    media, sd = x.mean(), x.std(ddof=1)
    h = T_975[n - 1] * sd / np.sqrt(n)
    return {"media": media, "sd": sd, "min": x.min(), "max": x.max(),
            "ic_inf": media - h, "ic_sup": media + h, "n": n}

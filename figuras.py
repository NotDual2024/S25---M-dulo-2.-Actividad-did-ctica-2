"""Figura de D (Viterbi - referencia) y D_post (posterior - referencia) con IC95 %
frente a eta (E2) y kappa (E3).

Lee results/resumen.csv; no simula nada. Uso: python figuras.py
"""
import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

OUT = Path(__file__).parent / "results"
res = list(csv.DictReader(open(OUT / "resumen.csv")))
SERIES = [("D", "Viterbi - referencia", "#1f4e79", "o-"),
          ("D_post", "Posterior - referencia", "#c55a11", "s--")]

fig, ejes = plt.subplots(1, 2, figsize=(9, 3.6), sharey=True)
for eje, esc, sim in ((ejes[0], "E2", r"$\eta$"), (ejes[1], "E3", r"$\kappa$")):
    for var, etiqueta, color, estilo in SERIES:
        filas = [f for f in res if f["variable"] == var]
        sub = [next(f for f in filas if f["escenario"] == "E1")] + \
              [f for f in filas if f["escenario"] == esc]
        x = [0.0] + [float(f["nivel"]) for f in sub[1:]]
        med = [float(f["media"]) for f in sub]
        lo = [float(f["media"]) - float(f["ic95_inf"]) for f in sub]
        hi = [float(f["ic95_sup"]) - float(f["media"]) for f in sub]
        eje.errorbar(x, med, yerr=[lo, hi], fmt=estilo, capsize=3, color=color, label=etiqueta)
    eje.axhline(0, color="gray", lw=0.8, ls=":")
    eje.set_xlabel(sim)
    eje.set_title(esc + (" (B mas ambigua)" if esc == "E2" else " (A menos persistente)"))
ejes[0].set_ylabel("Diferencia de exactitud por paso")
ejes[0].legend(fontsize=8, loc="lower right")
fig.suptitle("Media con IC95 % (R = 100 replicas); el nivel 0 es E1", fontsize=10)
fig.tight_layout()
fig.savefig(OUT / "fig_D.pdf")
fig.savefig(OUT / "fig_D.png", dpi=150)
print("Figura guardada en results/fig_D.pdf y .png")

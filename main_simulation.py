"""Experimento E1-E3 (decisiones D1, D2, D6, D7, D9, D10).

Para cada replica r (semilla propia, compartida entre configuraciones) y cada
configuracion, se simulan S secuencias de T acciones, se decodifican con
Viterbi y con el clasificador de referencia usando los parametros verdaderos,
y se calcula la exactitud por paso y por fase.

Uso:  python main_simulation.py
Salidas en results/.
"""
import csv
import platform
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent / "src"))
from hmm_core import viterbi_log, clasificador_ref, posterior_decode, simular  # noqa: E402
from utils_stats import resumen  # noqa: E402

# ---- Parametros del caso (hipoteticos, no estimados de partidos reales) ----
A = np.array([[0.60, 0.30, 0.10], [0.30, 0.40, 0.30], [0.20, 0.30, 0.50]])
B = np.array([[0.70, 0.25, 0.05], [0.40, 0.50, 0.10], [0.30, 0.30, 0.40]])
PI = np.array([0.40, 0.40, 0.20])
U = np.full((3, 3), 1 / 3)

# ---- Diseno (D6, D7) ----
T, S, R = 100, 50, 100
SEMILLA_RAIZ = 20261109
FASES = ["defensiva", "transicion", "ataque"]
METODOS = ["vit", "ref", "post"]   # Viterbi, referencia, decodificacion posterior (D10)

CONFIGS = [("E1", "-", 0.0, A, B)]
for eta in (0.25, 0.5, 0.75, 1.0):
    CONFIGS.append(("E2", "eta", eta, A, (1 - eta) * B + eta * U))
for kappa in (0.25, 0.5, 0.75, 1.0):
    CONFIGS.append(("E3", "kappa", kappa, (1 - kappa) * A + kappa * U, B))

OUT = Path(__file__).parent / "results"
OUT.mkdir(exist_ok=True)


def main():
    t0 = time.time()
    semillas = np.random.SeedSequence(SEMILLA_RAIZ).spawn(R)
    filas_rep = []                      # una fila por (configuracion, replica)
    conf_E1 = {m: np.zeros((3, 3), int) for m in METODOS}

    for esc, par, nivel, Ac, Bc in CONFIGS:
        for c in (Ac, Bc):
            assert np.allclose(c.sum(axis=1), 1)
        for r in range(R):
            rng = np.random.default_rng(semillas[r])   # misma semilla en todos los niveles
            ac = {m: np.zeros(3) for m in METODOS}
            n_f = np.zeros(3)
            for _ in range(S):
                s, o = simular(T, Ac, Bc, PI, rng)
                q = {"vit": viterbi_log(o, Ac, Bc, PI)[0],   # los metodos solo ven o
                     "ref": clasificador_ref(o, Ac, Bc),
                     "post": posterior_decode(o, Ac, Bc, PI)}
                for f in range(3):
                    msk = s == f
                    n_f[f] += msk.sum()
                    for m in METODOS:
                        ac[m][f] += (q[m][msk] == f).sum()
                if esc == "E1":
                    for m in METODOS:
                        np.add.at(conf_E1[m], (s, q[m]), 1)
            acc = {m: ac[m].sum() / (S * T) for m in METODOS}
            fila = {"escenario": esc, "parametro": par, "nivel": nivel, "replica": r,
                    "acc_vit": acc["vit"], "acc_ref": acc["ref"], "acc_post": acc["post"],
                    "D": acc["vit"] - acc["ref"],             # variable principal (P1-P3)
                    "D_post": acc["post"] - acc["ref"]}       # variable secundaria (D10)
            for f, nom in enumerate(FASES):
                fila[f"n_{nom}"] = int(n_f[f])
                for m in METODOS:
                    fila[f"rec_{m}_{nom}"] = ac[m][f] / n_f[f] if n_f[f] else float("nan")
            filas_rep.append(fila)
        print(f"{esc} {par}={nivel}: listo ({time.time() - t0:.0f} s)", flush=True)

    # ---- Exportacion ----
    with open(OUT / "replicas.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(filas_rep[0]))
        w.writeheader(); w.writerows(filas_rep)

    with open(OUT / "resumen.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["escenario", "parametro", "nivel", "variable",
                    "media", "sd", "min", "max", "ic95_inf", "ic95_sup", "R"])
        for esc, par, nivel, _, _ in CONFIGS:
            sub = [f for f in filas_rep if f["escenario"] == esc and f["nivel"] == nivel]
            vars_ = (["acc_vit", "acc_ref", "acc_post", "D", "D_post"] +
                     [f"rec_{m}_{n}" for m in METODOS for n in FASES])
            for v in vars_:
                x = [f[v] for f in sub]
                if np.isnan(x).any():
                    continue
                rs = resumen(x)
                w.writerow([esc, par, nivel, v, rs["media"], rs["sd"], rs["min"], rs["max"],
                            rs["ic_inf"], rs["ic_sup"], rs["n"]])

    with open(OUT / "confusion_E1.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["metodo", "fase_verdadera"] + [f"pred_{n}" for n in FASES])
        for met in METODOS:
            for f, nom in enumerate(FASES):
                w.writerow([met, nom] + list(conf_E1[met][f]))

    with open(OUT / "entorno.txt", "w") as fh:
        fh.write(f"python {platform.python_version()}\nnumpy {np.__version__}\n"
                 f"plataforma {platform.platform()}\nsemilla_raiz {SEMILLA_RAIZ}\n"
                 f"T={T} S={S} R={R}\nduracion_s {time.time() - t0:.1f}\n")
    print(f"Terminado en {time.time() - t0:.0f} s")


if __name__ == "__main__":
    main()

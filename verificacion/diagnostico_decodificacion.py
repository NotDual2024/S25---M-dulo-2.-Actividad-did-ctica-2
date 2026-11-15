"""Diagnostico (no forma parte del diseno aprobado; sirve para descartar errores).

1. Exactitud esperada del clasificador de referencia, calculada analiticamente.
2. Viterbi frente a busqueda exhaustiva en secuencias simuladas con E1 (T = 8).
3. Decodificacion posterior (forward-backward): maximiza la exactitud esperada
   por paso. Si supera al clasificador de referencia mientras Viterbi no lo hace,
   el resultado de Viterbi es una propiedad del criterio (camino conjunto) y no
   un error de implementacion.
Usa semillas distintas de las del experimento.
"""
import itertools
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from hmm_core import viterbi_log, clasificador_ref, simular, estacionaria  # noqa: E402

A = np.array([[0.60, 0.30, 0.10], [0.30, 0.40, 0.30], [0.20, 0.30, 0.50]])
B = np.array([[0.70, 0.25, 0.05], [0.40, 0.50, 0.10], [0.30, 0.30, 0.40]])
PI = np.array([0.40, 0.40, 0.20])


def posterior(obs, A, B, pi):
    T, N = len(obs), len(pi)
    al = np.empty((T, N)); be = np.ones((T, N)); c = np.empty(T)
    al[0] = pi * B[:, obs[0]]; c[0] = al[0].sum(); al[0] /= c[0]
    for t in range(1, T):
        al[t] = (al[t - 1] @ A) * B[:, obs[t]]; c[t] = al[t].sum(); al[t] /= c[t]
    for t in range(T - 2, -1, -1):
        be[t] = A @ (B[:, obs[t + 1]] * be[t + 1]) / c[t + 1]
    return np.argmax(al * be, axis=1)


p = estacionaria(A)
print("1) Exactitud esperada del clasificador de referencia (sum_o max_i p_i b_i(o)):",
      round(float((p[:, None] * B).max(axis=0).sum()), 4))

rng = np.random.default_rng(777)
ok = 0
for _ in range(100):
    s, o = simular(8, A, B, PI, rng)
    q, lp = viterbi_log(o, A, B, PI)
    best = max(np.log(PI[c[0]]) + np.log(B[c[0], o[0]]) +
               sum(np.log(A[c[t - 1], c[t]]) + np.log(B[c[t], o[t]]) for t in range(1, 8))
               for c in itertools.product(range(3), repeat=8))
    ok += np.isclose(lp, best)
print(f"2) Viterbi = busqueda exhaustiva en {ok}/100 secuencias simuladas (E1, T = 8)")

rng = np.random.default_rng(888)
acc = {"viterbi": [], "posterior": [], "referencia": []}
for _ in range(2000):
    s, o = simular(100, A, B, PI, rng)
    acc["viterbi"].append((viterbi_log(o, A, B, PI)[0] == s).mean())
    acc["posterior"].append((posterior(o, A, B, PI) == s).mean())
    acc["referencia"].append((clasificador_ref(o, A, B) == s).mean())
print("3) Exactitud media por paso en 2000 secuencias de E1 (T = 100):")
for k, v in acc.items():
    v = np.array(v)
    print(f"   {k:10s} {v.mean():.4f}  (error estandar {v.std(ddof=1) / np.sqrt(len(v)):.4f})")

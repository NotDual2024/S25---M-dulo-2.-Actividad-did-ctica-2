"""Verifica posterior_decode contra marginales exactas por enumeracion (T <= 7)."""
import itertools
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from hmm_core import posterior_decode, simular  # noqa: E402

A = np.array([[0.60, 0.30, 0.10], [0.30, 0.40, 0.30], [0.20, 0.30, 0.50]])
B = np.array([[0.70, 0.25, 0.05], [0.40, 0.50, 0.10], [0.30, 0.30, 0.40]])
PI = np.array([0.40, 0.40, 0.20])

rng = np.random.default_rng(999)
ok = 0
for _ in range(100):
    T = int(rng.integers(1, 8))
    _, o = simular(T, A, B, PI, rng)
    marg = np.zeros((T, 3))
    for c in itertools.product(range(3), repeat=T):
        pr = PI[c[0]] * B[c[0], o[0]]
        for t in range(1, T):
            pr *= A[c[t - 1], c[t]] * B[c[t], o[t]]
        for t in range(T):
            marg[t, c[t]] += pr
    ok += np.array_equal(posterior_decode(o, A, B, PI), np.argmax(marg, axis=1))
print(f"posterior_decode = argmax de marginales exactas en {ok}/100 secuencias")

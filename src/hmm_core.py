"""Nucleo del HMM discreto: Viterbi en log-espacio, clasificador de referencia y simulador.

Codigo aceptado por el equipo (decision D9, 2026-11-13). Convenciones:
- Fases (estados): 0 = defensiva, 1 = transicion, 2 = ataque.
- Acciones (observaciones): 0 = pase corto, 1 = pase largo, 2 = tiro a puerta.
- A[i, j] = P(fase j en t | fase i en t-1); B[j, k] = P(accion k | fase j).
- Empates: np.argmax elige el menor indice.
"""
import numpy as np


def viterbi_log(obs, A, B, pi):
    """Secuencia de fases mas probable y su log-probabilidad."""
    logA, logB, logpi = np.log(A), np.log(B), np.log(pi)
    N, T = A.shape[0], len(obs)
    delta = np.empty((T, N))
    psi = np.zeros((T, N), dtype=int)
    delta[0] = logpi + logB[:, obs[0]]                  # inicializacion
    for t in range(1, T):                               # recursion
        scores = delta[t - 1][:, None] + logA           # scores[i, j]
        psi[t] = np.argmax(scores, axis=0)
        delta[t] = scores[psi[t], np.arange(N)] + logB[:, obs[t]]
    q = np.empty(T, dtype=int)                          # reconstruccion
    q[-1] = np.argmax(delta[-1])
    for t in range(T - 2, -1, -1):
        q[t] = psi[t + 1, q[t + 1]]
    return q, delta[-1].max()


def posterior_decode(obs, A, B, pi):
    """Decodificacion posterior (forward-backward escalado), decision D10.

    En cada paso elige la fase con mayor P(S_t = i | toda la secuencia O).
    Maximiza el numero esperado de pasos acertados (no la prob. del camino).
    """
    T, N = len(obs), len(pi)
    alpha = np.empty((T, N))
    beta = np.ones((T, N))
    c = np.empty(T)                                     # factores de escala
    alpha[0] = pi * B[:, obs[0]]
    c[0] = alpha[0].sum(); alpha[0] /= c[0]
    for t in range(1, T):                               # forward
        alpha[t] = (alpha[t - 1] @ A) * B[:, obs[t]]
        c[t] = alpha[t].sum(); alpha[t] /= c[t]
    for t in range(T - 2, -1, -1):                      # backward
        beta[t] = A @ (B[:, obs[t + 1]] * beta[t + 1]) / c[t + 1]
    return np.argmax(alpha * beta, axis=1)


def estacionaria(A):
    """Distribucion estacionaria p (autovector de A^T con autovalor 1)."""
    w, v = np.linalg.eig(A.T)
    p = np.real(v[:, np.argmin(abs(w - 1))])
    return p / p.sum()


def clasificador_ref(obs, A, B):
    """Asigna a cada accion la fase con mayor p_i * b_i(o), sin transiciones."""
    p = estacionaria(A)
    regla = np.argmax(p[:, None] * B, axis=0)
    return regla[np.asarray(obs)]


def simular(T, A, B, pi, rng):
    """Genera (fases verdaderas s, acciones o) de longitud T."""
    s = np.empty(T, dtype=int)
    o = np.empty(T, dtype=int)
    s[0] = rng.choice(3, p=pi)
    o[0] = rng.choice(3, p=B[s[0]])
    for t in range(1, T):
        s[t] = rng.choice(3, p=A[s[t - 1]])
        o[t] = rng.choice(3, p=B[s[t]])
    return s, o

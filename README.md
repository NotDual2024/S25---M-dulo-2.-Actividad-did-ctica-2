# Aporte de la dependencia temporal a la inferencia de fases tácticas simuladas mediante Modelos Ocultos de Markov

Trabajo del curso Simulación — Ingeniería de Software y Datos, IU Digital.

Autores: Juan Sebastian Lopez Gallo y Andres Miguel Hernandez. Docente: Julian Andres Loaiza Lopez.

Estudio de simulación con un HMM discreto de parámetros hipotéticos conocidos (3 fases tácticas, 3 tipos de acción). Compara la decodificación de Viterbi y la decodificación posterior (forward-backward) con un clasificador sin transiciones, en tres escenarios: parámetros del caso (E1), emisiones más ambiguas (E2) y transiciones menos persistentes (E3). Los resultados se limitan al modelo simulado y no permiten afirmaciones sobre partidos reales.

## Estructura

| Ruta | Contenido |
|---|---|
| `main.tex`, `main.pdf` | Manuscrito (LaTeX) y PDF compilado |
| `bitacora.md` | Decisiones del equipo y verificaciones |
| `requirements.txt` | Versiones de las bibliotecas usadas |
| `main_simulation.py` | Ejecuta E1–E3 y exporta los CSV a `results/` |
| `figuras.py` | Genera `results/fig_D.pdf` y `.png` |
| `tablas_latex.py` | Genera `results/tablas_resultados.tex` desde los CSV |
| `src/hmm_core.py` | `viterbi_log`, `posterior_decode`, `clasificador_ref`, `simular`, `estacionaria` |
| `src/utils_stats.py` | Media, desviación estándar e IC95 % |
| `verificacion/` | Comprobaciones de los decodificadores (búsqueda exhaustiva y marginales exactas) |
| `results/` | CSV, figura, tablas, entorno de ejecución y salidas de las verificaciones |
| `results/ejecucion1/` | Archivo de la primera ejecución (antes de añadir la decodificación posterior) |

## Reproducir

Entorno usado: Python 3.14.2, NumPy 2.5.3, Matplotlib 3.11.1, Windows 11 (ver `results/entorno.txt`).

```bash
pip install -r requirements.txt
python main_simulation.py
python figuras.py
python tablas_latex.py
pdflatex main.tex
pdflatex main.tex
```

Semilla raíz: `20261109` (`numpy.random.SeedSequence(20261109).spawn(100)`, una semilla por réplica compartida entre niveles).

Verificaciones opcionales:

```bash
python verificacion/diagnostico_decodificacion.py
python verificacion/test_posterior.py
```

## Fuentes

- Ötting, M., Langrock, R., Maruotti, A. (2023). A copula-based multivariate hidden Markov model for modelling momentum in football. *AStA Advances in Statistical Analysis*, 107, 9–27. https://doi.org/10.1007/s10182-021-00395-8 (CC BY 4.0).
- Fani, M., Yazdi, M., Clausi, D. A., Wong, A. (2017). Soccer video structure analysis by parallel feature fusion network and hidden-to-observable transferring Markov model. *IEEE Access*, 5, 27322–27336. https://doi.org/10.1109/ACCESS.2017.2769140 (© IEEE; se cita, no se redistribuye).

## Uso de IA

Se usó un asistente de IA (Claude, Anthropic); ver la declaración en `main.tex`.

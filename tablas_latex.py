"""Genera results/tablas_resultados.tex a partir de los CSV (sin transcribir a mano).

Uso: python tablas_latex.py
"""
import csv
from pathlib import Path

OUT = Path(__file__).parent / "results"
res = list(csv.DictReader(open(OUT / "resumen.csv")))
FASES = ["defensiva", "transicion", "ataque"]
METODOS = [("vit", "Viterbi"), ("post", "Posterior"), ("ref", "Referencia")]


def get(esc, nivel, var):
    for f in res:
        if f["escenario"] == esc and float(f["nivel"]) == nivel and f["variable"] == var:
            return f
    raise KeyError((esc, nivel, var))


def m(esc, niv, var):
    return float(get(esc, niv, var)["media"])


def dic(esc, niv, var):
    f = get(esc, niv, var)
    return (f"${float(f['media']):+.4f}$ "
            f"$[{float(f['ic95_inf']):+.4f},\\,{float(f['ic95_sup']):+.4f}]$")


CONFIGS = [("E1", "E1", 0.0, r"$\eta=\kappa=0$")]
CONFIGS += [("E2" if i == 0 else "", "E2", v, rf"$\eta={v:g}$")
            for i, v in enumerate((0.25, 0.5, 0.75, 1.0))]
CONFIGS += [("E3" if i == 0 else "", "E3", v, rf"$\kappa={v:g}$")
            for i, v in enumerate((0.25, 0.5, 0.75, 1.0))]
SEP = {1, 5}  # \midrule antes de estas filas

L = [r"\begin{table}[ht]", r"\centering",
     r"\caption{Exactitud media por paso de cada método y diferencias pareadas con "
     r"IC95\,\% ($R=100$ réplicas; $S=50$ secuencias de $T=100$ acciones por réplica). "
     r"$D=\mathrm{Acc}^{\mathrm{Vit}}-\mathrm{Acc}^{\mathrm{ref}}$ (variable principal); "
     r"$D_{\mathrm{post}}=\mathrm{Acc}^{\mathrm{post}}-\mathrm{Acc}^{\mathrm{ref}}$ (secundaria). "
     r"Las desviaciones estándar están en \texttt{results/resumen.csv}.}",
     r"\label{tab:res}", r"\footnotesize", r"\setlength{\tabcolsep}{4pt}",
     r"\begin{adjustbox}{max width=\textwidth}", r"\begin{tabular}{llccccc}", r"\toprule",
     r"Esc. & Nivel & Viterbi & Posterior & Referencia & $\bar D$ [IC95\,\%] & "
     r"$\bar D_{\mathrm{post}}$ [IC95\,\%] \\", r"\midrule"]
for k, (nom, esc, niv, et) in enumerate(CONFIGS):
    if k in SEP:
        L.append(r"\midrule")
    L.append(f"{nom} & {et} & {m(esc, niv, 'acc_vit'):.4f} & {m(esc, niv, 'acc_post'):.4f} & "
             f"{m(esc, niv, 'acc_ref'):.4f} & {dic(esc, niv, 'D')} & {dic(esc, niv, 'D_post')} \\\\")
L += [r"\bottomrule", r"\end{tabular}", r"\end{adjustbox}", r"\end{table}", ""]

L += [r"\begin{table}[ht]", r"\centering",
      r"\caption{Exactitud por fase (proporción de pasos de cada fase verdadera asignados "
      r"correctamente; media sobre réplicas). D: defensiva, T: transición, At: ataque.}",
      r"\label{tab:fase}", r"\footnotesize", r"\setlength{\tabcolsep}{4pt}",
      r"\begin{adjustbox}{max width=\textwidth}", r"\begin{tabular}{ll" + "c" * 9 + "}", r"\toprule",
      r" & & " + " & ".join(rf"\multicolumn{{3}}{{c}}{{{n}}}" for _, n in METODOS) + r" \\",
      r"\cmidrule(lr){3-5}\cmidrule(lr){6-8}\cmidrule(lr){9-11}",
      r"Esc. & Nivel & " + " & ".join(["D & T & At"] * 3) + r" \\", r"\midrule"]
for k, (nom, esc, niv, et) in enumerate(CONFIGS):
    if k in SEP:
        L.append(r"\midrule")
    vals = [m(esc, niv, f"rec_{c}_{f}") for c, _ in METODOS for f in FASES]
    L.append(f"{nom} & {et} & " + " & ".join(f"{x:.3f}" for x in vals) + r" \\")
L += [r"\bottomrule", r"\end{tabular}", r"\end{adjustbox}", r"\end{table}", ""]

conf = {(f["metodo"], f["fase_verdadera"]): f for f in csv.DictReader(open(OUT / "confusion_E1.csv"))}
nom_f = {"defensiva": "defensiva", "transicion": "transición", "ataque": "ataque"}
L += [r"\begin{table}[ht]", r"\centering",
      r"\caption{Matriz de confusión en E1 (conteo de pasos acumulado sobre todas las "
      r"réplicas; filas: fase verdadera; columnas: fase asignada).}",
      r"\label{tab:conf}", r"\small", r"\begin{tabular}{llrrr}", r"\toprule",
      r"Método & Fase verdadera & D & T & At \\"]
for c, nombre in METODOS:
    L.append(r"\midrule")
    for i, f in enumerate(FASES):
        fila = conf[(c, f)]
        L.append(f"{nombre if i == 0 else ''} & {nom_f[f]} & " +
                 " & ".join(f"{int(fila['pred_' + n]):,}".replace(",", r"\,") for n in FASES) + r" \\")
L += [r"\bottomrule", r"\end{tabular}", r"\end{table}", ""]

(OUT / "tablas_resultados.tex").write_text("\n".join(L), encoding="utf8")
print("Escrito results/tablas_resultados.tex")

# Bitácora — Anteproyecto HMM, caso fútbol

Formato de cada entrada: consulta · propuesta · verificación · decisión humana · justificación · evidencia.
Regla: solo se registran como decisiones las expresadas explícitamente por el equipo en el chat.

## Decisiones registradas

| ID | Fecha | Decisión (texto del equipo) | Propuesta de origen | Justificación aportada |
|---|---|---|---|---|
| D1 | 2026-11-09 | «Opcion 1» | P1 Viterbi vs. baseline sin transiciones; P2 sensibilidad a B; P3 sensibilidad a A | No aportada |
| D2 | 2026-11-09 | «α» | E1 parámetros del caso; E2 B más ambigua; E3 A menos persistente | No aportada |
| D3 | 2026-11-09 | «Utilicemos el documento que he subido, parece que muchos de estos documentos son de pago.» | Estado del arte | Acceso: otras fuentes son de pago |
| D4 | 2026-11-09 | «Juan Sebastian Lopez Gallo/js.lopez.academic.2003@gmail.com, deja un espacio vacio para colocar un segundo integrante» | Autoría | — |
| D5 | 2026-11-09 | «formato LaTeX» | Formato | — |
| D6 | 2026-11-09 | «Aceptamos todo» | Diseño (etapa 5): T = 100, S = 50, R = 100; η ∈ {0, 0,25, 0,5, 0,75, 1}; κ ∈ {0, 0,25, 0,5, 0,75, 1}; semilla raíz con una semilla por réplica compartida entre niveles; empates resueltos por menor índice; exactitud por fase como métrica secundaria | No aportada. Interpretación de «todo»: incluye lo que se presentó como propuesta. **No incluye** el nivel de A más persistente (se dijo que no se añadiría salvo petición) ni el piloto (era opcional). Corregir si no es así. |
| — | 2026-11-09 (sesión previa) | Plantilla: `articulo.pdf` («puedes utilizar esta plantilla para el ejercicio») | — | — |

| D7 | 2026-11-13 | «Utilicemos la semilla 20261109» | Semilla raíz (pendiente 8) | — |
| D8 | 2026-11-13 | «podemos añadir este articulo en el estado del arte» (Fani et al., 2017) | Ampliar el estado del arte con una segunda fuente aportada por el equipo | — |
| D9 | 2026-11-13 | «Aceptamos y ejecuta el experimento» | Código explicado: `viterbi_log`, clasificador de referencia (borrador) y simulador (borrador), con semillas `SeedSequence(20261109).spawn(100)` | Tras la explicación línea a línea solicitada por el equipo |
| D10 | 2026-11-13 | «Sí, añádela» | Añadir la decodificación posterior (forward-backward) como tercer método del diseño | Surge del diagnóstico E7. Interpretación: es un método **complementario**; las preguntas P1–P3 y la variable principal D = Acc_Vit − Acc_ref no cambian. Se añade D_post = Acc_post − Acc_ref como variable secundaria. Corregir si no es así. |
| D11 | 2026-11-13 | «Validadas, sigamos» | Validar la correspondencia entre las cifras de §5 y la ejecución (E8) | — |
| D12 | 2026-11-14 | «Las recomendadas» | Interpretaciones: P1-A, P2-A, P3-A (descriptivas) y los tres límites propuestos | Interpretación de «las recomendadas»: solo las opciones marcadas como recomendadas (P1-A, P2-A, P3-A) y los límites. **Las explicaciones H1–H4 no tenían recomendación** → no se incorporan como interpretación; quedan pendientes. Corregir si no es así. |
| D13 | 2026-11-14 | «añadamos solamente H3 y H4» | Incluir en la discusión las hipótesis H2 (fases cortas), H3 (solapamiento de emisiones) y H4 (sesgo de Viterbi hacia la fase más persistente y frecuente) | No aportada. H3 y H4 se redactan en §6.1 como hipótesis («compatibles con»). **H2 no se incluye** y no se añade el nivel de A más persistente; el diseño no cambia y no se reejecuta. |
| D14 | 2026-11-14 | «El resumen se encuentra bien.» | Versión del resumen redactada en E9 | Se retira la marca de pendiente del resumen. |
| D15 | 2026-11-14 | «datos del segundo integrante : Andres Miguel Hernandez, andres.hernandez74@est.iudigital.edu.co» | Autoría (hueco de D4) | — |
| D16 | 2026-11-14 | «Nombre del profesor: Julian Andres Loaiza Lopez» | Docente asesor | Se incluye solo el nombre como «Docente». El enlace al perfil del aula virtual no se incluye en el manuscrito. No se indicó autor de correspondencia. |
| D17 | 2026-11-14 | «Son 3 objectivos especificos.» | Pendiente 3: tres objetivos (uno por pregunta) o dos | Se mantienen los tres objetivos de §2. |
| D18 | 2026-11-14 | «Ingenieria de software y datos, UI digital. La materia se llama "Simulacion"» | Afiliación (pendiente 4) | Interpretación: «UI digital» se escribe «IU Digital», como en el dominio del correo del segundo integrante (iudigital.edu.co). No se expande a un nombre oficial que el equipo no dio. Corregir si no es así. |
| D19 | 2026-11-14 | «Vamos a dejar el estado del arte como se encuentra debido a que casi todos los documentos son de pago» | Pendiente 9: ampliar el estado del arte con búsqueda en fuentes abiertas | Acceso: casi todos los documentos son de pago. §3 queda con dos fuentes y se indica el motivo en el texto. |
| D20 | 2026-11-14 | «aprobamos la declaración de la IA» | Texto de la declaración de uso de IA | Se retira la marca de pendiente; el texto no cambia. |
| D21 | 2026-11-14 | «Citar Ötting y quitarla» | Cita de §4.1 (tres problemas clásicos): citar a Ötting et al. o quitar la marca sin cita | Comprobado en el PDF antes de redactar: *forward* con coste O(TN²) en p. 14; estimación por máxima verosimilitud numérica (`nlm()`, 50 valores iniciales) en pp. 14–15; Viterbi con coste O(TₘN²) en p. 22. Ötting **no usa Baum–Welch/EM** → no se le atribuye; se indica que estima de otra forma. Ötting no presenta las tareas como «tres problemas clásicos» → la frase introductoria no se le atribuye. Baum–Welch queda sin cita. |
| D22 | 2026-11-14 | «Sí, redáctala» | Redactar la parte de resultados del guion del vídeo (Anexo B) | Encargo de redacción, no aprobación del texto. El guion se divide en 1:30–2:20 (resultados) y 2:20–2:50 (conclusión y límites); usa solo cifras ya presentes en §5–§7 y H3/H4 como hipótesis (D13). Texto aprobado en D23. |
| D23 | 2026-11-14 | «Aprobado» | Texto del guion del vídeo redactado en D22 (Anexo B) | Se aprueba sin cambios. |
| D24 | 2026-11-14 | «Quitarlo» | ¿El título debe seguir diciendo «Anteproyecto»? | Se elimina el subtítulo «Anteproyecto». Ajustes derivados: comentario del encabezado del `.tex` y un verbo en futuro de §4.3 («Se usará… se derivarán» → «Se usa… se derivan»), porque el experimento ya se ejecutó. El nombre de la carpeta `anteproyecto-futbol` no se cambia. |
| D25 | 2026-11-14 | «Remitir a trabajo futuro» | Marca del supuesto S6 (definición operativa de fases y de la unidad de secuencia con datos reales) | Se quita la marca; S6 remite al punto (ii) del trabajo futuro (§7), que ya trataba la definición operativa de las fases. |
| D26 | 2026-11-14 | «Por el momento crea una carpeta local, de tal forma que despues pueda subirla a github con la consola.» | Repositorio (Anexo A): carpeta local o publicar en GitHub | `git init -b main` en la carpeta del proyecto, **sin commit ni remoto**. Añadidos `README.md` (descripción e instrucciones para reproducir) y `.gitignore` (auxiliares de LaTeX, `__pycache__`). Anexo A actualizado. Los PDF de las fuentes no están en la carpeta. No se ha elegido licencia. |

## Entradas

### E1 · 2026-11-09 · Lectura de la plantilla `articulo.pdf`
- Consulta: estructura de la plantilla del curso (8 páginas).
- Verificación: texto extraído con `pdftotext`.
- Hallazgo: contiene cifras de ejemplo (94,2 %, 78,5 %, Tabla 3, 15,7 %) y referencias [3]–[7] no verificadas → **no se reutilizan**. Viterbi del Listing 1 en espacio de probabilidades (riesgo de underflow).
- Decisión humana: usar su estructura (ver tabla).

### E2 · 2026-11-09 · Lectura de la fuente aportada
- Fuente: Ötting, M., Langrock, R., Maruotti, A. (2023). A copula-based multivariate hidden Markov model for modelling momentum in football. *AStA Advances in Statistical Analysis*, 107, 9–27. https://doi.org/10.1007/s10182-021-00395-8
- Licencia: CC BY 4.0 (declarada en p. 25).
- Lectura: texto completo extraído con `pdftotext` (no resumen automático). Pasajes usados y páginas:
  - p. 10: datos minuto a minuto de un equipo (34 partidos, 3214 observaciones bivariadas, temporada 2017/18).
  - p. 12–13: estructura HMM; hay que elegir N y la distribución dependiente del estado.
  - p. 14–15: algoritmo forward O(TN²); partidos supuestos independientes; múltiples valores iniciales (50) contra máximos locales.
  - p. 19: AIC prefiere 5 estados y BIC 3; eligen 3 también por interpretabilidad.
  - p. 20: estados interpretados como control bajo/contraataque, equilibrado y control alto.
  - p. 22: decodificación con Viterbi.
  - p. 23: los estados de un HMM no supervisado son solo aproximaciones (*proxies*) de estados genuinos; la secuencia decodificada puede diferir de la real.
  - p. 24: los datos no permiten separar cambios tácticos de cambios de momentum.
  - p. 25: limitación: solo se modela un equipo.
- Pendiente: citas de segunda mano (Rabiner 1989, Zucchini et al. 2016, Leos-Barajas et al. 2017) **no leídas** → no se citan; se marcan como pendientes.

### E3 · 2026-11-09 · Verificación de implementación (no es un resultado experimental)
- Propuesta: Viterbi en log-espacio (Listing del manuscrito, §4.2).
- Verificación: comparada con búsqueda exhaustiva en 200 secuencias aleatorias (T = 1–6) con los A, B, π del caso: 200/200 coincidencias en log-probabilidad máxima; T = 5000 sin underflow.
- Entorno de la verificación: Python 3.14.2, NumPy 2.5.3 (script en el directorio temporal de la sesión; no forma parte del repositorio).
- Decisión humana: **pendiente** (aceptar el código solo si el equipo lo comprende y revisa).

### E4 · 2026-11-09 · Redacción del borrador `main.tex`
- Construido solo con decisiones D1–D5 y la plantilla. Lo provisional aparece en rojo como `\pendiente{...}`.
- No compilado: no hay compilador LaTeX instalado en este equipo.

### E5 · 2026-11-09 · Valores del diseño experimental
- Propuesta: tabla de valores de T, S, R, η, κ y semillas, con justificación.
- Verificación (propiedades del modelo, no resultados): en E1 cambia la fase en 0,494 de cada paso; con κ de 0 a 1, la diagonal de A baja de (0,60, 0,40, 0,50) a 1/3 y los cambios por paso suben de 0,494 a 0,667; con η = 0,75 el clasificador de referencia asigna tiro→defensiva; con η = 1, todo→defensiva.
- Decisión humana: D6 («Aceptamos todo»).
- Incorporado a `main.tex` (§1.1 S6, §4.3, Tabla de resultados).

### E6 · 2026-11-13 · Lectura de la segunda fuente aportada
- Fuente: Fani, M., Yazdi, M., Clausi, D. A., Wong, A. (2017). Soccer video structure analysis by parallel feature fusion network and hidden-to-observable transferring Markov model. *IEEE Access*, 5, 27322–27336. https://doi.org/10.1109/ACCESS.2017.2769140
- Derechos: © 2017 IEEE. La nota de la p. 27322 permite la minería de contenido para investigación académica y el uso personal; la republicación requiere permiso. → Se cita y se parafrasea; no se reproducen figuras ni tablas.
- Lectura: texto completo extraído con `pdftotext`. Las tablas son imágenes y su contenido no se extrajo: **solo se usa la cifra que aparece en el texto (98,7 %, resumen)**. Pasajes usados:
  - p. 27322: objetivo (clasificar el tipo de plano y segmentar el vídeo en juego/interrupción).
  - p. 27324: HMM previo [9] con 2 estados (juego, interrupción) y 4 observaciones (tipos de plano); parámetros aprendidos y decodificación con Viterbi.
  - pp. 27329–27330: H2O-MM; matrices estimadas con datos etiquetados a los que se añade un 1 % de ruido en cada iteración; Viterbi; los estados inferidos de 3 planos previos y 3 siguientes pasan a ser observaciones.
  - p. 27330: datos: 10 vídeos (9 h), 3452 planos.
  - p. 27333: evaluación del H2O-MM: 100 iteraciones, 10 ejecuciones; se reporta la exactitud media de las iteraciones de la última ejecución; se compara con dos HMM previos.
- Observación crítica (inferencia, no hecho): en los pasajes leídos no se describe una partición entrenamiento/prueba para el H2O-MM, y el algoritmo usa las etiquetas verdaderas en cada iteración. No puede descartarse que la exactitud se mida sobre los mismos datos usados para estimar los parámetros. Se redacta como límite de la comparación, no como acusación.
- Pendiente: las referencias secundarias [9] Tavassolipour et al. y [11] Xie et al. **no se han leído** → no se citan.

### E7 · 2026-11-13 · Ejecución del experimento (D9)
- Código: `src/hmm_core.py` (viterbi_log, clasificador_ref, simular, tal como se explicaron), `src/utils_stats.py` (t₀,₉₇₅,₉₉ = 1,984217 de tabla), `main_simulation.py`.
- Ejecución: una sola, 63 s; entorno en `results/entorno.txt` (Python 3.14.2, NumPy 2.5.3, Windows 11). Salidas: `results/replicas.csv`, `resumen.csv`, `confusion_E1.csv`; figura `results/fig_D.pdf` (`figuras.py`); tablas LaTeX generadas desde los CSV (`tablas_latex.py`), sin transcripción manual.
- Comprobaciones: 9 configuraciones × 100 réplicas; la matriz de confusión de E1 suma 500 000 pasos por método (= 100 × 50 × 100). Controles negativos: D = 0 exacto en η = 1 y κ = 1. No anticipado: D = 0 exacto también en κ = 0,75.
- Hallazgo inesperado: en E1, Viterbi < referencia (D̄ = −0,0327; IC95 [−0,0340, −0,0313]).
- Verificación complementaria (fuera del diseño aprobado, `verificacion/diagnostico_decodificacion.py`, semillas 777 y 888; salida en `results/diagnostico.txt`): exactitud analítica de la referencia = 0,550 (observada 0,551); Viterbi = búsqueda exhaustiva en 100/100 secuencias de E1 con T = 8; decodificación posterior 0,5548, referencia 0,5516 y Viterbi 0,5221 en 2000 secuencias. → La diferencia se atribuye al criterio de Viterbi (camino conjunto), no a un error de código.
- Decisión humana: **pendiente** validar la correspondencia entre cifras y ejecución, y elegir las interpretaciones (discusión y conclusiones).

### E8 · 2026-11-13 · Tercer método: decodificación posterior (D10)
- Código: `posterior_decode` en `src/hmm_core.py` (forward-backward escalado); `main_simulation.py` calcula los tres métodos, D (principal) y D_post (secundaria).
- Verificación: `verificacion/test_posterior.py` → coincide con el argmax de las marginales exactas por enumeración en 100/100 secuencias (T = 1–7); salida en `results/test_posterior.txt`.
- Reejecución completa (79 s). Los resultados de la ejecución 1 se archivaron en `results/ejecucion1/`; las 900 filas de Viterbi y referencia son **idénticas** (0 celdas distintas), porque el método nuevo no consume números aleatorios.
- Resultados de D_post: positiva y pequeña en E1 (+0,0020; IC95 [+0,0016, +0,0025]), η = 0,25–0,75 (máx. +0,0072 en η = 0,75) y κ = 0,25; exactamente 0 en η = 1 y κ ≥ 0,5; nunca negativa.
- Tablas y figura regeneradas desde los CSV; `main.tex` actualizado (§3.4, §4, §5 y declaración de IA).
- Decisión humana: **pendiente** validar las cifras y elegir las interpretaciones.

### E9 · 2026-11-14 · Redacción con D12 y compilación
- Redactados: resumen (pendiente de aprobación), discusión (síntesis, relación con fuentes, limitaciones) y respuestas a P1–P3, con las opciones A y los límites (D12). H2–H4 quedan marcadas como pendientes en §6.1.
- Compilado con MiKTeX (pdflatex, 2 pasadas): 0 errores, 0 referencias indefinidas, 0 cajas desbordadas tras ajustar (`url`, `\emergencystretch`, ancho de columna). `main.pdf`: 11 páginas. Revisión visual de las páginas de resultados, discusión, conclusiones y anexos.

### E10 · 2026-11-14 · Hipótesis H3 y H4 en la discusión (D13)
- Sustituido el pendiente de §6.1 por H3 y H4, redactadas como hipótesis.
- Cifras tomadas de `results/resumen.csv` y `results/confusion_E1.csv`, comprobadas antes de redactar: asignación a defensiva 311 958/500 000 = 62,4 % (Viterbi), 49,0 % (referencia), 47,3 % (posterior), verdad 194 977/500 000 = 39,0 %; acierto de Viterbi en defensiva 0,810 (E1), 0,858, 0,973 y 1,000 (η = 0,25; 0,5; 0,75); exactitud de la referencia 0,551 (E1) → 0,393 (η = 0,75).
- Recompilado con MiKTeX.

## Pendientes científicos (agrupados)
1. ~~Valores de T, S y R~~ → resuelto en D6.
2. ~~Valores de η y κ~~ → resuelto en D6.
3. ~~Número de objetivos específicos~~ → resuelto en D17 (tres).
4. ~~Docente~~ → resuelto en D16. ~~Afiliación~~ → resuelta en D18.
5. ~~Datos del segundo integrante~~ → resuelto en D15.
6. ~~Aprobación de la declaración de uso de IA~~ → resuelto en D20.
7. Revisión y aceptación del código Viterbi y del baseline.
8. ~~Valor de la semilla raíz~~ → resuelto en D7 (20261109).
9. ~~Si se amplía el estado del arte~~ → resuelto en D19 (no se amplía). Consecuencia: la cita para los tres problemas clásicos (§4.1, p. ej. Rabiner 1989) sigue sin poder añadirse, porque no se ha leído el original.

## Siete etapas — estado

| Etapa | Estado | Responsable | Evidencia |
|---|---|---|---|
| 1 Protocolo | Decidido (D1–D5) | Equipo | Tabla de decisiones |
| 2 Recopilación | Plantilla y dos fuentes | IA reúne · equipo validó las fuentes (D3, D8) | E1, E2, E6 |
| 3 Normalización | Notación unificada λ=(S,V,A,B,π); sumas verificadas | IA | Sesión previa (numpy) |
| 4 Depuración | Cifras/referencias de ejemplo de la plantilla excluidas | IA detecta · equipo confirma | E1 |
| 5 Valoración | Diseño decidido (D6); tres objetivos específicos (D17) | Equipo | D6, D17, E5 |
| 6 Construcción | Borrador con resultados; discusión y conclusiones pendientes | IA redacta | `main.tex`, `results/` |
| 7 Verificación | Código verificado (E3, E7); falta validación del equipo y aprobación final | Equipo aprueba | E7 |

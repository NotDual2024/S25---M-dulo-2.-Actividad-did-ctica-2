# Pitch: guion para dos voces

**Trabajo:** Aporte de la dependencia temporal a la inferencia de fases tácticas simuladas mediante Modelos Ocultos de Markov
**Duración objetivo:** 4–5 minutos, más preguntas
**Voces:** **JUAN** (Juan Sebastian Lopez Gallo) · **ANDRÉS** (Andres Miguel Hernandez)

> Las indicaciones entre corchetes son para vosotros, no se leen. Las cifras salen de `results/resumen.csv` y `results/confusion_E1.csv`.

---

## 1. Gancho · 0:00–0:30

**JUAN:**
Profesor, cuando vemos un partido decimos «el equipo está defendiendo» o «está atacando». Pero esa fase no aparece en ningún dato: lo que se registra son acciones, como un pase corto, un pase largo o un tiro. Y una acción sola no dice en qué fase estamos: un pase corto puede ser defensa, transición o ataque.

**ANDRÉS:**
Los Modelos Ocultos de Markov prometen resolver eso: usar la secuencia de acciones, y no solo cada acción por separado, para inferir la fase oculta. Nuestra pregunta fue sencilla: **¿cuánto ayuda de verdad esa secuencia?**

---

## 2. Por qué simulación · 0:30–1:10

**JUAN:**
Con datos reales no se puede responder, porque nadie sabe cuál era la fase verdadera en cada momento. Ötting y sus coautores, que modelan la Bundesliga con HMM, lo advierten: los estados que encuentra el modelo son solo aproximaciones de los estados reales.

**ANDRÉS:**
Por eso trabajamos al revés. Simulamos partidos con un HMM cuyos parámetros conocemos: tres fases (defensiva, transición y ataque) y tres acciones. Como nosotros generamos los datos, sabemos la fase verdadera en cada paso y podemos medir cuánto acierta cada método.

**JUAN:**
Es el escenario más favorable posible: el modelo es exactamente el correcto y los parámetros son conocidos. Si aquí la secuencia no ayuda mucho, con datos reales difícilmente ayudará más.

---

## 3. Qué comparamos · 1:10–2:00

[Mostrar la tabla de la metodología o el flujo con los tres métodos.]

**ANDRÉS:**
Comparamos tres métodos, todos con los mismos parámetros:
- **Viterbi**, que busca la secuencia completa de fases más probable.
- **La decodificación posterior**, que elige, paso a paso, la fase más probable teniendo en cuenta toda la secuencia.
- Y un **clasificador de referencia** que mira solo la acción actual, sin transiciones.

**JUAN:**
La diferencia entre Viterbi y la referencia, que llamamos **D**, mide exactamente cuánto aportan las transiciones. Esa es nuestra variable principal.

**ANDRÉS:**
Probamos tres escenarios: los parámetros del caso, emisiones cada vez más ambiguas y transiciones cada vez menos persistentes. En total, nueve configuraciones, con 100 réplicas de 50 secuencias de 100 acciones cada una. Usamos la semilla 20261109, así que todo es reproducible.

---

## 4. El resultado · 2:00–3:10

[Mostrar la Tabla 3 y la Figura 1.]

**JUAN:**
Y aquí vino la sorpresa. Con los parámetros del caso, **Viterbi acertó menos que el clasificador que ignora las transiciones**: 51,8 % frente a 55,1 %. La diferencia es de −0,033, con un intervalo de confianza que no toca el cero.

**ANDRÉS:**
Lo primero que pensamos fue que teníamos un error en el código. Así que lo verificamos de tres formas:
- comparamos Viterbi con una búsqueda exhaustiva de todas las secuencias posibles y coincidió en 100 de 100 casos;
- calculamos la exactitud de la referencia de forma analítica, 0,550, y la simulación dio 0,551;
- y comprobamos la decodificación posterior contra las probabilidades exactas, también en 100 de 100 casos.

**JUAN:**
No era un error. La explicación es que **Viterbi y nuestra métrica buscan cosas distintas**: Viterbi maximiza la probabilidad del camino completo, y nosotros contamos pasos acertados. El método que sí optimiza pasos acertados, la decodificación posterior, superó a la referencia, pero por solo **dos milésimas**.

---

## 5. Por qué pasa · 3:10–3:50

[Mostrar la matriz de confusión, Tabla 5.]

**ANDRÉS:**
La matriz de confusión muestra cómo pierde Viterbi: asigna la fase defensiva al **62 % de los pasos**, cuando en realidad solo el 39 % eran defensivos. Acierta casi todas las defensas, pero solo **una de cada cuatro transiciones**, mientras que la referencia acierta la mitad.

**JUAN:**
Planteamos dos hipótesis compatibles con esto, sin afirmar que estén demostradas. Primera: las fases emiten acciones muy parecidas; el pase corto es frecuente en las tres, así que ningún método puede acertar mucho. Segunda: Viterbi tiende a quedarse en la fase más persistente y más frecuente, que es la defensiva.

**ANDRÉS:**
Los otros escenarios refuerzan la idea. Cuando las acciones se vuelven más ambiguas, Viterbi termina diciendo «defensiva» en todos los pasos. Y cuando las fases cambian más a menudo, los tres métodos acaban dando exactamente las mismas respuestas.

---

## 6. Cierre · 3:50–4:30

**JUAN:**
En resumen: con estos parámetros, **usar la secuencia aporta muy poco a la exactitud por paso, y con Viterbi incluso la empeora**. Y hay una lección práctica: el método de decodificación tiene que elegirse según lo que se quiere medir.

**ANDRÉS:**
Somos conscientes de los límites. Los parámetros son hipotéticos, el modelo es correcto por construcción y solo trabajamos con dos fuentes, porque la mayoría de los artículos eran de pago. Nada de esto permite hacer afirmaciones sobre partidos reales.

**JUAN:**
Como trabajo futuro: estimar los parámetros con Baum–Welch en lugar de conocerlos, y definir las fases para poder anotarlas en datos reales.

**ANDRÉS:**
El código, los resultados y la bitácora de decisiones están en el repositorio, y todo se reproduce siguiendo las instrucciones del README. Gracias, profesor. Quedamos atentos a sus preguntas.

---

## Preguntas probables del profesor

**¿Por qué no usaron datos reales?**
Porque en datos reales no se conoce la fase verdadera, y sin ella no se puede medir la exactitud. La simulación es el único escenario donde la verdad se conoce. (Responde: ANDRÉS)

**¿De dónde salen los parámetros A, B y π?**
Son hipotéticos, del caso del curso; no se estimaron de datos reales. Por eso las conclusiones valen solo para este modelo. (Responde: JUAN)

**¿Seguro que Viterbi está bien implementado?**
Sí: está en espacio logarítmico y coincidió con la búsqueda exhaustiva en 100 de 100 secuencias. Los scripts están en la carpeta `verificacion/`. (Responde: JUAN)

**Si Viterbi acierta menos, ¿por qué se usa tanto?**
Porque devuelve una secuencia coherente, con transiciones posibles, y es la que maximiza la probabilidad del camino completo. Si lo que importa es acertar cada paso, la decodificación posterior es más adecuada. (Responde: ANDRÉS)

**¿Por qué 100 réplicas y la misma semilla en todos los niveles?**
Con 100 réplicas los intervalos de confianza son estrechos (±0,0014 en E1). Usar la misma semilla por réplica en todos los niveles hace que las diferencias entre niveles se deban al parámetro y no al azar. (Responde: JUAN)

**¿Cuál fue el uso de la IA?**
Se usó un asistente de IA para estructurar el documento, redactar borradores, escribir y verificar el código y ejecutar la simulación. Las decisiones científicas las tomamos nosotros y están registradas en la bitácora. (Responde: ANDRÉS)

---

## Consejos para la presentación

- Ensayad en voz alta con cronómetro; si pasáis de 5 minutos, recortad la sección 5.
- Tened abiertas la Tabla 3, la Figura 1 y la Tabla 5 del PDF para mostrarlas en su momento.
- La frase clave es: **«Viterbi optimiza el camino completo; nosotros medimos pasos acertados»**. Si el profesor solo recuerda una idea, que sea esa.

# Retroalimentación — Laboratorio 01: Fundamentos, complejidad y recurrencias

**Estudiante:** Januar Stiwar Martinez Palacios · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-13 23:59 · **Versión revisada:** commit `25e5793`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 17 / 25 |
| Calidad de la explicación teórica | 20 / 25 |
| Corrección de la implementación | 15 / 20 |
| Calidad del análisis de las gráficas | 17 / 20 |
| Documentación y organización del informe | 9 / 10 |
| **Total** | **78 / 100** |
| **Nota (0–5)** | **3.90** |

## 1. Corrección conceptual (17 / 25)
**Lo que hizo bien:**
- Distingue entre un resultado correcto y uno que llega a tiempo, y nombra la ventana de cuatro horas como la restricción que no se cumple.
- Explica que duplicar la velocidad del servidor no cambia cómo crece el trabajo al aumentar los datos.
- Da un segundo ejemplo propio (llamadas de clientes, 2.000.000 de registros, ventana de 8 horas).
- Habla de la repetición diaria del consumo de energía y de que el orden de la lista decide a quién se llama primero.

**Lo que puede mejorar:**
- En la Parte 2 no explica cómo el tiempo de ejecución se vuelve energía (por ejemplo, horas de servidor encendido por año).
- Los perjuicios están mencionados, pero no dice con claridad quién asume el costo en el caso del paciente (¿el paciente, la Secretaría, el equipo?).
- Falta explicar mejor qué obligación adicional tiene el equipo cuando el orden de la lista decide quién recibe atención primero.

## 2. Calidad de la explicación teórica (20 / 25)
**Lo que hizo bien:**
- Define mejor, peor y promedio sobre listas del mismo tamaño `n`, y justifica usar el peor caso para decidir la entrada a producción.
- Escribe la predicción antes del experimento y señala que se confirmó.
- Plantea la recurrencia de merge sort, explica cada término y la resuelve por sustitución hasta `O(n log n)`.
- Presenta la tabla de complejidades por caso.

**Lo que puede mejorar:**
- En la sustitución falta revisar el caso base y la constante que sostiene la hipótesis.
- El análisis de insertion sort línea a línea usa constantes `C1…C7` genéricas; debía indicar cuántas veces se ejecuta cada línea de su propio código y relacionarlas con él.

## 3. Corrección de la implementación (15 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien de mayor a menor, no cambian la lista recibida, cuentan comparaciones entre elementos y no usan `sorted()` ni `sort()`.
- Los tres generadores dan listas del tamaño pedido, con valores distintos y semilla reproducible.

**Lo que puede mejorar:**
- Faltan *type hints* y *docstring* completos en las funciones de `parte3_casos.py` y `parte4_complejidad.py` (parámetros sin tipo, sin retorno).
- Estilo PEP 8: faltan líneas en blanco entre funciones en `algoritmos.py` y `datos.py`, hay espacios de más en la llamada a `merge` y en la suma de comparaciones, y las importaciones están después de otras instrucciones en lugar de al inicio.
- `merge_sort` copia la lista en cada llamada recursiva sin necesidad.

## 4. Calidad del análisis de las gráficas (17 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, con título, ejes rotulados, leyenda y las curvas pedidas en los mismos ejes.
- Identifica con datos que el escenario C es el peor caso, el B el mejor y el A se acerca al promedio.
- Concluye, desde la gráfica de la Parte 4, que merge sort es mejor y lo relaciona con `O(n²)` frente a `O(n log n)`.
- El concepto técnico recomienda merge sort, extrapola a 1.200.000 registros declarándolo estimación (cerca de 21 horas para insertion sort), responde a la propuesta del servidor y comenta la memoria extra.

**Lo que puede mejorar:**
- Algunas cifras del informe no coinciden con las gráficas publicadas: en `parte3_tiempo.png` el escenario inverso llega a cerca de 4.0 s y el aleatorio a cerca de 1.9 s en n = 6400, pero el informe dice 4.35 s y 2.09 s. Cite lo que realmente muestra la gráfica entregada.
- Para tamaños pequeños dice que merge sort ya gana; explique con más cuidado por qué las curvas casi se tocan allí.

## 5. Documentación y organización del informe (9 / 10)
**Lo que hizo bien:**
- El laboratorio está en `laboratorios/lab1-fundamentos-complejidad-recurrencias/`, con todos los archivos y gráficas del entregable.
- Las gráficas se ven en el informe, y las Partes 3 y 4 enlazan su código, `algoritmos.py` y `datos.py`.
- Hay más de cinco commits con mensajes descriptivos.

**Lo que puede mejorar:**
- Las instrucciones de reproducción solo sirven para Windows (PowerShell) y los comandos de cada parte quedaron mezclados dentro del mismo bloque de código.

## ¿El código funciona?
Sí. Ambos algoritmos ordenan correctamente los tres escenarios y los scripts de las Partes 3 y 4 corren sin errores y generan las gráficas.

## Para el próximo laboratorio
- Cite en el informe los valores que realmente se ven en las gráficas entregadas.
- Explique con números el paso de tiempo de ejecución a energía y diga quién asume cada costo.
- En el conteo línea a línea, indique cuántas veces se ejecuta cada línea de su propio código.
- Agregue *type hints* y *docstrings* a todas las funciones y revise el estilo PEP 8.
- Escriba instrucciones de reproducción que sirvan en cualquier sistema operativo.

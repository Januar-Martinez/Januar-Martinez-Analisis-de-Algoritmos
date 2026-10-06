# Retroalimentación — Laboratorio 01: Fundamentos, complejidad y recurrencias

**Estudiante:** Januar Stiwar Martinez Palacios · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-06 23:59 · **Versión revisada:** commit `82f59fa`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 15 / 25 |
| Calidad de la explicación teórica | 15 / 25 |
| Corrección de la implementación | 14 / 20 |
| Calidad del análisis de las gráficas | 16 / 20 |
| Documentación y organización del informe | 6 / 10 |
| **Total** | **66 / 100** |
| **Nota (0–5)** | **3.30** |

## 1. Corrección conceptual (15 / 25)
**Lo que hizo bien:**
- Distingue que el algoritmo es correcto pero no cumple el tiempo: no termina en la ventana de 4 horas.
- Identifica dos perjuicios (centro de contacto y pacientes) e indica quién asume el costo de cada uno.
- Reconoce que el orden de la lista decide a quién se llama primero.

**Lo que puede mejorar:**
- Explique por qué un servidor el doble de rápido no arregla el problema: el tiempo del algoritmo crece mucho más rápido que la velocidad del equipo.
- El segundo ejemplo es muy general. Diga qué sistema es, cuántos datos tiene y qué límite se rompe, con más detalle.
- En lo ambiental, falta relacionar con más claridad las horas de ejecución con la energía gastada cada madrugada durante años.
- En la tensión ética, falte decir qué obligación adicional implica sobre la corrección del orden (por ejemplo, que un error de orden deja a un paciente grave sin llamar).

## 2. Calidad de la explicación teórica (15 / 25)
**Lo que hizo bien:**
- Da una predicción para los escenarios A, B y C antes del experimento y justifica usar el peor caso para decidir si entra en producción.
- Resuelve la recurrencia de merge sort por sustitución hasta `O(n log n)`.
- Presenta la tabla de complejidades por caso, correcta.

**Lo que puede mejorar:**
- Al definir los tres casos, indique sobre qué conjunto de entradas del mismo tamaño se toma el máximo, el mínimo y el promedio.
- Explique cada término de `T(n) = 2T(n/2) + O(n)`: cuántos subproblemas, de qué tamaño y de dónde sale el costo de combinar.
- En la sustitución falta el caso base y precisar las constantes que sostienen la hipótesis.
- La cota de insertion sort usa constantes generales (`C1`, `C2`...). Debe indicar cuántas veces se ejecuta cada línea de su propio código y explicar el resultado.

## 3. Corrección de la implementación (14 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien los tres escenarios, no cambian la lista recibida y cuentan comparaciones entre elementos (para una lista ya ordenada, insertion sort hace `n - 1`).
- Sin `sorted()` ni `sort()`; la mezcla de merge sort es propia y recursiva.
- Los generadores usan semilla y producen valores distintos, con el 2 % desordenado al final.

**Lo que puede mejorar:**
- Las funciones de `parte3_casos.py` y `parte4_complejidad.py` no tienen *type hints*, y sus *docstrings* no siguen el estilo Google (sin Args/Returns).
- Hay varios avisos de PEP 8: falta de líneas en blanco entre funciones y espacios dentro de paréntesis.
- En `datos.py` el `import` quedó antes del texto de descripción del módulo.

## 4. Calidad del análisis de las gráficas (16 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, con título, ejes rotulados, leyenda y las curvas pedidas en los mismos ejes.
- Identifica correctamente el inverso como peor caso, el casi ordenado como mejor y el aleatorio como promedio, y contrasta con su predicción.
- El concepto técnico recomienda merge sort, usa datos medidos (6.400 registros: 2,05 s contra 0,03 s), extrapola a 1.200.000 registros declarándolo estimación y responde a la propuesta del servidor.
- Considera la memoria y el riesgo de que el escenario B cambie.

**Lo que puede mejorar:**
- En 3.2 apóyese en números concretos de las gráficas (comparaciones o tiempos) para sostener cuál es cada caso.
- Las unidades del eje de comparaciones y de tiempo podrían ser más claras; el análisis de tamaños pequeños en 4.2 es muy general: diga qué pasa realmente en su gráfica.

## 5. Documentación y organización del informe (6 / 10)
**Lo que hizo bien:**
- El laboratorio está en la ubicación acordada y con los archivos del entregable.
- Las gráficas se ven en el README y cada parte enlaza su código.
- Hay 13 commits con mensajes descriptivos.

**Lo que puede mejorar:**
- Las instrucciones para reproducir quedaron al final y están incompletas: el comienzo del README tiene una frase cortada ("Para activar el enton"), el bloque de comandos no se cierra y no se indica en qué carpeta ejecutar. Deben ir al inicio.
- Los comandos indicados no funcionan tal como están escritos (ver abajo).

## ¿El código funciona?
Los algoritmos y generadores funcionan bien. Pero los scripts guardan las gráficas con una ruta que solo existe si se ejecuta desde la raíz del repositorio, y desde ahí no encuentran `datos.py` ni `algoritmos.py`. Ejecutado desde la carpeta del laboratorio, como indica el README, el programa mide pero falla al guardar la gráfica.

## Para el próximo laboratorio
- Pruebe las instrucciones del README en una carpeta limpia antes de entregar, y use rutas relativas al propio script.
- Explique cada paso de la teoría con su propio código: líneas ejecutadas, términos de la recurrencia y casos base.
- Dé más detalle y números a sus ejemplos y a la parte ambiental y ética.
- Agregue *type hints* y *docstrings* estilo Google a todas las funciones y revise el estilo PEP 8.

# Retroalimentación — Laboratorio 02: Dividir y vencer

**Estudiante:** Januar Stiwar Martinez · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `b1f50dc`

Muy buen trabajo: el laboratorio está completo y bien explicado.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 18 / 20 |
| Calidad de la explicación teórica | 19 / 20 |
| Corrección de la implementación | 23 / 25 |
| Calidad del análisis de las gráficas | 23 / 25 |
| Documentación y organización del informe | 6 / 10 |
| **Total** | **89 / 100** |
| **Nota (0–5)** | **4.45** |

## 1. Corrección conceptual (18 / 20)
**Lo que hizo bien:**
- Compara el máximo de un arreglo dividido contra el recorrido simple, con su recurrencia y el costo constante de combinar.
- Recomienda divide y vencerás y declara claramente que las cifras a 1.000.000 de registros son estimaciones, sin usar regla de tres lineal.

**Lo que puede mejorar:**
- Dice que divide y vencerás gana desde n = 50, pero allí los tiempos son casi iguales (0.000161 frente a 0.000163 s). Es más honesto decir que hay un empate y que la ventaja clara aparece desde n = 100.

## 2. Calidad de la explicación teórica (19 / 20)
**Lo que hizo bien:**
- Plantea `T(n) = 2T(n/2) + Θ(n)` y explica de dónde sale cada término.
- Resuelve con el método maestro verificando que `f(n) = Θ(n^(log_b a))` (caso 2) y justifica el `Θ(n²)` de la fuerza bruta con la suma de iteraciones.

**Lo que puede mejorar:**
- Podría explicar por qué la suma cruzada cuesta exactamente un recorrido lineal (dos barridos que juntos recorren el rango).

## 3. Corrección de la implementación (23 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en todos los casos pedidos y coinciden entre sí en listas aleatorias; no modifican la lista recibida.
- `subarreglo_maximo` resuelve los tres casos sin llamar a la fuerza bruta. Las pruebas usan 100 listas aleatorias.

**Lo que puede mejorar:**
- En `medicion.py` falta separar con dos líneas en blanco la función `graficar_tiempo`.
- Las docstrings de `medir_tiempos` no siguen el formato completo (falta describir qué hace con más detalle).

## 4. Calidad del análisis de las gráficas (23 / 25)
**Lo que hizo bien:**
- La gráfica tiene título, ejes rotulados, leyenda y ambas curvas en los mismos ejes, con 6 tamaños. Está incrustada y se ve.
- Calcula el factor al duplicar n (4.12 para fuerza bruta y 2.09 para divide y vencerás) y lo compara con lo esperado (4 y 2.22).
- Lo que afirma coincide con la gráfica (fuerza bruta cerca de 0.9 s en n = 4000, divide y vencerás casi pegada al eje).

**Lo que puede mejorar:**
- Solo hay un tamaño grande (4000); con 8000 se vería mejor la forma de las curvas.
- Cada tiempo se midió una sola vez; repetir y promediar hace las conclusiones más confiables.

## 5. Documentación y organización del informe (6 / 10)
**Lo que hizo bien:**
- Carpeta en `laboratorios/lab2-divide-y-vencer/` (ubicación válida) con todos los archivos del entregable.
- El informe sigue el orden pedido, enlaza el código en cada parte e incluye instrucciones de reproducción.

**Lo que puede mejorar:**
- Solo hay un commit que toca este laboratorio; se piden al menos tres commits descriptivos (por ejemplo uno por parte).

## ¿El código funciona?
Sí. Las pruebas pasan, las dos funciones dan siempre la misma suma máxima en mis pruebas adicionales y la medición corre y genera la gráfica.

## Para el próximo laboratorio
- Haga commits frecuentes y descriptivos, uno por cada parte del trabajo.
- Deje dos líneas en blanco entre funciones y escriba docstrings completos (con Args y Returns).
- Repita cada medición varias veces y use un tamaño grande adicional.
- Cuando dos tiempos sean casi iguales, descríbalos como empate y no como ventaja.

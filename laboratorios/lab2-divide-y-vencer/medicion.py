
"""Medicion de tiempos para los algoritmos de subarreglo maximo."""

import random
import time
import matplotlib.pyplot as plt
from pathlib import Path

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

CARPETA = Path(__file__).resolve().parent
CARPETA_GRAFICAS = CARPETA / "graficas"

def graficar_tiempo(tamanios: list[int], tiempos_fuerza_bruta: list[float], tiempos_divide_venceras: list[float], ) -> None:
    """Grafica los tiempos de ambos algoritmos en funcion del tamanio.

    Args:
        tamanios: lista de tamanios de entrada.
        tiempos_fuerza_bruta: lista de tiempos de ejecucion del algoritmo de fuerza bruta.
        tiempos_divide_venceras: lista de tiempos de ejecucion del algoritmo de divide y venceras.
    """

    plt.figure(figsize=(10, 6))
    plt.plot(tamanios, tiempos_fuerza_bruta, marker="o", label="Fuerza bruta",)
    plt.plot(tamanios, tiempos_divide_venceras, marker="o", label="Divide y venceras",)

    plt.title("Subarreglo maximo: tiempo vs. tamano de entrada")
    plt.xlabel("Tamano de la entrada (n)")
    plt.ylabel("Tiempo de ejecucion (segundos)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(CARPETA_GRAFICAS / "tiempo_vs_n.png")
    plt.close()


def medir_tiempos() -> None:
    """Mide ambos algoritmos y verifica que obtengan la misma suma."""

    tamanios = [10, 50, 100, 500, 1000, 4000]
    tiempos_fuerza_bruta = []
    tiempos_divide_venceras = []

    generador = random.Random(42)

    for n in tamanios:
        valores = [ generador.randint(-100, 100) for _ in range(n) ]

        inicio = time.perf_counter()
        resultado_fuerza = subarreglo_fuerza_bruta(valores)
        tiempo_fuerza = time.perf_counter() - inicio

        inicio = time.perf_counter()
        resultado_divide = subarreglo_maximo(valores, 0, len(valores) - 1)
        tiempo_divide = time.perf_counter() - inicio

        assert resultado_fuerza[2] == resultado_divide[2], (f"Las sumas no coinciden para n = {n}")

        tiempos_fuerza_bruta.append(tiempo_fuerza)
        tiempos_divide_venceras.append(tiempo_divide)

        print(
            f"n = {n:5d} | "
            f"Fuerza bruta: {tiempo_fuerza:.6f} s | "
            f"Divide y venceras: {tiempo_divide:.6f} s | "
            f"Suma maxima: {resultado_fuerza[2]}"
        )

    graficar_tiempo(tamanios, tiempos_fuerza_bruta, tiempos_divide_venceras,)

    print("\nTodas las sumas coinciden.")
    print("Grafica guardada en graficas/tiempo_vs_n.png")


if __name__ == "__main__":
    medir_tiempos()

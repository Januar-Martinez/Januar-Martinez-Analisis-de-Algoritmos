"""Comparacion de Insertion Sort y Merge Sort."""

import time
import matplotlib.pyplot as plt

from datos import generar_aleatorio
from algoritmos import insertion_sort, merge_sort

TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
SEMILLA = 42

def ejecutar_experimento():
    """Mide el tiempo de los dos algoritmos sobre el escenario A."""

    tiempos_insertion = []
    tiempos_merge = []

    for n in TAMANOS:
        datos = generar_aleatorio(n, SEMILLA)

        inicio = time.perf_counter()
        insertion_sort(datos)
        fin = time.perf_counter()

        tiempo_insertion = fin - inicio
        tiempos_insertion.append(tiempo_insertion)

        inicio = time.perf_counter()
        merge_sort(datos)
        fin = time.perf_counter()

        tiempo_merge = fin - inicio
        tiempos_merge.append(tiempo_merge)

        print(
            f"n={n:5} | "
            f"Insertion Sort: {tiempo_insertion:.8f} s | "
            f"Merge Sort: {tiempo_merge:.8f} s"
        )

    return tiempos_insertion, tiempos_merge


def generar_grafica(tiempos_insertion, tiempos_merge):
    """Genera la grafica comparativa de tiempos."""

    plt.figure()

    plt.plot(
        TAMANOS,
        tiempos_insertion,
        marker="o",
        label="Insertion Sort",
    )

    plt.plot(
        TAMANOS,
        tiempos_merge,
        marker="o",
        label="Merge Sort",
    )

    plt.title("Comparación de tiempos de ordenamiento")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True)

    plt.savefig(
        "laboratorios/lab1-fundamentos-complejidad-recurrencias/graficas/parte4_tiempo.png",
        dpi=300,
        bbox_inches="tight",
    )

    plt.close()


if __name__ == "__main__":
    tiempos_insertion, tiempos_merge = ejecutar_experimento()
    generar_grafica(tiempos_insertion, tiempos_merge)

    print("\nExperimento terminado.")
    print("Gráfica guardada en graficas/parte4_tiempo.png")
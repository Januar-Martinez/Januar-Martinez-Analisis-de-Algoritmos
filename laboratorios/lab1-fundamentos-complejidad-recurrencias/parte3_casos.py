import time
import matplotlib.pyplot as plt
from pathlib import Path

CARPETA = Path(__file__).resolve().parent
CARPETA_GRAFICAS = CARPETA / "graficas"

from datos import (
    generar_aleatorio,
    generar_casi_ordenado,
    generar_inverso,
)

from algoritmos import insertion_sort

TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
SEMILLA = 42


def ejecutar_experimento():
    """Ejecuta el experimento de Insertion Sort.

    Returns:
        Diccionario con los tiempos y comparaciones de cada escenario.
    """

    resultados = {
        "Aleatorio": {
            "comparaciones": [],
            "tiempo": [],
        },
        "Casi ordenado": {
            "comparaciones": [],
            "tiempo": [],
        },
        "Inverso": {
            "comparaciones": [],
            "tiempo": [],
        },
    }

    for n in TAMANOS:

        escenarios = {
            "Aleatorio": generar_aleatorio(n, SEMILLA),
            "Casi ordenado": generar_casi_ordenado(n, SEMILLA),
            "Inverso": generar_inverso(n),
        }

        for nombre, datos in escenarios.items():

            inicio = time.perf_counter()

            _, comparaciones = insertion_sort(datos)

            fin = time.perf_counter()

            tiempo = fin - inicio

            resultados[nombre]["comparaciones"].append(comparaciones)
            resultados[nombre]["tiempo"].append(tiempo)

            print(
                f"{nombre:16} | "
                f"n={n:5} | "
                f"comparaciones={comparaciones:10} | "
                f"tiempo={tiempo:.8f} s"
            )

    return resultados


def generar_graficas(resultados):
    """Genera las gráficas de comparaciones y tiempos.

    Args:
        resultados: resultados obtenidos durante el experimento.
    """

    plt.figure()

    for nombre, datos in resultados.items():
        plt.plot(
            TAMANOS,
            datos["comparaciones"],
            marker="o",
            label=nombre,
        )

    plt.title("Insertion Sort - Comparaciones")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Número de comparaciones")
    plt.legend()
    plt.grid(True)

    plt.savefig(
        CARPETA_GRAFICAS / "parte3_comparaciones.png",
        dpi=300,
        bbox_inches="tight",
    )

    plt.close()

    plt.figure()

    for nombre, datos in resultados.items():
        plt.plot(
            TAMANOS,
            datos["tiempo"],
            marker="o",
            label=nombre,
        )

    plt.title("Insertion Sort - Tiempo de ejecución")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo (segundos)")
    plt.legend()
    plt.grid(True)

    plt.savefig(
        CARPETA_GRAFICAS / "parte3_tiempo.png",
        dpi=300,
        bbox_inches="tight",
    )

    plt.close()


if __name__ == "__main__":
    resultados = ejecutar_experimento()
    generar_graficas(resultados)

    print("\nExperimento terminado.")
    print("Graficas guardadas en la carpeta 'graficas/'.")

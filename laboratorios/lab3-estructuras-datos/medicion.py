
"""Medicion de busquedas en listas enlazadas y tablas hash."""

import random
import time
from pathlib import Path

import matplotlib.pyplot as plt

from estructuras import ListaEnlazada, TablaHash


CARPETA = Path(__file__).resolve().parent
CARPETA_GRAFICAS = CARPETA / "graficas"


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.
 
    Args:
        existentes: guias almacenadas en las estructuras.
        cantidad: cuantas guias inexistentes generar.
        semilla: semilla del generador, para reproducir la medicion.
 
    Returns:
        Una lista con `cantidad` guias que no pertenecen a `existentes`.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes


def es_primo(numero: int) -> bool:
    """Determina si un numero entero es primo.

    Args:
        numero: Numero que se va a comprobar.

    Returns:
        True si es primo, False en caso contrario.
    """
    if numero < 2:
        return False

    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 1

    return True


def primo_cercano(objetivo: int) -> int:
    """Encuentra el numero primo mas cercano al objetivo.

    Args:
        objetivo: Valor alrededor del cual se busca un primo.

    Returns:
        El numero primo mas cercano al objetivo.
    """
    distancia = 0

    while True:
        inferior = objetivo - distancia
        superior = objetivo + distancia

        if inferior >= 2 and es_primo(inferior):
            return inferior

        if distancia > 0 and es_primo(superior):
            return superior

        distancia += 1


def construir_estructuras(guias: list[int], estados: list[str], m: int) -> tuple[ListaEnlazada, TablaHash]:
    """Construye las estructuras con los mismos envios.

    Args:
        guias: Numeros de guia que se almacenaran.
        estados: Estados asociados a las guias.
        m: Numero de casillas de la tabla hash.

    Returns:
        La lista enlazada y la tabla hash construidas.
    """
    lista = ListaEnlazada()
    tabla = TablaHash(m)

    for guia, estado in zip(guias, estados):
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)

    return lista, tabla


def verificar_estructuras(lista: ListaEnlazada, tabla: TablaHash, guias: list[int]) -> None:
    """Comprueba que ambas estructuras devuelvan los mismos estados.

    Args:
        lista: Lista enlazada que se verificara.
        tabla: Tabla hash que se verificara.
        guias: Guias existentes que se utilizaran en la prueba.
    """
    for guia in guias[:10]:
        assert lista.buscar(guia) == tabla.buscar(guia), (
            f"Resultados diferentes para la guia {guia}"
        )


def medir_busquedas(estructura: ListaEnlazada | TablaHash, guias: list[int]) -> float:
    """Calcula el tiempo medio de una busqueda infructuosa.

    Args:
        estructura: Lista enlazada o tabla hash que se evaluara.
        guias: Guias que no existen en la estructura.

    Returns:
        Tiempo medio por busqueda, en segundos.
    """
    inicio = time.perf_counter()

    for guia in guias:
        assert estructura.buscar(guia) is None

    tiempo_total = time.perf_counter() - inicio
    return tiempo_total / len(guias)


def graficar_lista_vs_tabla(tamanos: list[int], tiempos_lista: list[float], tiempos_tabla: list[float]) -> None:
    """Grafica los tiempos medios de ambas estructuras.

    Args:
        tamanos: Cantidad de guias almacenadas.
        tiempos_lista: Tiempos medios de la lista enlazada.
        tiempos_tabla: Tiempos medios de la tabla hash.
    """
    CARPETA_GRAFICAS.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(10, 6))
    plt.plot(
        tamanos, tiempos_lista, marker="o",
        label="Lista enlazada",
    )
    plt.plot(
        tamanos, tiempos_tabla, marker="o",
        label="Tabla hash",
    )

    plt.title("Busqueda infructuosa: lista enlazada vs. tabla hash")
    plt.xlabel("Numero de guias almacenadas (n)")
    plt.ylabel("Tiempo medio por busqueda (segundos)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(CARPETA_GRAFICAS / "lista_vs_tabla.png")
    plt.close()


def experimento_a() -> None:
    """Compara los tiempos de busqueda de ambas estructuras."""

    tamanos = [100, 500, 1000, 5000, 20000, 50000]
    tiempos_lista: list[float] = []
    tiempos_tabla: list[float] = []

    azar = random.Random(42)
    guias_generadas = azar.sample(
        range(10**9, 10**10),
        max(tamanos),
    )
    estados_posibles = ["en bodega", "en reparto", "entregado"]
    estados_generados = [
        estados_posibles[azar.randrange(len(estados_posibles))]
        for _ in guias_generadas
    ]

    for n in tamanos:
        guias = guias_generadas[:n]
        estados = estados_generados[:n]

        m = primo_cercano(round(n / 2))
        lista, tabla = construir_estructuras(guias, estados, m)

        verificar_estructuras(lista, tabla, guias)

        inexistentes = generar_guias_inexistentes(
            set(guias), 200, semilla=7
        )

        tiempo_lista = medir_busquedas(lista, inexistentes)
        tiempo_tabla = medir_busquedas(tabla, inexistentes)

        tiempos_lista.append(tiempo_lista)
        tiempos_tabla.append(tiempo_tabla)

        print(
            f"n = {n:5d} | m = {m:5d} | "
            f"alfa = {tabla.factor_carga():.3f} | "
            f"Lista: {tiempo_lista:.8f} s | "
            f"Tabla: {tiempo_tabla:.8f} s"
        )

    graficar_lista_vs_tabla(
        tamanos, tiempos_lista, tiempos_tabla
    )

    print("Grafica guardada en graficas/lista_vs_tabla.png")


def graficar_tiempo_vs_alfa( factores: list[float], tiempos: list[float]) -> None:
    """Grafica el tiempo medio de busqueda frente al factor de carga.

    Args:
        factores: Factores de carga medidos.
        tiempos: Tiempos medios por busqueda en segundos.
    """
    CARPETA_GRAFICAS.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(10, 6))
    plt.plot(
        factores, tiempos, marker="o",
        label="Tabla hash",
    )

    plt.title("Efecto del factor de carga en las busquedas")
    plt.xlabel("Factor de carga (alfa = n / m)")
    plt.ylabel("Tiempo medio por busqueda (segundos)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(CARPETA_GRAFICAS / "tiempo_vs_alfa.png")
    plt.close()


def experimento_b() -> None:
    """Mide el efecto del factor de carga en la tabla hash."""
    n = 20000
    factores_objetivo = [0.5, 1, 4, 10]

    azar = random.Random(42)
    guias = azar.sample(range(10**9, 10**10), n)

    estados_posibles = ["en bodega", "en reparto", "entregado"]
    estados = [
        estados_posibles[azar.randrange(len(estados_posibles))]
        for _ in range(n)
    ]

    inexistentes = generar_guias_inexistentes(
        set(guias), 200, semilla=7
    )

    factores_medidos: list[float] = []
    tiempos: list[float] = []

    for alfa_objetivo in factores_objetivo:
        m = primo_cercano(round(n / alfa_objetivo))
        tabla = TablaHash(m)

        for guia, estado in zip(guias, estados):
            tabla.insertar(guia, estado)

        for guia, estado in zip(guias[:10], estados[:10]):
            assert tabla.buscar(guia) == estado

        tiempo = medir_busquedas(tabla, inexistentes)
        alfa = tabla.factor_carga()

        factores_medidos.append(alfa)
        tiempos.append(tiempo)

        print(
            f"n = {n} | m = {m:5d} | "
            f"alfa = {alfa:.3f} | "
            f"Tiempo medio: {tiempo:.8f} s"
        )

    graficar_tiempo_vs_alfa(factores_medidos, tiempos)

    print("Grafica guardada en graficas/tiempo_vs_alfa.png")


def main() -> None:
    """Ejecuta los dos experimentos de medicion."""
    
    experimento_a()
    print()
    experimento_b()


if __name__ == "__main__":
    main()

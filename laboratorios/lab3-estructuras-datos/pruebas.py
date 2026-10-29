
"""Pruebas para la lista enlazada y la tabla hash."""

import random

from estructuras import ListaEnlazada, TablaHash


# 1. Verificar busquedas en la lista enlazada.
lista = ListaEnlazada()
lista.insertar(1000000010, "en bodega")
lista.insertar(1000000024, "en reparto")

assert lista.buscar(1000000010) == "en bodega"
assert lista.buscar(1000000024) == "en reparto"
assert lista.buscar(9999999999) is None


# 2. Verificar busquedas en la tabla hash.
tabla = TablaHash(7)
tabla.insertar(1000000010, "en bodega")
tabla.insertar(1000000024, "en reparto")

assert tabla.buscar(1000000010) == "en bodega"
assert tabla.buscar(1000000024) == "en reparto"
assert tabla.buscar(9999999999) is None


# 3. Verificar una colision forzada.
tabla_colisiones = TablaHash(7)

for guia in (10, 24, 17):
    tabla_colisiones.insertar(guia, "en bodega")

assert tabla_colisiones.hash(10) == 3
assert tabla_colisiones.hash(24) == 3
assert tabla_colisiones.hash(17) == 3

assert tabla_colisiones.buscar(10) == "en bodega"
assert tabla_colisiones.buscar(24) == "en bodega"
assert tabla_colisiones.buscar(17) == "en bodega"
assert tabla_colisiones.casillas[3].tamano == 3
assert tabla_colisiones.factor_carga() == 3 / 7


# 4. Comparar ambas estructuras con 20 colecciones aleatorias.
generador = random.Random(42)
estados = ["en bodega", "en reparto", "entregado"]

for _ in range(20):
    cantidad = generador.randint(1, 50)
    guias = generador.sample(range(1000000000, 1000001000), cantidad)

    lista_aleatoria = ListaEnlazada()
    tabla_aleatoria = TablaHash(17)

    for guia in guias:
        estado = generador.choice(estados)
        lista_aleatoria.insertar(guia, estado)
        tabla_aleatoria.insertar(guia, estado)

    # Las guias existentes deben devolver el mismo estado.
    for guia in guias:
        assert lista_aleatoria.buscar(guia) == tabla_aleatoria.buscar(guia)

    # Las guias inexistentes deben devolver None en ambas.
    guias_inexistentes = generador.sample(
        range(2000000000, 2000001000), 10
    )

    for guia in guias_inexistentes:
        assert lista_aleatoria.buscar(guia) is None
        assert tabla_aleatoria.buscar(guia) is None


print("Todas las pruebas fueron superadas.")

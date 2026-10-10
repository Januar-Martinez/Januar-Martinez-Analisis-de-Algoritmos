
"""Pruebas de los algoritmos de subarreglo maximo."""

import random

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

serie = [-3, 5, -2, 8, -6, 3, 9, -4]

assert subarreglo_fuerza_bruta(serie)[2] == 17
assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 17

# Un solo elemento.
serie = [7]

assert subarreglo_fuerza_bruta(serie)[2] == 7
assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 7

# Todos los valores negativos.
serie = [-8, -3, -6, -2, -9]

assert subarreglo_fuerza_bruta(serie)[2] == -2
assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == -2

# Todos los valores positivos.
serie = [2, 4, 1, 5]

assert subarreglo_fuerza_bruta(serie)[2] == 12
assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 12

# El mejor tramo cruza el punto medio.
serie = [4, -1, 3, 5, -2]

assert subarreglo_fuerza_bruta(serie)[2] == 11
assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 11

# Cien listas aleatorias.
random.seed(42)

for _ in range(100):
    longitud = random.randint(1, 50)
    serie = [
        random.randint(-20, 20)
        for _ in range(longitud)
    ]

    suma_fuerza_bruta = subarreglo_fuerza_bruta(serie)[2]
    suma_divide_venceras = subarreglo_maximo(
        serie, 0, len(serie) - 1
    )[2]

    assert suma_fuerza_bruta == suma_divide_venceras, (
        f"Resultados diferentes para la serie: {serie}"
    )

print("Todas las pruebas pasaron correctamente.")

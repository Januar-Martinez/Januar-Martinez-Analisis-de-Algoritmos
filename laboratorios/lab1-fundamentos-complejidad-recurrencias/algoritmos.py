"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""
 
 
def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.
 
    No modifica la lista recibida: trabaja sobre una copia.
 
    Args:
        datos: lista de indices de riesgo a ordenar.
 
    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    datos = datos.copy()
    comparaciones = 0
    n = len(datos)
    for i in range(1, n):
        clave = datos[i]
        j = i - 1
        while j >= 0:
            comparaciones += 1
            if datos[j] >= clave:
                break
            datos[j + 1] = datos[j]
            j -= 1
        datos[j + 1] = clave
    return datos, comparaciones

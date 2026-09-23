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

def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla.
 
    No modifica la lista recibida: trabaja sobre una copia.
 
    Args:
        datos: lista de indices de riesgo a ordenar.
 
    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    datos = datos.copy()

    if len(datos) <= 1:
        return datos, 0

    mitad = len(datos) // 2

    izquierda, comparaciones_izquierda = merge_sort(datos[:mitad])
    derecha, comparaciones_derecha = merge_sort(datos[mitad:])

    resultado, comparaciones_merge = merge(izquierda, derecha)

    comparaciones = ( comparaciones_izquierda + comparaciones_derecha + comparaciones_merge )

    return resultado, comparaciones

def merge( izquierda: list[int], derecha: list[int], ) -> tuple[list[int], int]:
    """Combina dos listas ordenadas de mayor a menor.

    Args:
        izquierda: lista ordenada de mayor a menor.
        derecha: lista ordenada de mayor a menor.

    Returns:
        Una tupla con la lista combinada y el numero de comparaciones.
    """
    resultado = []
    comparaciones = 0
    i = 0
    j = 0

    while i < len(izquierda) and j < len(derecha):
        comparaciones += 1

        if izquierda[i] >= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado, comparaciones
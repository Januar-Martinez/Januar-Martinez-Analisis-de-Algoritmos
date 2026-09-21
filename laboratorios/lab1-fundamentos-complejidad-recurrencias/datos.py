"""Generadores de lotes de registros para los escenarios de Tamiza."""
 
 
def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote de n registros en orden aleatorio (escenario A).
 
    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio, para que el
            experimento sea reproducible.
 
    Returns:
        Lista de n indices de riesgo enteros distintos, desordenada.
    """
    datos_aleatorio = list(range(n))

    generador = random.Random(semilla)
    generador.shuffle(datos_aleatorio)

    return datos_aleatorio
 
 
def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote casi ordenado: 98% ordenado y 2% al final (escenario B).
 
    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio.
 
    Returns:
        Lista de n indices de riesgo enteros distintos, con el primer
        98% en el orden que el algoritmo produce y el 2% restante
        desordenado al final.
    """
    datos_casi_ordenado = list(range(n - 1, -1, -1))

    cantidad_ordenada = int(n * 0.98)

    parte_ordenada = datos_casi_ordenado[:cantidad_ordenada]
    parte_nueva = datos_casi_ordenado[cantidad_ordenada:]

    generador = random.Random(semilla)
    generador.shuffle(parte_nueva)

    return parte_ordenada + parte_nueva
 
 
def generar_inverso(n: int) -> list[int]:
    """Genera un lote en el orden exactamente contrario (escenario C).
 
    Args:
        n: cantidad de registros del lote.
 
    Returns:
        Lista de n indices de riesgo enteros distintos, en el orden
        inverso al que el algoritmo debe producir.
    """
    return list(range(n))
# Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias

## Parte 1 — Analizar el algoritmo antes de comprar hardware

La Secretaría está por firmar la compra de un servidor del doble de velocidad para que el proceso de Tamiza quepa en la ventana de cuatro horas. 

### ¿Por qué debe analizarse primero el algoritmo, si el que está en producción lleva ocho años entregando el resultado correcto?

Un algoritmo funciona correctamente cuando cumple con la finalidad con la que se planteo y un algoritmo es eficiente cuando cumple con esa finalidad planteada en un tiempo determinado, en el caso de Tamiza no esta cumpliendo con la eficiencia ya que el algoritmo no culmina su proceso en la ventana de 4 horas.

Duplicar la velocidad del servidor sin antes analizar el algoritmo puede ser un error, ya que si el algoritmo está mal optimizado puede seguir ocurriendo que se incumpla la restricción.

**Otro ejemplo** es una empresa que procesa la cantidad de llamadas que hace cada cliente durante el día, esto puede llegar a ser mas de 2 millones de datos. Este proceso se debe hacer en una ventana de 8 horas, pero el algoritmo, aunque funciona bien no cumple con el proceso en la ventana requerida.

## Parte 2 — Responsabilidad ambiental y ética de la implementación

### Como responsable técnico de Tamiza, ¿qué responsabilidad ambiental y ética asume al decidir qué algoritmo de ordenamiento se ejecuta cada madrugada sobre los datos de 1.200.000 pacientes?

Debido a que se tiene un servidor corriendo el proceso eso se traduce en consumo de energía, y el hecho de que sea un proceso programado para todas las madrugadas implica que el consuma de energía es mayor.

La lentitud del programa afecta a el centro de contacto, ya que al iniciar la jornada no cuentan con la lista completa para realizar las llamadas, en este caso el equipo de desarrollo debe asumir el costo del error ya que debió al mal funcionamiento del programa están perjudicando al centro de contacto. También se ven afectados los pacientes, debido a que puede ocurrir que no sean llamados debido a un error humano de un operador del centro de contacto por hecho de que son demasiados datos, aquí la secretaria debe asumir el costo del error ya que es la responsable principal de que los pacientes sean atendidos de la mejor manera.

Es importante que el ordenamiento sea adecuado ya que de eso depende a quien llamar primero y es delicado ya que el llamado es por índice de riesgo.

## Parte 3 — Peor caso, mejor caso y caso promedio, demostrados en Python

### 3.1 — Explicación

 - El **mejor caso** se da cuando los 1.200.000 registros vienen ya ordenados por índice de riegos de mayor a menor, el **caso promedio**  se cuando vienen ordenados de manera totalmente al azar y el **peor caso** cuando los registro vienen ordenados de menor a mayor riesgo.
 - Para decidir si el algoritmo Tamiza entra en producción hay que usar el peor caso, porque es donde mas se va demorar el algoritmo en realizar el proceso.
 - Predicción: El escenario **A — Aleatorio** = caso promedio, el escenario **B — Casi ordenado** = mejor caso y el escenario **C — Orden inverso** = el peor caso.

### 3.2 — Demostración experimental
#### Comparaciones

![Comparaciones vs tamaño de entrada](graficas/parte3_comparaciones.png)

#### Tiempo de ejecución

![Tiempo vs tamaño de entrada](graficas/parte3_tiempo.png)

- El escenario C – orden inverso resulto siendo el peor caso, el escenario B – casi ordenado el mejor y el escenario A – aleatorio el que se aproxima al promedio.
- Esto coincide al 100% con mi predicción.

## Parte 4 — Complejidad de merge sort e insertion sort: cálculo y validación

### 4.1 — Cálculo teórico

#### Planteamiento de la recurrencia de Merge Sort y resolución por método de sustitución

$$
T(n)=2T\left(\frac{n}{2}\right)+O(n)
$$

- $2T(n/2)$ = costo de la recursividad.
- $O(n)$ = hace referencia a una función de costo lineal.

#### Método de sustitución

Partimos de:

$$
T(n)=2T\left(\frac{n}{2}\right)+O(n)
$$

Reemplazamos $O(n)$ por $cn$:

$$
T(n)=2T\left(\frac{n}{2}\right)+cn
$$

**Hipótesis:**

$$
T(n)\leq cn\log n
$$

Entonces:

$$
T\left(\frac{n}{2}\right)
\leq
c\frac{n}{2}\log\left(\frac{n}{2}\right)
$$

Sustituimos:

$$
T(n)
\leq
2\left[
c\frac{n}{2}\log\left(\frac{n}{2}\right)
\right]+cn
$$

Simplificando:

$$
T(n)
\leq
cn\log\left(\frac{n}{2}\right)+cn
$$

Por lo tanto:

$$
T(n)
\leq
cn(\log n-\log 2)+cn
$$

Entonces:

$$
T(n)
\leq
cn\log n-cn\log 2+cn
$$

Como $\log_2 2=1$:

$$
T(n)
\leq
cn\log n-cn+cn
$$

Finalmente:

$$
T(n)\leq cn\log n
$$

Por lo tanto:

$$
\boxed{T(n)=O(n\log n)}
$$

---

### Cota manual de Insertion Sort

La expresión de la complejidad es:

$$
T(n) = C_1n + C_2(n-1) + C_3(n-1) + C_4\sum_{i=1}^{n-1}(t_i+1) + C_5\sum_{i=1}^{n-1}t_i + C_6\sum_{i=1}^{n-1}t_i + C_7(n-1)
$$

Agrupando términos:

$$
T(n) = C_1n + (n-1)(C_2+C_3+C_4+C_7) + (C_4+C_5+C_6) \sum_{i=1}^{n-1}t_i
$$

En el peor caso, los datos están en **orden inverso**:

$$
t_i=i
$$

Por lo tanto:

$$
\sum_{i=1}^{n-1}i = \frac{n(n-1)}{2}
$$

Sustituimos:

$$
T(n) = C_1n + (C_2+C_3+C_4+C_7)(n-1) + (C_4+C_5+C_6) \frac{n^2-n}{2}
$$

El término dominante es:

$$
n^2
$$

Por lo tanto:

$$
\boxed{T(n)=O(n^2)}
$$

---

### Complejidad esperada de cada algoritmo

| Algoritmo | Mejor caso | Caso promedio | Peor caso |
|---|---|---|---|
| **Insertion Sort** | $O(n)$ | $O(n^2)$ | $O(n^2)$ |
| **Merge Sort** | $O(n\log n)$ | $O(n\log n)$ | $O(n\log n)$ |
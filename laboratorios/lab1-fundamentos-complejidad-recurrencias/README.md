# Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias

## Parte 1 — Analizar el algoritmo antes de comprar hardware

La Secretaría está por firmar la compra de un servidor del doble de velocidad para que el proceso de Tamiza quepa en la ventana de cuatro horas. 

### **¿Por qué debe analizarse primero el algoritmo, si el que está en producción lleva ocho años entregando el resultado correcto?**

Un algoritmo funciona correctamente cuando cumple con la finalidad con la que se planteo y un algoritmo es eficiente cuando cumple con esa finalidad planteada en un tiempo determinado, en el caso de Tamiza no esta cumpliendo con la eficiencia ya que el algoritmo no culmina su proceso en la ventana de 4 horas.

Duplicar la velocidad del servidor sin antes analizar el algoritmo puede ser un error, ya que si el algoritmo está mal optimizado puede seguir ocurriendo que se incumpla la restricción.

**Otro ejemplo** es una empresa que procesa la cantidad de llamadas que hace cada cliente durante el día, esto puede llegar a ser mas de 2 millones de datos. Este proceso se debe hacer en una ventana de 8 horas, pero el algoritmo, aunque funciona bien no cumple con el proceso en la ventana requerida.
# 1. Qué es programar y qué es Python

## De una tarea a instrucciones precisas

Programar consiste en describir instrucciones que un ordenador puede ejecutar. Un programa recibe datos, aplica operaciones y produce un resultado. No deduce lo que querías decir: hace lo que has indicado, dentro de las reglas del lenguaje.

Imagina una papelería que vende 3 cuadernos a 4 euros. Antes de pensar en código, escribe los pasos:

1. Conocer cuántos cuadernos se venden.
2. Conocer el precio de cada cuaderno.
3. Multiplicar cantidad por precio.
4. Mostrar el importe.

Esa secuencia es un **algoritmo**: una forma precisa de resolver el problema. Podemos expresarla en castellano, mediante un diagrama o con un lenguaje de programación.

## Un lenguaje para expresar el algoritmo

Un lenguaje de programación define una sintaxis —cómo se escribe— y una semántica —qué significa lo escrito—. Python es uno de esos lenguajes. Su código es texto y utiliza palabras como `if`, `for` o `import`, aunque los nombres y los mensajes de nuestro programa pueden estar en castellano.

```python
cantidad = 3
precio = 4
importe = cantidad * precio
print(importe)
```

Resultado esperado:

```text
12
```

Lee el programa de arriba abajo. `cantidad` y `precio` son nombres asociados a valores; `=` realiza una asignación; `*` multiplica; `print(...)` muestra el resultado. No tienes que memorizar estos símbolos todavía. Los practicarás después.

**Un programa puede funcionar y calcular algo incorrecto.** Si escribes `cantidad + precio`, Python mostrará `7` sin dar un error. Por eso debemos comprobar el resultado con un ejemplo que entendamos.

## Para qué usaremos Python

En este curso empezaremos con cálculos y mensajes, después procesaremos pequeñas colecciones y finalmente trabajaremos con tablas. Leer un CSV, filtrar pedidos o resumir ventas son aplicaciones de los mismos fundamentos.

Python es un lenguaje de propósito general. Pandas es una biblioteca que añade herramientas para tablas; no necesitas Pandas para tu primer programa. Un CSV es un archivo de datos, no un programa. Un notebook permite reunir explicaciones y código, pero tampoco es el lenguaje.

## Actividad sin ordenador

Escribe los pasos para calcular cuánto cuestan 5 entradas a 8 euros, con un descuento fijo de 3 euros sobre el total. Comprueba a mano el resultado. Después cambia solo el número de entradas a 2.

**Comprobación:** debes obtener 37 y 13 euros. ¿En qué paso aplicaste el descuento? ¿Qué ocurriría si lo restases al precio de cada entrada?

Consulta: [introducción oficial a Python](https://docs.python.org/3/tutorial/introduction.html) y [primeros pasos en VS Code](https://code.visualstudio.com/docs/python/python-quick-start).

[Anterior: índice](README.md) · [Siguiente: las herramientas](02-herramientas.md)

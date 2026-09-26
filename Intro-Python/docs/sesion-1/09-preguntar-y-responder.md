# 9 · Preguntar y responder

[Inicio](../README.md) › [Sesión 1](README.md) › Preguntar y responder

**Tiempo aproximado:** 10 minutos

## Un programa que sirva para cualquier producto

Nuestro programa de margen funciona, pero solo para el Sofá Aurora. Si Marta quiere calcular el margen de otro producto, tiene que abrir el código y cambiar los números. Sería mejor que el programa **le preguntara** los datos.

## `input`: preguntar al usuario

`input()` muestra una pregunta en la terminal, **espera** a que la persona escriba algo y pulse Intro, y devuelve lo que ha escrito.

> **Pruébalo.** Crea `saludo.py`:
>
> ```python
> nombre = input("¿Cómo te llamas? ")
> tienda = input("¿En qué tienda de FraSoHome compras? ")
> print("Hola,", nombre)
> print("Te esperamos en FraSoHome", tienda)
> ```
>
> Ejecútalo y **responde en la terminal**, abajo. El programa se queda esperando hasta que escribas algo y pulses Intro.

> **Cuidado.** Cuando un programa usa `input`, parece que "no hace nada". En realidad está esperando tu respuesta. Haz clic en la terminal y escribe.

## La trampa: `input` siempre devuelve texto

Vamos a pedir una cantidad y a calcular el importe:

```python
unidades = input("¿Cuántos Cuadro Atlas quieres? ")
precio = 31.63
print(unidades * precio)
```

Si lo ejecutas y escribes `2`, Python **se queja** con un error (`TypeError`). ¿Por qué? Porque `input` siempre devuelve **texto**. Lo que escribiste no es el número 2, sino el texto `"2"`, y Python no sabe multiplicar un texto por un decimal.

La solución es **convertir** el texto en número:

| Función | Convierte a... | Ejemplo | Resultado |
|---|---|---|---|
| `int()` | Número entero | `int("2")` | `2` |
| `float()` | Número decimal | `float("31.63")` | `31.63` |
| `str()` | Texto | `str(2)` | `"2"` |

```python
unidades = int(input("¿Cuántos Cuadro Atlas quieres? "))
precio = 31.63
print(unidades * precio)
```

Ahora sí funciona. Lee la primera línea de dentro hacia fuera: primero `input` pregunta, luego `int` convierte la respuesta en número y, al final, se guarda en `unidades`.

> **Idea clave.** Lo que llega de fuera del programa (lo que escribe una persona, lo que se lee de un archivo) suele llegar como **texto**. Convertirlo al tipo correcto es una de las tareas más habituales al trabajar con datos.

## f-strings: mensajes bien presentados

Con `round()` ya evitamos resultados como `78.52000000000001`, pero los mensajes con varias comas quedan poco naturales. Para presentar resultados como en un informe usaremos las **f-strings**: textos con una `f` delante en los que puedes meter variables entre llaves `{}`. Además, redondean solo **al mostrar**, sin cambiar el valor guardado.

```python
producto = "Sofá Aurora 160cm"
margen = 221.99 - 143.47
print(f"El margen del {producto} es {margen:.2f} euros")
```

```text
El margen del Sofá Aurora 160cm es 78.52 euros
```

| Lo que escribes | Qué hace |
|---|---|
| `f"..."` | Avisa a Python de que dentro hay variables que tiene que sustituir |
| `{producto}` | Pone ahí el valor de la variable `producto` |
| `{margen:.2f}` | Pone el valor de `margen` **con 2 decimales** |
| `{margen_pct:.1f}` | Lo mismo, con 1 decimal |

> **Cuidado.** Si olvidas la `f` delante de las comillas, Python mostrará literalmente `{producto}` en lugar del nombre del producto.

## Todo junto

> **Pruébalo.** Crea `margen_pregunta.py`, un programa que pregunte los datos de cualquier producto y calcule el margen:
>
> ```python
> producto = input("Nombre del producto: ")
> precio_venta = float(input("Precio de venta (usa punto decimal): "))
> coste_unitario = float(input("Coste unitario (usa punto decimal): "))
>
> margen = precio_venta - coste_unitario
> margen_pct = margen / precio_venta * 100
>
> print(f"{producto}: margen de {margen:.2f} euros ({margen_pct:.1f} % del precio)")
> ```
>
> Pruébalo con el **Sofá Aurora 160cm** (221.99 y 143.47). Debe decir `margen de 78.52 euros (35.4 % del precio)`.

> **Pruébalo. Rompe algo a propósito.** Ejecuta el programa y, cuando te pida el precio, escribe `221,99` **con coma**. Después vuelve a ejecutarlo y escribe `mucho`. En los dos casos Python se detiene con un error `ValueError`: no sabe convertir esos textos en números. En el [apartado 11](11-cuando-algo-falla.md) verás cómo leer estos mensajes.

Puedes comparar con el ejemplo [03_saludo.py](ejemplos/03_saludo.py).

---

[← Anterior: Tipos de datos y variables](08-tipos-de-datos-y-variables.md) · [Índice de la sesión](README.md) · [Siguiente: Tomar decisiones →](10-tomar-decisiones.md)

# 1 · Listas, diccionarios y bucles

[Inicio](../README.md) › [Sesión 2](README.md) › Listas, diccionarios y bucles

**Tiempo aproximado:** 25 minutos

## La pregunta de Marta

> *"Está muy bien lo del stock, pero yo no tengo un producto: tengo cientos. ¿Tengo que ejecutar el programa una vez por cada uno?"*

No. Hasta ahora cada variable guardaba **un solo dato**. Ahora vamos a aprender a guardar **muchos datos juntos** y a **repetir** una tarea para cada uno de ellos.

## Listas: varios valores en orden

Una **lista** guarda varios valores en un orden concreto. Se escribe entre corchetes `[ ]`, con los valores separados por comas:

```python
categorias = ["Muebles", "Decoración", "Iluminación", "Textil hogar"]
```

Son las cuatro categorías de productos de FraSoHome. Algunas cosas que puedes hacer con una lista:

| Quiero... | Escribo | Resultado |
|---|---|---|
| Saber cuántos elementos tiene | `len(categorias)` | `4` |
| Ver el primer elemento | `categorias[0]` | `"Muebles"` |
| Ver el segundo | `categorias[1]` | `"Decoración"` |
| Ver el último | `categorias[-1]` | `"Textil hogar"` |
| Añadir uno al final | `categorias.append("Jardín")` | La lista pasa a tener 5 elementos |
| Sumar una lista de números | `sum([2, 1, 1])` | `4` |

> **Cuidado.** En Python **se empieza a contar desde 0**. El primer elemento es el `[0]`, el segundo el `[1]`... Al principio cuesta; en una semana lo harás sin pensar.

## Bucles `for`: repetir para cada elemento

Un **bucle** repite un bloque de instrucciones. El bucle `for` lo repite **una vez para cada elemento** de una lista:

```python
categorias = ["Muebles", "Decoración", "Iluminación", "Textil hogar"]

for categoria in categorias:
    print("Categoría:", categoria)
```

```text
Categoría: Muebles
Categoría: Decoración
Categoría: Iluminación
Categoría: Textil hogar
```

Léelo así: *"para cada `categoria` de la lista `categorias`, muestra la categoría"*. En cada vuelta, la variable `categoria` toma el valor del siguiente elemento.

Como en el `if`, la línea del `for` termina en **dos puntos** y lo que se repite va **sangrado**.

> **Pruébalo.** Añade una línea **sin sangría** después del bucle: `print("Fin del catálogo")`. ¿Cuántas veces se muestra? ¿Y si le pones sangría?

## Diccionarios: fichas con etiquetas

Una lista está bien para valores del mismo tipo, pero un producto tiene **varios datos distintos**: código, nombre, categoría, precio... Para eso existen los **diccionarios**, que se escriben entre llaves `{ }` y guardan pares **clave: valor**:

```python
producto = {
    "id": "P1001",
    "nombre": "Cuadro Atlas",
    "categoria": "Decoración",
    "precio_venta": 31.63,
}
```

Es como una **ficha de producto**: cada dato tiene una etiqueta (la clave) y un contenido (el valor). Para consultar un dato, usas su clave entre corchetes:

```python
print(producto["nombre"])         # Cuadro Atlas
print(producto["precio_venta"])   # 31.63
```

## Listas de diccionarios: ¡una tabla!

Y ahora juntamos las dos ideas. Una **lista de fichas** de producto:

```python
catalogo = [
    {"nombre": "Cuadro Atlas", "precio_venta": 31.63},
    {"nombre": "Sábana Nórdico 140x200", "precio_venta": 103.97},
    {"nombre": "Sofá Aurora 160cm", "precio_venta": 221.99},
]
```

Si lo piensas, esto es **una tabla**: cada diccionario es una fila y cada clave es una columna.

| nombre | precio_venta |
|---|---|
| Cuadro Atlas | 31.63 |
| Sábana Nórdico 140x200 | 103.97 |
| Sofá Aurora 160cm | 221.99 |

> **Idea clave.** Casi todos los datos de una empresa son tablas: filas (productos, clientes, ventas) con columnas (nombre, precio, fecha). Lo que acabas de escribir a mano es, en pequeño, lo mismo que manejarás cuando trabajes con datos reales.

Ahora podemos recorrer la tabla y **decidir para cada fila**:

```python
for p in catalogo:
    if p["precio_venta"] > 100:
        print(f"{p['nombre']}: {p['precio_venta']:.2f} euros (más de 100)")
    else:
        print(f"{p['nombre']}: {p['precio_venta']:.2f} euros")
```

```text
Cuadro Atlas: 31.63 euros
Sábana Nórdico 140x200: 103.97 euros (más de 100)
Sofá Aurora 160cm: 221.99 euros (más de 100)
```

> **Cuidado.** Dentro de una f-string con comillas dobles `"..."`, las claves del diccionario se escriben con comillas **simples**: `{p['nombre']}`. Si usas las mismas comillas por dentro y por fuera, Python puede confundirse.

## El acumulador: sumar mientras recorres

Una tarea muy habitual es **ir sumando** mientras recorres una lista. Por ejemplo, el valor total del catálogo:

```python
total = 0                          # 1. Antes del bucle: empieza en cero

for p in catalogo:
    total = total + p["precio_venta"]   # 2. En cada vuelta: suma el precio

print(f"Suma de precios: {total:.2f} euros")   # 3. Después del bucle: muestra el total
```

```text
Suma de precios: 357.59 euros
```

Esta estructura (**empezar en cero → sumar en cada vuelta → mostrar al final**) se llama **acumulador** y la usarás constantemente.

> **Pruébalo.**
>
> 1. Añade al catálogo la **Alfombra Zen 200x300**, que cuesta 112,47 €. ¿Cuánto suman ahora los precios?
> 2. Crea un segundo acumulador, `caros`, que **cuente** cuántos productos cuestan más de 100 €. Pista: empieza en `0` y súmale `1` cuando se cumpla la condición.

<details markdown>
<summary>Ver solución</summary>

```python
catalogo = [
    {"nombre": "Cuadro Atlas", "precio_venta": 31.63},
    {"nombre": "Sábana Nórdico 140x200", "precio_venta": 103.97},
    {"nombre": "Sofá Aurora 160cm", "precio_venta": 221.99},
    {"nombre": "Alfombra Zen 200x300", "precio_venta": 112.47},
]

total = 0
caros = 0

for p in catalogo:
    total = total + p["precio_venta"]
    if p["precio_venta"] > 100:
        caros = caros + 1

print(f"Suma de precios: {total:.2f} euros")
print(f"Productos de más de 100 euros: {caros}")
```

```text
Suma de precios: 470.06 euros
Productos de más de 100 euros: 3
```

</details>

## Un paso más: `range`, mutabilidad y otras colecciones

### Repetir un número de veces: `range`

A veces no quieres recorrer una lista, sino repetir algo **un número de veces**. `range(inicio, fin)` genera los números desde `inicio` hasta `fin`, **sin incluir** `fin`:

```python
for dia in range(1, 4):
    print("Revisión de stock, día", dia)
```

```text
Revisión de stock, día 1
Revisión de stock, día 2
Revisión de stock, día 3
```

### Mutable e inmutable

En la [sesión 1](../sesion-1/08-tipos-de-datos-y-variables.md) viste que una variable es una **etiqueta** que apunta a un valor en memoria. Con las listas esto tiene una consecuencia importante:

```python
precios = [31.63, 103.97, 221.99]
copia = precios          # ¡no copia la lista! Pega otra etiqueta a la MISMA lista
copia.append(112.47)
print(precios)
```

```text
[31.63, 103.97, 221.99, 112.47]
```

Hemos añadido el precio a `copia`... y ha aparecido también en `precios`. Las dos variables son **dos etiquetas pegadas a la misma lista**. Si quieres una copia independiente, tienes que pedirla: `copia = precios.copy()`.

Esto ocurre porque las listas y los diccionarios son **mutables**: se pueden modificar después de crearlos. Los números, los textos y los booleanos son **inmutables**: no se pueden modificar. Cualquier operación sobre ellos crea un valor **nuevo**. Por eso `"Madrid".upper()` no cambia el texto original, sino que devuelve otro.

| Tipo | ¿Mutable? |
|---|---|
| `int`, `float`, `bool`, `str`, `tuple` | No |
| `list`, `dict`, `set` | Sí |

> **Cuidado.** Este comportamiento es fuente de errores muy difíciles de encontrar. Cuando modifiques una lista y "algo cambie solo" en otro sitio, piensa en las etiquetas.

### Otras dos colecciones que verás

| Colección | Se escribe | Característica | Ejemplo |
|---|---|---|---|
| **Tupla** (`tuple`) | `( )` | Como una lista, pero **inmutable**. Para datos que no deben cambiar | `tienda = ("S001", "Madrid Centro")` |
| **Conjunto** (`set`) | `{ }` sin claves | **Sin orden y sin duplicados**. Para saber qué valores distintos hay | `{"Decoración", "Muebles", "Decoración"}` tiene 2 elementos |

### Funciones útiles con listas

| Función | Qué hace | Ejemplo con `[31.63, 103.97, 221.99]` |
|---|---|---|
| `sum()` | Suma los elementos | `357.59` (aprox.) |
| `max()` / `min()` | El mayor / el menor | `221.99` / `31.63` |
| `sorted()` | Devuelve una copia ordenada | `[31.63, 103.97, 221.99]` |
| `in` | ¿Está este valor en la lista? | `103.97 in precios` da `True` |

Puedes comparar con el ejemplo [01_catalogo.py](ejemplos/01_catalogo.py).

---

[Índice de la sesión](README.md) · [Siguiente: Funciones y módulos →](02-funciones-y-modulos.md)

# 2 · Funciones y módulos

[Inicio](../README.md) › [Sesión 2](README.md) › Funciones y módulos

**Tiempo aproximado:** 20 minutos

## La pregunta de Marta

> *"Todo el día hago los mismos cálculos: cantidad por precio, aplicar un descuento, calcular el margen... ¿No podríamos tenerlos preparados para usarlos cuando haga falta?"*

Sí. Para eso sirven las **funciones**.

## Ya conoces algunas funciones

Sin darte cuenta, llevas desde la sesión 1 usando funciones: `print()`, `input()`, `int()`, `float()`, `len()`, `sum()`, `type()`... Todas siguen el mismo patrón:

- Tienen un **nombre**.
- Reciben datos **entre paréntesis**.
- Hacen un trabajo y, muchas veces, **devuelven un resultado**.

```python
len(["Muebles", "Decoración"])   # recibe una lista, devuelve 2
```

Ahora vas a crear **las tuyas**.

## Crear una función

```python
def calcular_importe(cantidad, precio):
    """Devuelve cantidad x precio."""
    return cantidad * precio
```

| Parte | Qué es |
|---|---|
| `def` | Palabra que significa "voy a **def**inir una función" |
| `calcular_importe` | El nombre que le das. Mismas reglas que las variables |
| `(cantidad, precio)` | Los **parámetros**: los datos que la función necesita recibir |
| `:` y sangría | Como en `if` y `for`, el cuerpo de la función va sangrado |
| `"""Devuelve..."""` | Una descripción opcional de lo que hace. Es buena costumbre |
| `return` | El **resultado** que la función devuelve a quien la llamó |

Definir una función **no la ejecuta**. Es como escribir una receta en el cuaderno: la tienes preparada, pero todavía no has cocinado nada. Para usarla, la **llamas** por su nombre y le das los datos:

```python
importe = calcular_importe(2, 31.63)
print(f"2 Cuadro Atlas: {importe:.2f} euros")
```

```text
2 Cuadro Atlas: 63.26 euros
```

Al llamar a `calcular_importe(2, 31.63)`, Python entra en la función con `cantidad = 2` y `precio = 31.63`, calcula `2 * 31.63` y **devuelve** `63.26`, que se guarda en la variable `importe`.

## Funciones que usan otras funciones

```python
def aplicar_descuento(importe, descuento_pct):
    """Devuelve el importe después de aplicar un descuento en %."""
    return importe * (1 - descuento_pct / 100)


importe = calcular_importe(2, 31.63)
con_descuento = aplicar_descuento(importe, 10)
print(f"Con un 10 % de descuento: {con_descuento:.2f} euros")
```

```text
Con un 10 % de descuento: 56.93 euros
```

Cada función hace **una cosa** y tiene un nombre que dice **qué hace**. El programa final se lee casi como una frase: *calcula el importe, aplícale el descuento y muéstralo*.

> **Idea clave.** Una buena función es como un buen empleado: tiene una tarea clara, sabe qué necesita para hacerla y entrega un resultado.

## `print` o `return`: la diferencia importa

Estas dos funciones parecen iguales, pero no lo son:

```python
def importe_con_print(cantidad, precio):
    print(cantidad * precio)


def importe_con_return(cantidad, precio):
    return cantidad * precio
```

| | `print` | `return` |
|---|---|---|
| Qué hace | **Muestra** el resultado en pantalla | **Entrega** el resultado a quien llamó a la función |
| ¿Puedo guardarlo en una variable y seguir calculando? | **No.** La variable se queda vacía (`None`) | **Sí** |
| Analogía | Decir el resultado en voz alta | Dártelo por escrito para que lo uses |

> **Pruébalo.** Escribe las dos funciones y ejecuta:
>
> ```python
> a = importe_con_print(2, 31.63)
> b = importe_con_return(2, 31.63)
> print("a vale:", a)
> print("b vale:", b)
> ```
>
> **Predice** antes de ejecutar: ¿qué valdrá `a`? ¿Y `b`?

<details markdown>
<summary>Ver explicación</summary>

```text
63.26
a vale: None
b vale: 63.26
```

`importe_con_print` muestra `63.26` en pantalla, pero **no devuelve nada**. Por eso `a` vale `None`, que en Python significa "nada". `importe_con_return` no muestra nada, pero devuelve el valor, que queda guardado en `b`.

Regla práctica: las funciones que **calculan** usan `return`. El `print` se deja para el final, cuando quieres enseñar el resultado.

</details>

> **Pruébalo.** Escribe una función `calcular_margen(precio_venta, coste_unitario)` que devuelva el margen en euros. Úsala para calcular el margen del **Sofá Aurora 160cm** (221,99 y 143,47) y el del **Cuadro Atlas** (31,63 y 21,79).

<details markdown>
<summary>Ver solución</summary>

```python
def calcular_margen(precio_venta, coste_unitario):
    """Devuelve el margen en euros de un producto."""
    return precio_venta - coste_unitario


margen_sofa = calcular_margen(221.99, 143.47)
margen_cuadro = calcular_margen(31.63, 21.79)

print(f"Sofá Aurora 160cm: {margen_sofa:.2f} euros")
print(f"Cuadro Atlas: {margen_cuadro:.2f} euros")
```

```text
Sofá Aurora 160cm: 78.52 euros
Cuadro Atlas: 9.84 euros
```

</details>

Puedes comparar con el ejemplo [02_funciones.py](ejemplos/02_funciones.py).

## Miniproyecto: el ticket de Madrid Centro

Ya tienes todas las piezas para el primer programa "de verdad" para Marta.

> **Pruébalo (en parejas, 10 minutos).** Un cliente de **FraSoHome Madrid Centro** se lleva:
>
> | Producto | Cantidad | Precio unitario |
> |---|---|---|
> | Cuadro Atlas | 2 | 31,63 € |
> | Sábana Nórdico 140x200 | 1 | 103,97 € |
> | Sofá Aurora 160cm | 1 | 221,99 € |
>
> Escribe un programa `ticket.py` que:
>
> 1. Guarde el ticket como una **lista de diccionarios** con las claves `producto`, `cantidad` y `precio`.
> 2. Use la función `calcular_importe(cantidad, precio)`.
> 3. **Recorra** el ticket y muestre cada línea con su importe con dos decimales.
> 4. **Acumule** el total de unidades y el total en euros, y los muestre al final.
>
> Resultado esperado:
>
> ```text
> FraSoHome Madrid Centro
> 2 x Cuadro Atlas: 63.26 euros
> 1 x Sábana Nórdico 140x200: 103.97 euros
> 1 x Sofá Aurora 160cm: 221.99 euros
> Unidades: 4
> Total: 389.22 euros
> ```
>
> Después, **comprueba dos casos límite**: ¿qué muestra tu programa si el ticket está vacío (`ticket = []`)? ¿Y si el cliente se lleva 4 cuadros en lugar de 2?

<details markdown>
<summary>Ver solución</summary>

```python
def calcular_importe(cantidad, precio):
    """Devuelve cantidad x precio."""
    return cantidad * precio


ticket = [
    {"producto": "Cuadro Atlas", "cantidad": 2, "precio": 31.63},
    {"producto": "Sábana Nórdico 140x200", "cantidad": 1, "precio": 103.97},
    {"producto": "Sofá Aurora 160cm", "cantidad": 1, "precio": 221.99},
]

total_unidades = 0
total_euros = 0

print("FraSoHome Madrid Centro")
for linea in ticket:
    importe = calcular_importe(linea["cantidad"], linea["precio"])
    print(f"{linea['cantidad']} x {linea['producto']}: {importe:.2f} euros")
    total_unidades = total_unidades + linea["cantidad"]
    total_euros = total_euros + importe

print(f"Unidades: {total_unidades}")
print(f"Total: {total_euros:.2f} euros")
```

Con el ticket vacío muestra `Unidades: 0` y `Total: 0.00 euros`, porque el bucle no da ninguna vuelta. Con 4 cuadros, `Unidades: 6` y `Total: 452.48 euros`.

</details>

## Módulos: funciones que ya ha escrito otra persona

No hace falta escribirlo todo desde cero. Python trae de serie una enorme **biblioteca estándar**: cientos de **módulos**, que son archivos con funciones ya hechas y probadas, agrupadas por tema. Para usarlas, primero hay que **importarlas** con `import`:

```python
import math
import statistics
from datetime import date

# math: funciones matemáticas
print(math.ceil(23 / 5))    # 5: cajas necesarias para 23 velas si caben 5 por caja (redondea hacia arriba)

# statistics: estadística básica
precios = [31.63, 103.97, 221.99, 112.47]
print(round(statistics.mean(precios), 2))   # media: 117.52
print(statistics.median(precios))           # mediana: 108.22

# datetime: fechas
alta = date(2018, 12, 23)      # fecha de alta del cliente C0001 en el programa de fidelización
hoy = date(2025, 9, 2)
print((hoy - alta).days)       # 2445 días como cliente
print(hoy.strftime("%d/%m/%Y"))  # 02/09/2025
```

| Forma de importar | Cómo se usa después | Cuándo usarla |
|---|---|---|
| `import math` | `math.ceil(...)` | La más habitual y la más clara: se ve de dónde viene cada función |
| `from datetime import date` | `date(...)` | Cuando usas mucho una pieza concreta de un módulo |
| `import statistics as st` | `st.mean(...)` | Para acortar nombres largos. Verás `import pandas as pd` en todas partes |

> **Idea clave.** Un **módulo** es un archivo `.py` con funciones. Un **paquete** es una carpeta con varios módulos. La **biblioteca estándar** viene con Python; los paquetes de otras personas (como pandas) hay que **instalarlos** aparte. Lo harás en el apartado de paquetes.

> **Para curiosos.** Tus propios archivos `.py` también son módulos. Si guardas `calcular_importe` en `calculos.py`, desde otro archivo de la misma carpeta puedes escribir `from calculos import calcular_importe`. Así es como se organizan los proyectos grandes. Y es entonces cuando aparece la carpeta `__pycache__` con el bytecode de la que hablamos en la [sesión 1](../sesion-1/03-como-entiende-el-ordenador-un-programa.md).

## Reto · El informe de márgenes de Marta

Marta te pasa esta lista con cinco productos de su tienda:

| Producto | Precio de venta | Coste unitario |
|---|---|---|
| Cuadro Atlas | 31,63 € | 21,79 € |
| Sábana Nórdico 140x200 | 103,97 € | 39,47 € |
| Sofá Aurora 160cm | 221,99 € | 143,47 € |
| Alfombra Zen 200x300 | 112,47 € | 40,67 € |
| Sábana Minimal 200x300 | 200,88 € | 128,73 € |

Escribe un programa que:

1. Guarde los productos como una **lista de diccionarios**.
2. Tenga una **función** `calcular_margen_pct(precio_venta, coste_unitario)` que devuelva el margen en porcentaje.
3. **Recorra** la lista y muestre el margen de cada producto con un decimal.
4. Marque con `<- margen bajo` los productos con un margen **inferior al 40 %**.
5. Al final, diga **cuántos** productos tienen margen bajo y cuál es el **margen medio** (usa el módulo `statistics`).

Resultado esperado:

```text
Cuadro Atlas: 31.1 %  <- margen bajo
Sábana Nórdico 140x200: 62.0 %
Sofá Aurora 160cm: 35.4 %  <- margen bajo
Alfombra Zen 200x300: 63.8 %
Sábana Minimal 200x300: 35.9 %  <- margen bajo
Productos con margen bajo: 3 de 5
Margen medio: 45.7 %
```

<details markdown>
<summary>Ver solución</summary>

```python
import statistics


def calcular_margen_pct(precio_venta, coste_unitario):
    """Devuelve el margen como porcentaje del precio de venta."""
    return (precio_venta - coste_unitario) / precio_venta * 100


productos = [
    {"nombre": "Cuadro Atlas", "precio_venta": 31.63, "coste_unitario": 21.79},
    {"nombre": "Sábana Nórdico 140x200", "precio_venta": 103.97, "coste_unitario": 39.47},
    {"nombre": "Sofá Aurora 160cm", "precio_venta": 221.99, "coste_unitario": 143.47},
    {"nombre": "Alfombra Zen 200x300", "precio_venta": 112.47, "coste_unitario": 40.67},
    {"nombre": "Sábana Minimal 200x300", "precio_venta": 200.88, "coste_unitario": 128.73},
]

margen_bajo = 0
margenes = []

for p in productos:
    pct = calcular_margen_pct(p["precio_venta"], p["coste_unitario"])
    margenes.append(pct)
    if pct < 40:
        aviso = "  <- margen bajo"
        margen_bajo = margen_bajo + 1
    else:
        aviso = ""
    print(f"{p['nombre']}: {pct:.1f} %{aviso}")

print(f"Productos con margen bajo: {margen_bajo} de {len(productos)}")
print(f"Margen medio: {statistics.mean(margenes):.1f} %")
```

Este programa reúne casi todo lo visto hasta ahora: variables, operaciones, una función con `return`, una lista de diccionarios, un bucle, una decisión, un acumulador, un módulo de la biblioteca estándar y una f-string.

</details>

---

[← Anterior: Listas, diccionarios y bucles](01-listas-diccionarios-y-bucles.md) · [Índice de la sesión](README.md) · [Siguiente: Markdown →](03-markdown.md)

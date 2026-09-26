# 7 · NumPy

[Inicio](../README.md) › [Sesión 2](README.md) › NumPy

**Tiempo aproximado:** 15 minutos

## La pregunta de Marta

> *"Quiero ver los precios de mis productos con el IVA incluido. ¿Tengo que escribir un bucle cada vez que quiera hacer una cuenta con todos los precios?"*

Con listas, sí. Con **NumPy**, no.

## Qué es NumPy

**NumPy** (*Numerical Python*) es el paquete sobre el que se construye casi todo el análisis de datos en Python: pandas, matplotlib, scikit-learn... Aporta un tipo de dato nuevo, el **array**: una colección de números **del mismo tipo**, guardados juntos en memoria, con la que se puede operar **de golpe**.

¿Recuerdas del [apartado 3 de la sesión 1](../sesion-1/03-como-entiende-el-ordenador-un-programa.md) que Python es "lento", pero se usa para datos porque delega el trabajo pesado en código compilado? NumPy es el mejor ejemplo: **por dentro está escrito en C**. Tú escribes una línea sencilla de Python y el cálculo lo hace código compilado, muy rápido.

Crea un notebook nuevo, `numpy.ipynb`, y ve probando cada ejemplo en una celda.

## Crear un array

```python
import numpy as np

precios = np.array([31.63, 103.97, 221.99, 112.47, 200.88])
precios
```

```text
array([ 31.63, 103.97, 221.99, 112.47, 200.88])
```

`import numpy as np` es la forma de importarlo que usa todo el mundo. Los precios son del Cuadro Atlas, la Sábana Nórdico 140x200, el Sofá Aurora 160cm, la Alfombra Zen 200x300 y la Sábana Minimal 200x300.

| Atributo | Qué dice | Resultado |
|---|---|---|
| `precios.dtype` | El tipo de **todos** sus elementos | `float64`: decimales de 64 bits, los mismos `float` de la sesión 1 |
| `precios.shape` | Su forma: cuántos elementos tiene en cada dimensión | `(5,)`: una dimensión con 5 elementos |

## Operar con todo el array a la vez

Aquí está la gran diferencia con las listas:

```python
precios * 1.21
```

```text
array([ 38.2723, 125.8037, 268.6079, 136.0887, 243.0648])
```

Una sola línea multiplica **cada** precio por 1,21 (el 21 % de IVA), sin bucle. Esto se llama **operación vectorizada**.

> **Cuidado.** Prueba lo mismo con una lista: `[31.63, 103.97] * 2`. El resultado es `[31.63, 103.97, 31.63, 103.97]`: con listas, `*` **repite** la lista. Con arrays, **multiplica** cada elemento. Mismo símbolo, comportamiento distinto según el tipo.

También se puede operar **entre arrays**, elemento a elemento:

```python
costes = np.array([21.79, 39.47, 143.47, 40.67, 128.73])

margen = precios - costes
margen_pct = margen / precios * 100
np.round(margen_pct, 1)
```

```text
array([31.1, 62. , 35.4, 63.8, 35.9])
```

Son los mismos márgenes del reto de Marta del [apartado 2](02-funciones-y-modulos.md), pero sin bucle, sin función y sin acumulador.

> **Pruébalo.** El ticket de Madrid Centro, en dos líneas: con `cantidades = np.array([2, 1, 1])`, multiplica por los tres primeros precios (`precios[:3]`) y suma el resultado con `.sum()`. ¿Te sale `389.22`?

## Resúmenes en una línea

| Quiero... | Escribo | Resultado |
|---|---|---|
| La suma | `precios.sum()` | `670.94` |
| La media | `precios.mean()` | `134.188...` |
| La mediana | `np.median(precios)` | `112.47` |
| El máximo | `precios.max()` | `221.99` |
| La **posición** del máximo | `precios.argmax()` | `2` (el tercer elemento, el sofá) |
| La desviación típica | `precios.std()` | `69.37...` |

> **Cuidado.** En el notebook verás los resultados como `np.float64(670.94)`. No es un error: es el número 670,94 con su tipo de NumPy. Con `print(precios.sum())` verás solo el número.

## Filtrar con condiciones

Una comparación con un array devuelve **otro array de `True` y `False`**:

```python
precios > 150
```

```text
array([False, False,  True, False,  True])
```

Y ese array se puede usar **como filtro**, entre corchetes:

```python
precios[precios > 150]
```

```text
array([221.99, 200.88])
```

Léelo así: *"dame los precios en los que la condición es verdadera"*. Esta técnica, llamada **filtrado booleano**, es la base de cómo se filtran los datos en pandas.

> **Pruébalo.** Crea un array `nombres` con los cinco nombres de producto y usa la misma condición para obtener **los nombres** de los productos de más de 150 €: `nombres[precios > 150]`.

## ¿De verdad es más rápido?

> **Pruébalo.** En una celda, crea diez millones de números como lista y como array:
>
> ```python
> numeros = list(range(10_000_000))
> arr = np.arange(10_000_000)
> ```
>
> En otra celda escribe `%timeit sum(numeros)` y, en otra, `%timeit arr.sum()`. `%timeit` es un comando especial de los notebooks que mide cuánto tarda una instrucción.

Los dos dan el mismo resultado, pero NumPy suele ser **decenas de veces más rápido**. La cifra exacta depende de tu ordenador. Con los millones de filas de una empresa real, esa diferencia es la que separa esperar un segundo de esperar un minuto.

> **Para curiosos.** Los arrays pueden tener **varias dimensiones**. Una tabla con el stock de 2 tiendas y 3 productos sería `np.array([[14, 11, 1], [3, 0, 7]])`, con `shape` `(2, 3)`. Con `.sum(axis=0)` sumas por columnas (total por producto) y con `.sum(axis=1)`, por filas (total por tienda).

> **Idea clave.** Un array de NumPy es rápido porque **todos sus elementos son del mismo tipo**. Si mezclas tipos, por ejemplo `np.array([1, "2", 3.5])`, NumPy convierte todo a texto y pierdes la posibilidad de calcular. El tipo de dato vuelve a ser clave.

---

[← Anterior: Notebooks](06-notebooks.md) · [Índice de la sesión](README.md) · [Siguiente: Primeros datos con pandas →](08-pandas.md)

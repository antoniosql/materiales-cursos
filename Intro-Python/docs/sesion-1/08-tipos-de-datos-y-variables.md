# 8 · Tipos de datos y variables

[Inicio](../README.md) › [Sesión 1](README.md) › Tipos de datos y variables

**Tiempo aproximado:** 20 minutos

## La pregunta de Marta

> *"El **Sofá Aurora 160cm** lo vendemos a **221,99 €** y a nosotros nos cuesta **143,47 €**. ¿Cuánto ganamos con cada sofá? ¿Y qué porcentaje del precio es beneficio?"*

Para responder necesitamos dos cosas: **datos** y **nombres** para guardarlos. En el [apartado 3](03-como-entiende-el-ordenador-un-programa.md) viste que, por dentro, todo son ceros y unos, y que el ordenador necesita saber **cómo interpretarlos**. Eso es exactamente un **tipo de dato**.

## Valores y tipos

Un **valor** es un dato concreto: `2`, `221.99`, `"Madrid Centro"`. Cada valor tiene un **tipo**, que le dice a Python dos cosas: **cómo guardarlo** en memoria y **qué se puede hacer** con él. Los tipos básicos de Python son estos:

| Tipo | Nombre en Python | Ejemplos de FraSoHome | Para qué sirve |
|---|---|---|---|
| Número entero | `int` | `2` (unidades), `1850` (m² de la tienda) | Contar cosas |
| Número decimal | `float` | `221.99` (precio), `143.47` (coste) | Importes, medidas, porcentajes |
| Texto | `str` (de *string*, cadena) | `"Sofá Aurora 160cm"`, `"P1000"` | Nombres, descripciones, códigos |
| Lógico | `bool` (de *booleano*) | `True`, `False` | Respuestas de sí o no: ¿está activo el producto? |
| Nada | `NoneType` (su único valor es `None`) | `None` | Indicar que un dato **no existe o falta**: un cliente sin correo registrado |

> **Cuidado.** En Python los decimales se escriben con **punto**, no con coma: `221.99`, no `221,99`. Y los textos van **siempre entre comillas**: `"Madrid"` es un texto; `Madrid` sin comillas, Python lo tomará por un nombre que no conoce.

> **Pruébalo.** Python te dice el tipo de cualquier valor con `type()`. Crea `tipos.py`:
>
> ```python
> print(type(2))
> print(type(221.99))
> print(type("Sofá Aurora 160cm"))
> print(type(True))
> print(type(None))
> print(type("221.99"))
> ```
>
> Fíjate en la última línea: `"221.99"` entre comillas **no es un número**, es un texto que contiene cifras. Esta diferencia te ahorrará muchos disgustos cuando trabajes con datos.

## Cada tipo, un poco más a fondo

### `int`: enteros sin límite

En muchos lenguajes los enteros tienen un tamaño máximo. En Python no: un `int` crece todo lo que haga falta, mientras quepa en la memoria.

```python
print(2 ** 100)
```

```text
1267650600228229401496703205376
```

### `float`: decimales con letra pequeña

Los `float` se guardan en **64 bits**, siguiendo un estándar internacional (IEEE 754) que usan casi todos los lenguajes. Eso da unos **15-16 dígitos de precisión**, más que suficiente para casi todo, pero con una consecuencia curiosa: como se guardan en binario, algunos decimales **no se pueden representar exactamente**, igual que 1/3 no se puede escribir exactamente en decimal (0,3333...).

```python
print(0.1 + 0.2)
print(221.99 - 143.47)
```

```text
0.30000000000000004
78.52000000000001
```

No es un fallo tuyo ni de Python. La diferencia es minúscula y la resolveremos al **mostrar** los resultados, redondeando a dos decimales.

> **Cuidado.** Por este motivo, **no compares decimales con `==`**: `0.1 + 0.2 == 0.3` da `False`. Lo verás en el [apartado 10](10-tomar-decisiones.md).

> **Para curiosos.** Los bancos y los programas de contabilidad no usan `float` para el dinero, sino tipos decimales exactos. Python tiene uno: `from decimal import Decimal` y `Decimal("0.1") + Decimal("0.2")` da exactamente `0.3`.

### `str`: texto, carácter a carácter

Un `str` es una **secuencia de caracteres Unicode**, así que admite tildes, eñes, el símbolo `€` o una estrella `★` (hay productos de FraSoHome con una en el nombre). Puedes consultar sus caracteres por posición, empezando a contar desde **0**:

```python
tienda = "Madrid Centro"
print(tienda[0])       # M
print(tienda[-1])      # o  (el último)
print(len(tienda))     # 13 caracteres, contando el espacio
```

Los textos traen **métodos**: acciones que se escriben con un punto detrás del valor. Son muy útiles para **limpiar datos**:

| Método | Qué hace | Ejemplo | Resultado |
|---|---|---|---|
| `.upper()` | Pasa a mayúsculas | `"Madrid Centro".upper()` | `"MADRID CENTRO"` |
| `.lower()` | Pasa a minúsculas | `"Sofá".lower()` | `"sofá"` |
| `.strip()` | Quita los espacios del principio y del final | `"  decoración ".strip()` | `"decoración"` |
| `.capitalize()` | Primera letra en mayúscula y el resto en minúscula | `"decoración".capitalize()` | `"Decoración"` |
| `.replace(a, b)` | Sustituye un trozo por otro | `"31,63".replace(",", ".")` | `"31.63"` |

> **Idea clave.** Para Python, `"Decoración"` y `"decoración"` son **dos textos distintos**. En los datos reales de FraSoHome aparecen las dos formas en la columna de categoría. Métodos como `.strip()` y `.capitalize()` sirven justo para unificarlas.

### `bool`: verdadero o falso

Solo tiene dos valores, `True` y `False`, con la primera letra en mayúscula. Aparece siempre que haces una **pregunta** al programa: *¿el stock es menor que el mínimo?* La respuesta es un `bool`. Lo usarás mucho en el [apartado 10](10-tomar-decisiones.md).

### `None`: el dato que falta

`None` representa **la ausencia de valor**. No es cero ni un texto vacío: es "no hay dato". En las bases de datos se llama `NULL`. Al trabajar con datos reales lo verás a menudo: clientes sin correo, productos sin coste registrado...

## Tipado dinámico y fuerte

Python tiene dos características que conviene conocer, porque cambian cómo se escribe código:

| Característica | Qué significa | Ejemplo |
|---|---|---|
| **Tipado dinámico** | No declaras el tipo de una variable: Python lo deduce del valor. Una misma variable puede guardar después un valor de otro tipo | `x = 5` y luego `x = "cinco"` es válido |
| **Tipado fuerte** | Python **no mezcla tipos por su cuenta**. Si intentas sumar un texto y un número, se niega | `"2" + 2` da un error (`TypeError`) |

En lenguajes de **tipado estático**, como Java o C, hay que declarar el tipo de cada variable (`int unidades = 2;`) y no puede cambiar. Es más trabajo al escribir, pero muchos errores se detectan antes de ejecutar. En lenguajes de **tipado débil**, como JavaScript, `"2" + 2` da `"22"` sin quejarse, lo que a veces provoca resultados inesperados.

> **Para curiosos.** Python permite **anotar** el tipo esperado de una variable: `precio: float = 31.63`. Python no lo comprueba al ejecutar, pero el editor y otras herramientas lo usan para avisarte de errores. Lo verás en mucho código profesional.

## Conversiones entre tipos

Como Python no mezcla tipos por su cuenta, a veces tendrás que **convertir** tú:

| Función | Convierte a... | Ejemplo | Resultado |
|---|---|---|---|
| `int()` | Entero | `int("2")` | `2` |
| `int()` | Entero (¡**corta** los decimales, no redondea!) | `int(3.9)` | `3` |
| `float()` | Decimal | `float("31.63")` | `31.63` |
| `str()` | Texto | `str(2)` | `"2"` |
| `round()` | Redondea | `round(78.52000000000001, 2)` | `78.52` |

> **Pruébalo.** ¿Qué pasa con `float("31,63")`? ¿Cómo lo arreglarías con uno de los métodos de texto de arriba?

## Operaciones

| Operación | Símbolo | Ejemplo | Resultado |
|---|---|---|---|
| Suma | `+` | `221.99 + 10` | `231.99` |
| Resta | `-` | `221.99 - 143.47` | `78.52...` |
| Multiplicación | `*` | `2 * 31.63` | `63.26` |
| División | `/` | `10 / 2` | `5.0` (**siempre** da `float`) |
| División entera | `//` | `23 // 5` | `4` |
| Resto de la división | `%` | `23 % 5` | `3` |
| Potencia | `**` | `2 ** 3` | `8` |

Las dos más raras son muy útiles. Imagina que en el almacén hay **23 velas** y se empaquetan en **cajas de 5**: `23 // 5` te da las **4 cajas** completas y `23 % 5` las **3 velas sueltas** que sobran.

Con los textos, `+` **une** (concatena): `"FraSoHome" + " " + "Madrid Centro"` da `"FraSoHome Madrid Centro"`.

Python respeta el **orden de las operaciones** de las matemáticas: primero potencias, luego multiplicaciones y divisiones, y al final sumas y restas. Usa **paréntesis** para dejarlo claro: `(221.99 - 143.47) / 221.99`.

## Variables: poner nombre a los datos

Una **variable** es un nombre que apunta a un valor. Se crea con `=`:

```python
precio_venta = 221.99
```

Léelo así: *"guarda 221.99 con el nombre `precio_venta`"*.

> **Idea clave.** En programación, `=` **no significa "es igual a"**, sino **"asigna"**. El valor de la derecha se guarda con el nombre de la izquierda.

Técnicamente, el valor `221.99` se crea en la **memoria** y la variable es una **etiqueta** que apunta a él. Si cambias el valor, la etiqueta pasa a apuntar a otro sitio:

```python
stock = 11
print(stock)
stock = stock - 1      # se ha vendido una unidad
print(stock)
```

```text
11
10
```

La tercera línea se lee de derecha a izquierda: *"toma el valor actual de `stock`, réstale 1 y guarda el resultado otra vez como `stock`"*.

### Reglas para los nombres

| Regla | Válido | No válido |
|---|---|---|
| Sin espacios: usa `_` para separar palabras (se llama *snake_case*) | `precio_venta` | `precio venta` |
| No puede empezar por un número | `tienda_1` | `1_tienda` |
| Mayúsculas y minúsculas son distintas | `precio` y `Precio` son **dos variables diferentes** | — |
| No se pueden usar palabras reservadas de Python | `clase` | `class`, `if`, `for` |
| Que se entienda lo que guarda | `coste_unitario` | `x`, `dato2`, `cosa` |

> **Cuidado.** Python permite tildes y eñes en los nombres de variables, pero es mejor evitarlas (`anio`, no `año`). Es la costumbre en todo el mundo y evita problemas con otras herramientas.

## Respondiendo a Marta

> **Pruébalo.** Crea `margen.py`:
>
> ```python
> # Margen de un producto de FraSoHome: Sofá Aurora 160cm (P1000)
>
> producto = "Sofá Aurora 160cm"
> precio_venta = 221.99      # euros que paga el cliente
> coste_unitario = 143.47    # euros que le cuesta a FraSoHome
>
> margen = precio_venta - coste_unitario
> margen_pct = margen / precio_venta * 100
>
> print(producto)
> print("Margen en euros:", round(margen, 2))
> print("Margen sobre el precio:", round(margen_pct, 1))
> ```
>
> **Antes de ejecutar, predice** qué saldrá.

```text
Sofá Aurora 160cm
Margen en euros: 78.52
Margen sobre el precio: 35.4
```

`print` puede mostrar **varias cosas separadas por comas**, y las muestra en la misma línea separadas por un espacio.

> **Pruébalo. Cambia algo.**
>
> 1. Cambia el producto por el **Cuadro Atlas**: precio de venta 31,63 € y coste 21,79 €. ¿Qué producto deja más margen en euros? ¿Y en porcentaje?
> 2. Marta quiere saber cuánto gana si vende **3 sofás**. Añade una variable `unidades = 3` y calcula el margen total.
> 3. Añade al final `print(type(margen), type(unidades))`. ¿Qué tipo tiene cada una? ¿Por qué?

<details markdown>
<summary>Ver solución</summary>

```python
producto = "Cuadro Atlas"
precio_venta = 31.63
coste_unitario = 21.79
unidades = 3

margen = precio_venta - coste_unitario
margen_pct = margen / precio_venta * 100
margen_total = margen * unidades

print(producto)
print("Margen en euros:", round(margen, 2))
print("Margen sobre el precio:", round(margen_pct, 1))
print("Margen total:", round(margen_total, 2))
print(type(margen), type(unidades))
```

El Cuadro Atlas deja 9,84 € por unidad (un 31,1 % del precio). El sofá deja más dinero por unidad (78,52 €) y también un porcentaje algo mayor (35,4 %). `margen` es `float` porque sale de restar decimales; `unidades` es `int` porque le asignaste un número entero.

</details>

Puedes comparar con el ejemplo [02_margen.py](ejemplos/02_margen.py).

---

[← Anterior: Tu primer programa](07-tu-primer-programa.md) · [Índice de la sesión](README.md) · [Siguiente: Preguntar y responder →](09-preguntar-y-responder.md)

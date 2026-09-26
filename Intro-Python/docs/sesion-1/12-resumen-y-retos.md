# 12 · Resumen y retos

[Inicio](../README.md) › [Sesión 1](README.md) › Resumen y retos

**Tiempo aproximado:** 10 minutos en clase. Los retos, cuando quieras.

## Lo que has conseguido hoy

Esta mañana no sabías qué era un intérprete. Ahora:

| Sabes... | Con... |
|---|---|
| Pensar un problema como una secuencia de pasos precisos | Algoritmos |
| Explicar qué pasa dentro del ordenador cuando se ejecuta un programa | CPU, memoria, disco, bits y bytes, compilado frente a interpretado, bytecode |
| Preparar tu ordenador para programar | Python, VS Code, la extensión Python y Git |
| Moverte por tus carpetas y ejecutar programas | La terminal: `pwd`, `ls`, `cd`, `mkdir`, `python archivo.py` |
| Mostrar resultados y dejar notas en el código | `print`, comentarios `#` |
| Distinguir los tipos de datos y trabajar con ellos | `int`, `float`, `str`, `bool`, `None`, `type()`, métodos de texto, tipado dinámico y fuerte |
| Guardar datos y operar con ellos | Variables, `+ - * / // % **`, `round()` |
| Preguntar al usuario y presentar bien los resultados | `input`, `int()`, `float()`, f-strings con `:.2f` |
| Hacer que el programa decida | `if`, `elif`, `else`, `==`, `<`, `and`, `or` |
| Entender y prevenir errores | Tracebacks, `try` y `except` |

Y lo has hecho respondiendo a preguntas reales de Marta: márgenes, reposición de stock, descuentos y datos con errores.

## Autoevaluación

Antes de la sesión 2, comprueba si puedes hacer esto **sin mirar los apuntes**:

- [ ] Explicar la diferencia entre un lenguaje compilado y uno interpretado, y qué hace Python exactamente.
- [ ] Crear un archivo `.py`, guardarlo y ejecutarlo con el botón ▶ y desde la terminal.
- [ ] Decir de qué tipo es `2`, `2.0`, `"2"`, `True` y `None`.
- [ ] Explicar por qué `0.1 + 0.2` no da exactamente `0.3`.
- [ ] Explicar la diferencia entre `=` y `==`.
- [ ] Explicar por qué `input` necesita `int()` o `float()` para hacer cálculos.
- [ ] Escribir un `if` / `elif` / `else` con la sangría correcta.
- [ ] Leer un traceback y decir en qué línea está el error y de qué tipo es.

Si alguna no te sale, vuelve al apartado correspondiente. Es normal: hoy has visto muchas cosas nuevas.

## Retos para practicar (voluntarios)

Los retos son **voluntarios**, pero son la mejor forma de asentar lo aprendido. Intenta cada uno **al menos 15 minutos** antes de mirar la solución. Guárdalos en tu carpeta `curso-python`.

### Reto 1 · Las cajas de velas

En el almacén de FraSoHome hay que empaquetar velas. Escribe un programa que **pregunte** cuántas velas hay y cuántas caben en cada caja, y diga cuántas **cajas completas** salen y cuántas velas quedan **sueltas**.

Comprueba tu programa: con **23 velas** y cajas de **5**, deben salir **4 cajas** y **3 velas sueltas**.

<details markdown>
<summary>Ver pista</summary>

Repasa las operaciones `//` y `%` en el [apartado 8](08-tipos-de-datos-y-variables.md).

</details>

<details markdown>
<summary>Ver solución</summary>

```python
unidades = int(input("¿Cuántas velas hay en el almacén? "))
por_caja = int(input("¿Cuántas velas caben en cada caja? "))

cajas = unidades // por_caja
sueltas = unidades % por_caja

print(f"Cajas completas: {cajas}")
print(f"Velas sueltas: {sueltas}")
```

</details>

### Reto 2 · El semáforo del stock, a prueba de errores

Mejora el programa de stock del [apartado 10](10-tomar-decisiones.md):

1. Que **pregunte** el nombre del producto, el stock al cierre y el stock mínimo.
2. Que, si hay que reponer, diga **cuántas unidades faltan** como mínimo para llegar al stock mínimo.
3. Que, si el stock es **negativo**, avise de que el dato es un error de registro. (Sí, en los datos reales de FraSoHome hay stocks negativos.)
4. Que, si alguien escribe algo que no es un número, muestre un mensaje amable en lugar de un error.

Comprueba: con el **Sofá Boreal Compact**, stock **1** y mínimo **3**, debe decir que hay que reponer **2 unidades**.

<details markdown>
<summary>Ver solución</summary>

```python
producto = input("Producto: ")

try:
    stock_cierre = int(input("Stock al cierre: "))
    stock_minimo = int(input("Stock mínimo: "))

    if stock_cierre < 0:
        print("Stock negativo: revisa el dato, es un error de registro")
    elif stock_cierre == 0:
        print(f"{producto}: SIN EXISTENCIAS. Pedido urgente.")
    elif stock_cierre < stock_minimo:
        faltan = stock_minimo - stock_cierre
        print(f"{producto}: hay que reponer {faltan} unidades como mínimo.")
    else:
        print(f"{producto}: stock suficiente.")
except ValueError:
    print("El stock tiene que ser un número entero, por ejemplo 7")
```

Fíjate en el orden de las condiciones: primero el caso imposible (negativo), después el más urgente (cero) y luego el general.

</details>

### Reto 3 · Datos que llegan sucios

Los sistemas de FraSoHome no siempre guardan los datos igual. Estos tres valores están copiados **tal cual** de los archivos reales de la empresa:

```python
categoria_raw = "  decoración "
precio_raw = "127,74"
precio_raw_2 = "€848.91"
```

Escribe un programa que:

1. Convierta `categoria_raw` en `"Decoración"`, sin espacios y con la primera letra en mayúscula.
2. Convierta `precio_raw` y `precio_raw_2` en números decimales (`float`).
3. Muestre los valores limpios con su **tipo**.
4. Muestre la **suma** de los dos precios con dos decimales.

Resultado esperado:

```text
Categoría: Decoración
<class 'str'>
Precio 1: 127.74
<class 'float'>
Precio 2: 848.91
<class 'float'>
Suma de precios: 976.65
```

<details markdown>
<summary>Ver pista</summary>

Repasa los métodos de texto (`.strip()`, `.capitalize()`, `.replace()`) y las conversiones en el [apartado 8](08-tipos-de-datos-y-variables.md). Puedes encadenar métodos: `texto.strip().capitalize()`.

</details>

<details markdown>
<summary>Ver solución</summary>

```python
categoria_raw = "  decoración "
precio_raw = "127,74"
precio_raw_2 = "€848.91"

categoria = categoria_raw.strip().capitalize()
precio = float(precio_raw.replace(",", "."))
precio_2 = float(precio_raw_2.replace("€", ""))

print(f"Categoría: {categoria}")
print(type(categoria))
print(f"Precio 1: {precio:.2f}")
print(type(precio))
print(f"Precio 2: {precio_2:.2f}")
print(type(precio_2))
print(f"Suma de precios: {precio + precio_2:.2f}")
```

Acabas de hacer, en pequeño, una tarea que ocupa buena parte del tiempo de cualquier equipo de datos: **limpiar y tipar** datos que llegan con formatos distintos.

</details>

## Para seguir aprendiendo

Si te has quedado con ganas de más:

- ***Piensa en Python*** (*Think Python*), de Allen B. Downey: libro gratuito en castellano, muy recomendable para empezar desde cero.
- **CS50's Introduction to Programming with Python** (cs50.harvard.edu/python): curso gratuito de la Universidad de Harvard, en inglés, con vídeos muy claros.
- **Fundamentos de Python 1**, del Python Institute (edube.org): curso gratuito que prepara para la certificación básica PCEP.

## Lo que viene en la sesión 2

Marta tiene cientos de productos, y hoy hemos trabajado con uno cada vez. En la próxima sesión:

- Guardarás **muchos datos juntos** (listas y diccionarios), **repetirás** tareas con bucles y crearás tus propias **funciones**.
- Aprenderás **Markdown**, el formato en el que están escritos estos mismos materiales.
- Usarás **Git** para guardar el historial de tu trabajo y **GitHub** para tener una copia en la nube.
- Instalarás **paquetes**, trabajarás con **notebooks**, calcularás con **NumPy** y harás tus primeras preguntas a **datos reales de FraSoHome** con pandas, incluso leyéndolos directamente de su base de datos.

---

[← Anterior: Cuando algo falla](11-cuando-algo-falla.md) · [Índice de la sesión](README.md) · [Inicio del seminario](../README.md)

# 8 · Primeros datos con pandas

[Inicio](../README.md) › [Sesión 2](README.md) › Primeros datos con pandas

**Tiempo aproximado:** 35 minutos

## La pregunta de Marta

> *"Te paso el catálogo completo de FraSoHome, tal y como sale del sistema. Quiero saber cuántos productos tenemos de cada categoría, cuáles son los más caros y en qué categoría ganamos más por producto."*

Ha llegado el momento de trabajar con **datos reales**. Para eso usaremos **pandas**, la herramienta más utilizada del mundo para trabajar con tablas en Python.

## Prepara los datos

1. Dentro de `curso-python`, crea una carpeta llamada **`datos`**.
2. Descarga en ella estos dos archivos del sistema de FraSoHome: [productos.csv](datos/productos.csv) (el catálogo) y [tiendas.csv](datos/tiendas.csv).
3. Crea un notebook nuevo, `catalogo.ipynb`, con el kernel `.venv`, y ve probando cada ejemplo en una celda.

> **Para curiosos.** Un archivo **CSV** (*comma-separated values*) es una tabla guardada como texto: cada línea es una fila y los valores se separan con comas. Puedes abrirlo en VS Code para ver cómo es por dentro. Es el formato más común para intercambiar datos entre sistemas.

## Series y DataFrame

pandas tiene dos piezas básicas:

| Pieza | Qué es | Analogía |
|---|---|---|
| **DataFrame** | Una **tabla**: filas y columnas con nombre | Una hoja de Excel |
| **Series** | **Una columna** de esa tabla | Una columna de la hoja |

Por dentro, cada columna es un **array de NumPy**. Por eso todo lo que viste en el apartado anterior (operaciones vectorizadas, filtros con `True` y `False`) funciona igual aquí.

Empecemos con algo conocido: el ticket de Madrid Centro. ¿Recuerdas que dijimos que una lista de diccionarios ya es una tabla? pandas la convierte en una directamente:

```python
import pandas as pd

ticket = [
    {"producto": "Cuadro Atlas", "cantidad": 2, "precio": 31.63},
    {"producto": "Sábana Nórdico 140x200", "cantidad": 1, "precio": 103.97},
    {"producto": "Sofá Aurora 160cm", "cantidad": 1, "precio": 221.99},
]

df = pd.DataFrame(ticket)
df["importe"] = df["cantidad"] * df["precio"]
df
```

|   | producto | cantidad | precio | importe |
|---|---|---|---|---|
| 0 | Cuadro Atlas | 2 | 31.63 | 63.26 |
| 1 | Sábana Nórdico 140x200 | 1 | 103.97 | 103.97 |
| 2 | Sofá Aurora 160cm | 1 | 221.99 | 221.99 |

Una sola línea ha creado la columna `importe` para **todas** las filas. Y `df["importe"].sum()` da `389.22`, el total del ticket, sin bucles ni acumuladores.

> **Idea clave.** La columna de la izquierda (0, 1, 2) es el **índice**: la etiqueta de cada fila. pandas lo crea automáticamente.

## Leer el catálogo

```python
productos = pd.read_csv("datos/productos.csv")
productos.shape
```

```text
(101, 18)
```

101 productos y 18 columnas. Las primeras exploraciones que se hacen **siempre** con una tabla nueva:

| Quiero... | Escribo |
|---|---|
| Ver las primeras filas | `productos.head()` (o `productos.head(10)`) |
| Ver los nombres de las columnas | `productos.columns` |
| Ver el tipo de cada columna y los datos que faltan | `productos.info()` |
| Ver un resumen estadístico de las columnas numéricas | `productos.describe()` |

> **Pruébalo.** Ejecuta las cuatro. Fíjate bien en el resultado de `info()`.

## La primera sorpresa

En `info()` aparece algo así (resumido):

```text
 #   Column               Non-Null Count  Dtype
---  ------               --------------  -----
 0   product_id           101 non-null    str
 1   nombre_producto      101 non-null    str
 2   categoria            101 non-null    str
 8   precio_venta         101 non-null    str
 9   coste_unitario       98 non-null     str
 10  iva_pct              101 non-null    int64
 11  peso_kg              101 non-null    float64
```

`precio_venta` y `coste_unitario` son **texto** (`str`; en versiones antiguas de pandas aparece como `object`), no números. Además, `coste_unitario` tiene solo 98 valores: **faltan 3**.

> **Pruébalo.** Ejecuta `productos["precio_venta"].sum()`. ¿Qué pasa?

<details markdown>
<summary>Ver explicación</summary>

Devuelve un texto larguísimo que empieza por `'221.9931.63169.18264.87...'`. Al ser textos, **sumar significa pegar**, como viste con `"FraSoHome" + " Madrid"` en la sesión 1. Y `productos["precio_venta"].mean()` directamente da error: no se puede calcular la media de unos textos.

</details>

¿Por qué son texto? Porque algunos precios vienen del sistema en otro formato:

```python
productos[productos["precio_venta"].str.contains(",|€")][["nombre_producto", "precio_venta"]]
```

| | nombre_producto | precio_venta |
|---|---|---|
| 39 | Cuadro Nórdico ★ | €237.04 |
| 51 | Alfombra Aurora Set 2 uds | 23,53 |
| 68 | Lámparas mesa Minimal "Star" | 50,41 |
| 72 | Aplique Aurora "Star" | 213,45 |
| 78 | Estantería Atlas 160cm | 702,02 |
| 83 | Aplique Aurora "Star" | €393.42 |

Basta con **seis** valores con coma o con `€` para que pandas no pueda tratar la columna entera como número. Es exactamente el problema del reto 3 de la sesión 1, pero ahora en una columna entera.

## Arreglarlo: limpiar y convertir

```python
productos["precio_venta"] = pd.to_numeric(
    productos["precio_venta"].str.replace("€", "").str.replace(",", ".")
)
productos["coste_unitario"] = pd.to_numeric(
    productos["coste_unitario"].str.replace(",", ".")
)
```

`.str` permite aplicar los **métodos de texto** que ya conoces a toda una columna a la vez. `pd.to_numeric` convierte la columna en números. Los 3 costes que faltaban se quedan como **`NaN`** (*Not a Number*), que es como pandas marca un dato ausente: el `None` de la sesión 1.

> **Pruébalo.** Vuelve a ejecutar `productos.info()` y `productos.describe()`. Ahora `precio_venta` es `float64` y ya puedes calcular: el precio medio del catálogo es de **289,79 €**.

`describe()` esconde más sorpresas. Mira las filas `min`:

- Hay un producto con **precio de venta 0**: el *Espejo Élite 80cm*, que ya conoces de la caza del error.
- Hay un producto con **coste negativo** (−12,50 €): las *Lámparas techo Zen "Star"*.

No los vamos a corregir ahora, pero ya sabes que **explorar datos es también descubrir sus errores**.

## Seleccionar y filtrar

| Quiero... | Escribo |
|---|---|
| Una columna (una Series) | `productos["nombre_producto"]` |
| Varias columnas (un DataFrame) | `productos[["nombre_producto", "precio_venta"]]` |
| Las filas que cumplen una condición | `productos[productos["precio_venta"] > 500]` |
| Dos condiciones a la vez (y) | `productos[(productos["estado_producto"] == "Activo") & (productos["precio_venta"] > 500)]` |
| Una u otra condición (o) | `productos[(productos["categoria"] == "Muebles") \| (productos["categoria"] == "Iluminación")]` |
| Una fila concreta por su índice | `productos.loc[0]` |

El filtrado funciona igual que en NumPy: la condición crea una columna de `True` y `False`, y los corchetes se quedan con las filas `True`.

> **Cuidado.** En pandas, para combinar condiciones se usan **`&`** (y) y **`|`** (o), no `and` ni `or`. Y cada condición va **entre paréntesis**. Si lo olvidas, verás un error difícil de entender.

> **Pruébalo.** ¿Cuántos productos **activos** cuestan más de 500 €? Pista: `len(...)` te da el número de filas. (Solución: 12.)

## Crear columnas

Igual que en el ticket, una operación entre columnas crea una columna nueva para todas las filas:

```python
productos["margen"] = productos["precio_venta"] - productos["coste_unitario"]
productos[["nombre_producto", "precio_venta", "coste_unitario", "margen"]].head(3)
```

| | nombre_producto | precio_venta | coste_unitario | margen |
|---|---|---|---|---|
| 0 | Sofá Aurora 160cm | 221.99 | 143.47 | 78.52 |
| 1 | Cuadro Atlas ★ | 31.63 | 21.79 | 9.84 |
| 2 | Sábana Brisa 90x200 | 169.18 | 106.71 | 62.47 |

Los productos sin coste tendrán el margen como `NaN`: si falta un dato, el resultado también falta.

## Contar, agrupar y ordenar

Ahora ya podemos responder a Marta.

### ¿Cuántos productos hay de cada categoría?

```python
productos["categoria"].value_counts()
```

```text
categoria
Decoración      31
Iluminación     28
Muebles         23
Textil hogar    18
decoración       1
```

¡Otra vez! `Decoración` y `decoración` aparecen como dos categorías distintas. Lo arreglamos con los métodos de texto de la sesión 1:

```python
productos["categoria"] = productos["categoria"].str.strip().str.capitalize()
productos["categoria"].value_counts()
```

```text
categoria
Decoración      32
Iluminación     28
Muebles         23
Textil hogar    18
```

### ¿En qué categoría ganamos más por producto?

`groupby` **agrupa** las filas por el valor de una columna y calcula algo para cada grupo:

```python
productos.groupby("categoria")["margen"].mean().round(2).sort_values(ascending=False)
```

```text
categoria
Muebles         323.71
Iluminación      82.07
Decoración       65.31
Textil hogar     51.47
```

Léelo así: *"agrupa los productos por categoría, toma la columna margen, calcula la media, redondea a dos decimales y ordena de mayor a menor"*. Encadenar operaciones así es muy habitual en pandas.

También se pueden calcular varias cosas a la vez:

```python
productos.groupby("categoria").agg(
    productos=("product_id", "count"),
    precio_medio=("precio_venta", "mean"),
    margen_medio=("margen", "mean"),
).round(2)
```

| categoria | productos | precio_medio | margen_medio |
|---|---|---|---|
| Decoración | 32 | 176.80 | 65.31 |
| Iluminación | 28 | 198.07 | 82.07 |
| Muebles | 23 | 700.38 | 323.71 |
| Textil hogar | 18 | 108.69 | 51.47 |

### ¿Cuáles son los cinco productos más caros?

```python
productos.sort_values("precio_venta", ascending=False)[["nombre_producto", "categoria", "precio_venta"]].head(5)
```

| | nombre_producto | categoria | precio_venta |
|---|---|---|---|
| 90 | Armario Sol XL | Muebles | 1207.99 |
| 85 | Sofá Boreal Compact | Muebles | 1142.37 |
| 31 | Cama Nórdico 3 plazas | Muebles | 1136.89 |
| 4 | Cama Sol 120cm | Decoración | 1131.94 |
| 65 | Sofá Atlas 3 plazas | Muebles | 1087.01 |

> **Pruébalo.** Fíjate en la cuarta fila. ¿Una **cama** en la categoría **Decoración**? Era el producto que aparecía como `decoración` en minúscula. Al unificar el texto lo hemos metido en Decoración, pero el problema real es que estaba **mal clasificado** desde el origen. Limpiar datos exige mirar con ojos de negocio, no solo de programador.

## Un gráfico en una línea

pandas dibuja gráficos directamente con matplotlib:

```python
productos["categoria"].value_counts().plot(kind="bar", title="Productos por categoría")
```

> **Pruébalo.** Cambia `kind="bar"` por `kind="barh"` (barras horizontales) o por `kind="pie"` (tarta). Después dibuja el margen medio por categoría del apartado anterior.

## Práctica guiada: las tiendas

> **Pruébalo (en parejas, 10 minutos).** Carga `datos/tiendas.csv` en un DataFrame llamado `tiendas` y responde:
>
> 1. ¿Cuántas filas y columnas tiene?
> 2. ¿Cuáles son las tres ubicaciones con más metros cuadrados? ¿Tiene sentido comparar todas entre sí?
> 3. ¿Cuántas ubicaciones están en estado `Activa`?
> 4. Usa `tiendas["store_id"].duplicated().sum()` para buscar códigos de tienda repetidos. ¿Cuántos encuentra? Repite después con `tiendas["store_id"].str.strip().duplicated().sum()`. ¿Por qué cambia el resultado?
> 5. Cuenta las tiendas por `region` con `value_counts()`. ¿Ves algo raro?

<details markdown>
<summary>Ver soluciones</summary>

```python
tiendas = pd.read_csv("datos/tiendas.csv")

# 1
tiendas.shape                      # (8, 19)

# 2
tiendas.sort_values("metros_cuadrados", ascending=False)[["nombre_tienda", "metros_cuadrados"]].head(3)

# 3
tiendas["estado"].value_counts()   # Activa: 7, Planificada: 1

# 4
tiendas["store_id"].duplicated().sum()               # 0
tiendas["store_id"].str.strip().duplicated().sum()   # 1

# 5
tiendas["region"].value_counts()
```

2. La primera es **FraSoHome eCommerce / Almacén Central** (5.200 m²), un almacén, no una tienda. No tiene sentido compararlo con las tiendas: habría que filtrar por `canal == "FISICO"`. Después vienen Barcelona Eixample (2.100 m²) y Madrid Centro (1.850 m²).
3. Hay 7 en estado `Activa`, pero **no son 7 tiendas**: una es el almacén online y otra es un duplicado de Valencia Ruzafa. FraSoHome tiene 5 tiendas físicas abiertas.
4. El duplicado de Valencia tiene el código `"S003 "`, **con un espacio al final**. Para Python, `"S003"` y `"S003 "` son textos distintos. Al quitar los espacios con `.str.strip()`, aparece el duplicado.
5. Aparecen `Levante` y `LEVANTE` como regiones distintas: el mismo problema de mayúsculas que con las categorías.

</details>

> **Idea clave.** Casi todo lo que has encontrado hoy (números guardados como texto, mayúsculas distintas, espacios de más, duplicados, datos que faltan, valores imposibles) son problemas **reales** de los datos de las empresas. Saber detectarlos es una de las habilidades más valiosas de cualquier profesional de datos.

Guarda el notebook y haz commit y **Sync Changes**.

---

[← Anterior: NumPy](07-numpy.md) · [Índice de la sesión](README.md) · [Siguiente: Conexión con la base de datos y cierre →](09-conexion-y-cierre.md)

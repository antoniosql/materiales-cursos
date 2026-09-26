# 3 · Markdown

[Inicio](../README.md) › [Sesión 2](README.md) › Markdown

**Tiempo aproximado:** 20 minutos

## La pregunta de Marta

> *"Tus programas funcionan, pero cuando se los paso a mi equipo nadie sabe para qué sirve cada uno ni cómo usarlo. ¿Puedes dejar alguna explicación?"*

Todo programa necesita **documentación**: qué hace, cómo se usa, qué datos necesita. Y hoy en día, esa documentación se escribe casi siempre en **Markdown**.

## Ya estás leyendo Markdown

Estos materiales que tienes delante están escritos en Markdown. Los títulos, las negritas, las tablas, los bloques de código y los enlaces que ves son archivos de **texto plano** con unas pocas marcas sencillas, que una herramienta convierte después en la página web que estás leyendo.

**Markdown** es un **lenguaje de marcado ligero**: una forma de dar formato a un texto usando símbolos normales del teclado (`#`, `*`, `-`...), en lugar de botones como en Word. Lo creó John Gruber en 2004 con una idea clara: que el texto se pudiera **leer bien incluso sin convertirlo**.

Compara la misma ficha de producto escrita en Markdown, tal y como la escribes, y tal y como se ve una vez convertida:

````markdown
## Sofá Aurora 160cm

Sofá de **lino beige** de la marca *UrbanHome*.

- Categoría: Muebles
- Precio de venta: 221,99 €
- Estado: `Activo`
````

> ## Sofá Aurora 160cm
>
> Sofá de **lino beige** de la marca *UrbanHome*.
>
> - Categoría: Muebles
> - Precio de venta: 221,99 €
> - Estado: `Activo`

Incluso sin convertir, el texto de la izquierda se entiende perfectamente. Esa es la gracia de Markdown.

## Por qué es tan importante hoy

| Dónde | Para qué |
|---|---|
| **GitHub y cualquier proyecto de software** | Cada proyecto tiene un archivo `README.md` que explica qué es y cómo usarlo. GitHub lo muestra automáticamente como portada del proyecto |
| **Notebooks de Jupyter** | Las celdas de texto que acompañan al código se escriben en Markdown |
| **Documentación técnica y wikis** | Herramientas de documentación, wikis corporativas y aplicaciones de notas como Obsidian o Notion usan Markdown |
| **Inteligencia artificial** | ChatGPT, Claude y Copilot **responden en Markdown** (por eso sus respuestas tienen títulos, listas y tablas). Las instrucciones que se dan a los asistentes y agentes de IA también suelen escribirse en archivos Markdown, y es el formato preferido para darles documentos que leer |
| **Webs y blogs** | Muchas webs se generan a partir de archivos Markdown, como estos materiales |

Además, al ser **texto plano**, un archivo Markdown:

- Se abre con **cualquier** editor, en cualquier sistema, hoy y dentro de 30 años.
- Ocupa muy poco.
- Se puede **versionar con Git** línea a línea, como el código. Lo verás en el [siguiente apartado](04-git-y-github.md).

> **Idea clave.** Tratar la documentación **como si fuera código** (texto plano, junto al código, con su historial de versiones) es una práctica muy extendida que se conoce como *docs as code*. Markdown es la pieza que lo hace posible.

## La sintaxis esencial

Con estas marcas cubrirás el 95 % de lo que necesitas:

| Quiero... | Escribo | Resultado |
|---|---|---|
| Un título | `# Título`, `## Subtítulo`, `### Apartado` | Títulos de nivel 1, 2 y 3 |
| Negrita | `**texto**` | **texto** |
| Cursiva | `*texto*` | *texto* |
| Código dentro de una frase | `` `print()` `` | `print()` |
| Un enlace | `[FraSoHome](https://ejemplo.com)` | [FraSoHome](https://ejemplo.com) |
| Una imagen | `![Logo](logo.png)` | La imagen `logo.png` |
| Una lista | `- elemento` en cada línea | • elemento |
| Una lista numerada | `1. paso` en cada línea | 1. paso |
| Una cita | `> texto` | Texto destacado, como los recuadros de estos materiales |
| Una línea separadora | `---` | Una línea horizontal |

### Bloques de código

Para mostrar varias líneas de código, se encierran entre tres comillas invertidas (`` ` ``, la tecla junto a la `P` en el teclado español, que se escribe pulsándola seguida de la barra espaciadora). Después de las tres primeras se indica el lenguaje, y así se colorea correctamente:

````markdown
```python
def calcular_importe(cantidad, precio):
    return cantidad * precio
```
````

### Tablas

Las columnas se separan con `|` y la segunda línea, con guiones, separa la cabecera del resto:

````markdown
| Tienda | Ciudad | m² |
|---|---|---|
| FraSoHome Madrid Centro | Madrid | 1850 |
| FraSoHome Barcelona Eixample | Barcelona | 2100 |
````

| Tienda | Ciudad | m² |
|---|---|---|
| FraSoHome Madrid Centro | Madrid | 1850 |
| FraSoHome Barcelona Eixample | Barcelona | 2100 |

No hace falta que las columnas queden alineadas en el texto: la tabla se verá bien igualmente.

### Listas de tareas

En GitHub y en muchas herramientas puedes crear casillas:

````markdown
- [x] Instalar Python
- [ ] Publicar mi primer repositorio
````

> **Cuidado.** Deja siempre una **línea en blanco** antes y después de títulos, listas, tablas y bloques de código. Es el error más frecuente: sin esa línea, muchas herramientas no reconocen el formato.

> **Para curiosos.** Hay varias "variantes" de Markdown. La más extendida es **GitHub Flavored Markdown** (GFM), que añade tablas, listas de tareas y otras cosas al Markdown original. Es la que se usa en estos materiales.

## Markdown en VS Code

VS Code entiende Markdown sin instalar nada:

1. Crea un archivo con extensión **`.md`**.
2. Escribe en él.
3. Pulsa `Ctrl + Shift + V` (Windows) o `Cmd + Shift + V` (Mac) para abrir la **vista previa**. También puedes pulsar `Ctrl + K` y después `V` (`Cmd + K`, `V` en Mac) para verla **al lado** mientras escribes.

## Práctica: el README de tu proyecto

> **Pruébalo (10 minutos).** En tu carpeta `curso-python`, crea un archivo llamado **`README.md`** (en mayúsculas, así lo reconocerá GitHub) que documente tu trabajo para el equipo de Marta. Debe incluir:
>
> 1. Un **título** con el nombre del proyecto.
> 2. Un **párrafo** que explique para qué sirve, con alguna palabra en **negrita**.
> 3. Una **lista** con los programas que has creado y qué hace cada uno (por ejemplo, `margen.py` o `stock.py`).
> 4. Una **tabla** con los productos que has usado y sus precios.
> 5. Un **bloque de código** que muestre cómo se ejecuta un programa desde la terminal.
> 6. Un **enlace** a la web de Python.
>
> Usa la vista previa para comprobar que todo se ve bien.

<details markdown>
<summary>Ver un ejemplo</summary>

````markdown
# Herramientas de análisis para FraSoHome Madrid Centro

Programas en Python para ayudar a la tienda de **Madrid Centro** a calcular
márgenes, controlar el stock y preparar tickets.

## Programas

- `margen.py`: calcula el margen en euros y en porcentaje de un producto.
- `stock.py`: indica si hay que reponer un producto.
- `ticket.py`: calcula el total de un ticket con varios productos.

## Productos de ejemplo

| Producto | Precio de venta | Coste |
|---|---|---|
| Sofá Aurora 160cm | 221,99 € | 143,47 € |
| Cuadro Atlas | 31,63 € | 21,79 € |

## Cómo se usa

Abre una terminal en esta carpeta y ejecuta:

```text
python ticket.py
```

Necesitas tener instalado [Python](https://www.python.org).
````

</details>

Guarda bien este `README.md`: en el siguiente apartado se convertirá en la **portada** de tu primer proyecto publicado en GitHub.

---

[← Anterior: Funciones y módulos](02-funciones-y-modulos.md) · [Índice de la sesión](README.md) · [Siguiente: Git y GitHub →](04-git-y-github.md)

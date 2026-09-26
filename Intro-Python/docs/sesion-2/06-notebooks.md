# 6 · Notebooks

[Inicio](../README.md) › [Sesión 2](README.md) › Notebooks

**Tiempo aproximado:** 10 minutos

## Código, explicaciones y resultados en un solo documento

Hasta ahora has escrito **scripts**: archivos `.py` que se ejecutan de principio a fin. Para analizar datos se usa mucho otra forma de trabajar: los **notebooks** (cuadernos).

Un **notebook** es un documento, con extensión **`.ipynb`**, dividido en **celdas**:

- **Celdas de código**: se ejecutan de una en una y su resultado aparece justo debajo, en el propio documento.
- **Celdas de texto**, escritas en **Markdown**: sirven para explicar qué haces y por qué.

El resultado se parece a un informe que, además, se puede ejecutar. Por eso los notebooks son la herramienta habitual para explorar datos y para compartir análisis.

| | Script `.py` | Notebook `.ipynb` |
|---|---|---|
| Organización | Un archivo de instrucciones | Celdas de código y de texto |
| Ejecución | Todo, de principio a fin, cada vez | Celda a celda, en el orden que tú decidas |
| Resultados | En la terminal, y desaparecen | Debajo de cada celda, y se guardan en el documento |
| Explicaciones | Comentarios `#` | Celdas de Markdown |
| Ideal para | Programas que se ejecutan una y otra vez | Explorar datos, probar ideas y contar un análisis |

## Crear tu primer notebook

> **Pruébalo.**
>
> 1. Pulsa `Ctrl + Shift + P` (`Cmd + Shift + P` en Mac) y ejecuta **Create: New Jupyter Notebook**. Si VS Code te propone instalar la extensión **Jupyter** de Microsoft, acepta.
> 2. Arriba a la derecha, pulsa **Select Kernel** y elige **Python Environments → .venv**. El **kernel** es el Python que ejecutará las celdas; tiene que ser el de tu entorno, que es donde están instalados los paquetes.
> 3. Guarda el notebook como `ticket.ipynb`.
> 4. En la primera celda escribe:
>
>    ```python
>    producto = "Cuadro Atlas"
>    cantidad = 2
>    precio = 31.63
>    ```
>
> 5. Pulsa `Shift + Intro` para ejecutarla. La celda no muestra nada, pero las variables ya existen en el kernel.
> 6. En la celda siguiente escribe solo esto y ejecútala:
>
>    ```python
>    cantidad * precio
>    ```
>
>    Debajo aparece `63.26`. En un notebook, **la última línea de una celda se muestra sola**, sin `print`.

## Celdas de Markdown

> **Pruébalo.** Pasa el ratón entre dos celdas y pulsa **+ Markdown**. Escribe:
>
> ```markdown
> ## Ticket de Madrid Centro
>
> Cálculo del importe de un ticket con **dos Cuadro Atlas**.
> ```
>
> Pulsa `Shift + Intro`: el texto se muestra con formato. Todo lo que aprendiste en el [apartado 3](03-markdown.md) funciona aquí.

## La trampa del orden

Las variables viven en el **kernel**, no en las celdas. El kernel recuerda todo lo que has ejecutado, **en el orden en que lo ejecutaste**, no en el orden en que aparece en pantalla.

> **Pruébalo.**
>
> 1. Añade una celda con `importe = cantidad * precio` y ejecútala.
> 2. Añade otra con `importe` y ejecútala: muestra `63.26`.
> 3. **Vuelve a la primera celda**, cambia `cantidad = 2` por `cantidad = 4` y ejecuta **solo esa celda**.
> 4. Ejecuta otra vez la celda que muestra `importe`. ¿Sigue diciendo `63.26`? ¿Por qué?

<details markdown>
<summary>Ver explicación</summary>

`importe` se calculó cuando `cantidad` valía 2 y nadie lo ha vuelto a calcular. Has cambiado `cantidad`, pero la celda que calcula `importe` no se ha vuelto a ejecutar. El notebook muestra un resultado **desactualizado** que no corresponde con el código que ves en pantalla.

</details>

> **Idea clave.** Antes de dar por bueno un notebook, pulsa **Restart** (reiniciar el kernel) y después **Run All** (ejecutar todo). Si funciona de arriba abajo con el kernel recién reiniciado, el resultado es fiable.

> **Pruébalo.** Pulsa **Restart** y después **Run All** en la barra superior del notebook. Ahora `importe` vale `126.52`.

Guarda el notebook y haz commit en Git con el mensaje `Añade el notebook del ticket`. Los notebooks también se ven en GitHub, con sus resultados.

---

[← Anterior: Paquetes y entornos virtuales](05-paquetes-y-entornos-virtuales.md) · [Índice de la sesión](README.md) · [Siguiente: NumPy →](07-numpy.md)

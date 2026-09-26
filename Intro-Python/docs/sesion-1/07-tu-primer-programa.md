# 7 · Tu primer programa

[Inicio](../README.md) › [Sesión 1](README.md) › Tu primer programa

**Tiempo aproximado:** 10 minutos

## Un mensaje para Marta

Vas a escribir tu primer programa. Será muy sencillo: un saludo. Lo importante hoy no es lo que hace, sino **el ciclo** que vas a repetir miles de veces a partir de ahora: **escribir → guardar → ejecutar → mirar el resultado**.

## Paso a paso

> **Pruébalo.**
>
> 1. En el Explorador de VS Code (a la izquierda), pasa el ratón sobre `CURSO-PYTHON` y pulsa el icono de **New File** (una hoja con un +).
> 2. Llámalo `hola.py` y pulsa Intro. La terminación **`.py`** le dice al ordenador que es un archivo de Python.
> 3. Escribe en el archivo estas líneas:
>
>    ```python
>    # Mi primer programa en Python
>    print("Hola, FraSoHome")
>    print("Hoy empiezo en el equipo de datos")
>    ```
>
> 4. **Guarda** con `Ctrl + S` (Windows) o `Cmd + S` (Mac).
> 5. Pulsa el botón **▶** (*Run Python File*) arriba a la derecha.

En la terminal de abajo debería aparecer:

```text
Hola, FraSoHome
Hoy empiezo en el equipo de datos
```

**Enhorabuena: acabas de escribir y ejecutar tu primer programa en Python.**

> **Cuidado.** Si al pulsar ▶ VS Code te pide **seleccionar un intérprete** (*Select Interpreter*), elige el que pone **Python 3.14**. Solo lo pregunta la primera vez.

> **Cuidado.** Si el nombre del archivo en la pestaña tiene un **punto blanco** (●), significa que hay cambios **sin guardar**. Python ejecuta lo que hay guardado en el archivo, no lo que ves en pantalla. Acostúmbrate a guardar siempre antes de ejecutar.

## Qué ha pasado

Vamos línea a línea:

| Línea | Qué es |
|---|---|
| `# Mi primer programa en Python` | Un **comentario**. Todo lo que va detrás de `#` es una nota para personas: Python lo ignora |
| `print("Hola, FraSoHome")` | Una **instrucción**. `print` muestra en pantalla lo que pongas entre los paréntesis |
| `"Hola, FraSoHome"` | Un **texto**. Los textos van siempre entre comillas, simples (`'...'`) o dobles (`"..."`) |

Python ha leído el archivo **de arriba abajo** y ha ejecutado las instrucciones **en orden**. Por eso el saludo aparece antes que la segunda frase.

## Otra forma de ejecutar: desde la terminal

El botón ▶ es cómodo, pero por dentro lo que hace VS Code es escribir una orden en la terminal. Tú también puedes hacerlo:

> **Pruébalo.** En la terminal escribe (en Mac, `python3`):
>
> ```text
> python hola.py
> ```

Es la orden "Python, ejecuta el archivo `hola.py`". El resultado es el mismo.

> **Cuidado.** Para que funcione, la terminal debe estar **en la misma carpeta** que el archivo. Si ves un error como `can't open file 'hola.py'`, usa `pwd` para ver dónde estás y `cd` para ir a `curso-python`.

## Cambia algo

> **Pruébalo.** Sigue el método: predice, ejecuta, cambia, explica.
>
> 1. Añade una tercera línea con `print` que diga tu nombre.
> 2. Cambia el orden de las líneas. ¿Qué pasa?
> 3. Pon `#` delante de una de las líneas con `print`. ¿Qué pasa? ¿Por qué?
> 4. Quita las comillas de uno de los textos y ejecuta. Algo va a fallar. No te preocupes: en el [apartado 11](11-cuando-algo-falla.md) aprenderemos a leer esos mensajes.

Puedes comparar tu archivo con el ejemplo [01_hola.py](ejemplos/01_hola.py).

---

[← Anterior: Carpetas y terminal](06-carpetas-y-terminal.md) · [Índice de la sesión](README.md) · [Siguiente: Tipos de datos y variables →](08-tipos-de-datos-y-variables.md)

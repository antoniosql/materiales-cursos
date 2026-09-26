# 6 · Carpetas y terminal

[Inicio](../README.md) › [Sesión 1](README.md) › Carpetas y terminal

**Tiempo aproximado:** 10 minutos

## Un sitio para tu trabajo

Marta guarda los papeles de la tienda en carpetas: facturas, pedidos, turnos. Nosotros haremos lo mismo con nuestros programas. Todo lo que escribas en el seminario vivirá en **una única carpeta**.

> **Pruébalo.** Crea tu carpeta de trabajo:
>
> 1. Abre el **Explorador de archivos** (Windows) o el **Finder** (Mac).
> 2. Entra en **Documentos**.
> 3. Crea una carpeta nueva llamada `curso-python`, sin espacios ni tildes.

> **Cuidado.** Evita los espacios, las tildes y la "ñ" en los nombres de carpetas y archivos de código. Funcionan casi siempre, pero cuando fallan cuesta mucho descubrir por qué. Usa guiones (`curso-python`) o guiones bajos (`mi_programa.py`).

## Abrir la carpeta en VS Code

1. En VS Code, ve al menú **File → Open Folder...** (en Mac, **File → Open...**).
2. Selecciona tu carpeta `curso-python` y pulsa **Seleccionar carpeta** o **Abrir**.
3. VS Code te preguntará si **confías en los autores** de los archivos de la carpeta. Como la has creado tú, responde **Yes, I trust the authors**.

A la izquierda verás el nombre de la carpeta, todavía vacía. Esa zona se llama **Explorador** y muestra los mismos archivos que ves en el Explorador de Windows o en el Finder, pero dentro de VS Code.

## La terminal dentro de VS Code

VS Code tiene una terminal incorporada, así que no hace falta abrir otra ventana.

> **Pruébalo.** Abre el menú **Terminal → New Terminal**. Aparecerá un panel en la parte inferior con un texto parecido a este:
>
> - Windows: `PS C:\Users\TuNombre\Documents\curso-python>`
> - Mac: `tunombre@MacBook curso-python %`

Ese texto se llama **prompt**. Significa "estoy esperando una orden" y además te dice **en qué carpeta estás**. Fíjate: la terminal ya está dentro de `curso-python`.

> **Cuidado.** Cuando copies órdenes de estos materiales, **no copies el prompt**. Escribe solo lo que viene después.

## Cuatro órdenes básicas

Estas cuatro órdenes funcionan igual en Windows (PowerShell) y en Mac:

| Orden | Qué hace | Ejemplo |
|---|---|---|
| `pwd` | Te dice en qué carpeta estás (*print working directory*) | `pwd` |
| `ls` | Muestra lo que hay en la carpeta (*list*) | `ls` |
| `mkdir` | Crea una carpeta nueva (*make directory*) | `mkdir pruebas` |
| `cd` | Entra en una carpeta (*change directory*). `cd ..` sube a la carpeta de arriba | `cd pruebas` |

> **Pruébalo.** Escribe estas órdenes una a una, pulsando Intro después de cada una, y observa el resultado:
>
> ```text
> pwd
> mkdir pruebas
> ls
> cd pruebas
> pwd
> cd ..
> pwd
> ```
>
> Ahora mira el Explorador de la izquierda en VS Code: ¿aparece la carpeta `pruebas`?

> **Idea clave.** La terminal y el Explorador muestran **las mismas carpetas y archivos**. Solo cambia la forma de manejarlos: con el ratón o escribiendo órdenes.

## Dos lugares distintos: la terminal y Python

Ahora prueba a escribir en la terminal:

```text
python
```

(En Mac, `python3`.)

El prompt cambia a `>>>`. Ya no estás hablando con la terminal, **estás hablando directamente con Python**. Es el modo REPL: Python lee cada línea que escribes, la ejecuta y te enseña el resultado.

> **Pruébalo.** Escribe después de `>>>`:
>
> ```python
> 2 * 31.63
> ```
>
> Python responde `63.26`. Es el cálculo de los dos cuadros de Marta. Ahora escribe `exit()` y pulsa Intro para volver a la terminal.

| Si ves... | Estás hablando con... | Ahí se escriben... |
|---|---|---|
| `PS C:\...>` o `... %` | La **terminal** | Órdenes como `pwd`, `ls` o `python --version` |
| `>>>` | **Python** (REPL) | Código Python, como `2 * 31.63` |

> **Cuidado.** Un error muy común al principio es escribir órdenes de la terminal dentro de `>>>`, o código Python en la terminal. Si algo falla de forma rara, **mira primero el prompt**.

El REPL es útil para probar cosas rápidas, pero lo que escribes se pierde al cerrarlo. Para guardar tu trabajo usaremos **archivos**, que es justo lo que haremos después del descanso.

---

## Descanso (15 minutos)

Antes de irte, comprueba que tienes:

- [ ] La carpeta `curso-python` abierta en VS Code.
- [ ] La terminal de VS Code funcionando.

Si algo no funciona, este es el momento de decírselo al profesor.

---

[← Anterior: Instalación guiada](05-instalacion-guiada.md) · [Índice de la sesión](README.md) · [Siguiente: Tu primer programa →](07-tu-primer-programa.md)

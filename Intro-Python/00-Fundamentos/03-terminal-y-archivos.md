# 3. Archivos, carpetas, terminal y CLI

## Dónde está tu trabajo

Una carpeta agrupa archivos. Un **proyecto** es la carpeta donde reunimos el código y sus recursos. Un **repositorio** conserva archivos e historial de cambios; Git es una herramienta para gestionarlo y GitHub es el servicio donde se aloja este curso. Puedes descargarlo sin instalar Git.

Una **ruta absoluta** parte de la raíz del sistema, como `C:\Users\Ana\curso\hola.py` o `/Users/ana/curso/hola.py`. Una **ruta relativa**, como `ejemplos/hola.py`, parte de la carpeta de trabajo actual. `.` significa la carpeta actual y `..` la carpeta superior. Si hay espacios, encierra la ruta entre comillas.

La extensión indica el tipo de archivo: `.py` contiene código Python; `.md`, texto Markdown; `.ipynb`, un notebook; `.csv`, datos tabulares. Guardar `hola.py.txt` no crea el archivo esperado. En VS Code verás el nombre completo.

## Abrir una terminal

En Windows, abre Inicio, escribe **PowerShell** y ábrelo. En macOS, pulsa **Cmd+Espacio**, escribe **Terminal** y pulsa Intro. Dentro de VS Code utiliza **Terminal > New Terminal** (Terminal > Nueva terminal).

El texto que aparece antes de escribir es el **prompt**, un indicador de que el programa está esperando. Su aspecto puede variar. No copies ese indicador al pegar comandos.

| Si ves algo parecido a… | Estás en… | Puedes escribir… |
|---|---|---|
| `PS C:\Users\Ana>` | PowerShell | `Get-Location` |
| `ana@Mac ~ %` o `$` | Shell de macOS | `pwd` |
| `>>>` | REPL de Python | `print("Hola")` |

`python --version` es una orden para la **shell**. `print("Hola")` es código para **Python**. Si ejecutas la primera dentro de `>>>`, Python intentará interpretarla como código y fallará. Escribe `exit()` para volver a la shell. Más adelante entrarás de nuevo usando `py` o `python3`.

## Práctica de navegación

Todavía no necesitas Python. Crea una carpeta llamada `practica-terminal` dentro de una ubicación tuya, por ejemplo Documentos, utilizando el Explorador de Windows o Finder de macOS. Ábrela y copia su ruta. Abre una terminal y usa `cd` seguido de esa ruta entre comillas. En macOS puedes arrastrar la carpeta a Terminal después de escribir `cd `.

| Acción | Windows: PowerShell | macOS: Terminal |
|---|---|---|
| Saber dónde estás | `Get-Location` | `pwd` |
| Ver archivos y carpetas | `Get-ChildItem` | `ls` |
| Entrar en una carpeta | `cd "ruta de la carpeta"` | `cd "ruta de la carpeta"` |
| Crear una subcarpeta | `mkdir ejercicios` | `mkdir ejercicios` |
| Entrar en ella | `cd ejercicios` | `cd ejercicios` |
| Volver a la superior | `cd ..` | `cd ..` |

Sustituye `ruta de la carpeta` por tu ruta real; las otras órdenes se pueden copiar. Si `ejercicios` ya existe, pasa al siguiente paso. Pulsa Intro después de cada orden.

**Comprueba:** la subcarpeta debe aparecer también en el Explorador o Finder. La terminal y el explorador muestran los mismos archivos; cambia la forma de interactuar con ellos.

## Comandos y argumentos

En `python --version`, `python` es el programa y `--version` una opción. En `python hola.py`, `hola.py` es el archivo que queremos ejecutar. **PATH** es la lista de carpetas donde el sistema busca programas al escribir su nombre; no es la carpeta donde guardas tu curso. Las guías de instalación comprobarán ambas cosas por separado.

Referencias: [terminal integrada de VS Code](https://code.visualstudio.com/docs/terminal/basics), [CLI de VS Code](https://code.visualstudio.com/docs/configure/command-line) y [intérprete de Python](https://docs.python.org/3/tutorial/interpreter.html).

[Anterior](02-herramientas.md) · [Siguiente: comprobación](04-comprueba-lo-aprendido.md)

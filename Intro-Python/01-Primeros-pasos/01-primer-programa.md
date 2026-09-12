# 1. Tu primer programa, desde una carpeta vacía

## Descargar y abrir el curso sin saber Git

1. Abre [materiales-cursos en GitHub](https://github.com/antoniosql/materiales-cursos).
2. En la raíz del repositorio pulsa **Code > Download ZIP**. La descarga incluye otros cursos y puede ser grande.
3. Extrae el ZIP: en Windows, **Extraer todo**; en macOS, abre el ZIP con doble clic. No trabajes dentro del archivo comprimido.
4. En VS Code selecciona **File > Open Folder…** y abre la carpeta `Intro-Python` dentro de `materiales-cursos-main`. Debes ver `README.md`, `Requisitos` y `Notebooks` en la barra lateral.
5. Si aparece un aviso de confianza de carpeta, revisa que sea la copia de este repositorio antes de habilitar la ejecución.

Si ya sabes Git, la alternativa es clonar el repositorio y abrir su subcarpeta `Intro-Python`. Git no es un requisito para esta ruta.

## Crear el archivo

En el Explorador de VS Code crea una carpeta `mis-ejercicios`. Dentro crea un archivo **`hola.py`** con este contenido:

```python
print("Hola, Python")
print("Estoy ejecutando mi primer programa")
```

Guarda con **Ctrl+S** (Windows) o **Cmd+S** (macOS). Comprueba que se llama `hola.py`, no `hola.py.txt`. Las comillas deben ser rectas, como las del ejemplo; no las comillas tipográficas de un procesador de textos.

`print` es una función: una operación a la que damos datos entre paréntesis. Las comillas delimitan un texto; no se mostrarán en la salida.

## Ejecutar desde VS Code

Selecciona el intérprete con **Python: Select Interpreter**. Con `hola.py` abierto, pulsa **Run Python File in Terminal**, el botón de ejecución del editor, o busca **Python: Run Python File in Terminal** en la paleta.

Resultado esperado:

```text
Hola, Python
Estoy ejecutando mi primer programa
```

Puede aparecer también el comando que VS Code ha utilizado. La salida de nuestro programa son las dos líneas anteriores.

## Ejecutar el mismo archivo desde la terminal

Abre **Terminal > New Terminal**. Comprueba que estás en `Intro-Python` con `Get-Location` (PowerShell) o `pwd` (macOS). Usa una de estas órdenes, según tu instalación:

Windows:

```powershell
py -3.14 mis-ejercicios/hola.py
```

macOS:

```bash
python3.14 mis-ejercicios/hola.py
```

Verás el mismo resultado. Si has instalado otra versión, utiliza el comando que verificaste en tu equipo. No ejecutes el archivo con doble clic: la ventana puede cerrarse antes de que veas la salida.

## Probar la sesión interactiva

En la terminal escribe `py -3.14` (Windows) o `python3.14` (macOS), sin nombre de archivo. Aparecerá `>>>`. Escribe, una línea cada vez:

```python
2 + 3
print("Prueba interactiva")
exit()
```

Verás `5`, un mensaje y regresarás a la shell. No copies `>>>` ni escribas comandos de PowerShell dentro de esa sesión. La REPL sirve para pruebas breves; el archivo conserva las instrucciones para repetirlas.

**Tu turno:** añade una tercera línea con tu nombre, guarda y vuelve a ejecutar. Luego cambia solo el texto. Si la salida no cambia, comprueba qué archivo estás ejecutando y si lo has guardado.

Fuentes: [ejecución en VS Code](https://code.visualstudio.com/docs/python/run) y [uso del intérprete](https://docs.python.org/3/tutorial/interpreter.html).

[Siguiente: variables](02-valores-y-variables.md) · [Índice](README.md)

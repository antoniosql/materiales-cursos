# Entorno virtual y paquetes, paso a paso

Haz esta página después de los [primeros programas](../01-Primeros-pasos/README.md), cuando necesites notebooks o bibliotecas. Abre **la carpeta `Intro-Python`** en VS Code y **Terminal > New Terminal**. Comprueba con `Get-Location` (PowerShell) o `pwd` (macOS) que estás en ella; debe contener `requirements-inicio.txt`.

## 1. Entender qué vamos a crear

Una biblioteca aporta código reutilizable. `pip` instala paquetes en un entorno de Python; `import` permite utilizar módulos desde un programa. Por ejemplo, se instala `scikit-learn`, pero se importa `sklearn`. Una extensión de VS Code se instala en el editor, no mediante pip.

Un entorno virtual aísla los paquetes de un proyecto. Lo llamaremos `.venv`. No es una máquina virtual ni una nueva carpeta para tus ejercicios. Tus archivos se guardan **fuera** de `.venv`.

## 2. Crear el entorno —una vez por copia del curso—

Si ya existe `.venv`, reutilízalo y pasa a la comprobación. Con la instalación de estas guías:

Windows, PowerShell:

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip --version
```

macOS:

```bash
python3.14 -m venv .venv
./.venv/bin/python -m pip --version
```

`-m venv` pide a Python ejecutar su módulo `venv`. La salida de pip debe mostrar una ruta dentro de `.venv`. Si elegiste otra versión instalada, sustituye el comando de creación por el correspondiente a ella.

## 3. Instalar solo lo necesario

Elige **una fila**, según el bloque al que vayas a entrar. Ejecuta el comando desde `Intro-Python`.

| Bloque | Archivo | Qué instala |
|---|---|---|
| Primer notebook | `requirements-inicio.txt` | `ipykernel` |
| Análisis con datos | `requirements-datos.txt` | Lo anterior, NumPy, Pandas, Matplotlib, Seaborn, SciPy, scikit-learn, mysql-connector-python y python-dotenv |

Windows, primer notebook:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-inicio.txt
```

macOS, primer notebook:

```bash
./.venv/bin/python -m pip install -r requirements-inicio.txt
```

Para el bloque de datos, ejecuta el mismo comando cambiando el nombre por `requirements-datos.txt`. `-r` significa «leer la lista de paquetes de este archivo». Las listas no fijan versiones: describen dependencias de los ejemplos, **no son un entorno congelado ni una garantía de compatibilidad de los materiales antiguos**. El docente debe preparar y validar su entorno de análisis antes de impartirlo.

## 4. Elegir el entorno en VS Code

Ejecuta **Python: Select Interpreter** desde la paleta y selecciona `.venv`. Si no aparece, utiliza **Enter interpreter path…** y elige:

- Windows: `.venv/Scripts/python.exe` dentro del curso.
- macOS: `.venv/bin/python` dentro del curso.

Para un notebook, selecciona **también su kernel** como explica [Jupyter](Jupyter.md).

## 5. Activación opcional

Los comandos anteriores usan la ruta explícita y funcionan sin activar el entorno. Activarlo permite escribir simplemente `python` en esa terminal:

Windows, PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS:

```bash
source .venv/bin/activate
```

Después comprueba:

```bash
python -c "import sys; print(sys.executable)"
python -m pip --version
```

Ambas rutas deben pertenecer a `.venv`. Sal con `deactivate`. En una nueva terminal comprueba el entorno otra vez: la activación pertenece a cada sesión.

**Si PowerShell bloquea `Activate.ps1`**, continúa usando `.\.venv\Scripts\python.exe` como arriba. No necesitas modificar la política de ejecución del equipo para realizar el curso.

## 6. Correcciones de la guía anterior

- `sqlite3` forma parte de la biblioteca estándar en las instalaciones oficiales usadas aquí: no ejecutes `pip install sqlite3`.
- Instala `scikit-learn`; en el código se utiliza `import sklearn`.
- `pip` viene normalmente con Python y con los entornos creados por `venv`; no descargues `get-pip.py` como primer paso. Consulta [pip](<Instalar PIP.md>).
- No es necesario fijar `scipy==1.2` para este curso.
- `pyodbc` y `statsmodels`, citados en las guías anteriores, no se importan en los notebooks actuales. Son ampliaciones opcionales; ODBC puede requerir controladores externos.
- En una celda Jupyter, `%pip install nombre` apunta al entorno del kernel. En una terminal usa la ruta del intérprete seguida de `-m pip`. `!pip` es sintaxis de IPython y no funciona en un archivo `.py` normal.

Fuentes: [venv](https://docs.python.org/3/library/venv.html), [guía de PyPA](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/), [instalación de scikit-learn](https://scikit-learn.org/stable/install.html), [sqlite3](https://docs.python.org/3/library/sqlite3.html) y [magias de IPython](https://ipython.readthedocs.io/en/stable/interactive/magics.html).

[Siguiente: Jupyter](Jupyter.md) · [Volver a preparación](README.md)

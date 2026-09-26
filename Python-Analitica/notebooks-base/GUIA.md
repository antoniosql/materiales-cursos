# Guía de notebooks y dependencias

Antes de los originales, completa [00_0_Primer_notebook.ipynb](00_0_Primer_notebook.ipynb). La guía de [Jupyter](../Requisitos/Jupyter.md) explica instalación, kernel y ejecución en orden.

## Condiciones de ejecución

| Notebook | Preparación y particularidades |
|---|---|
| [00_0_Primer_notebook](00_0_Primer_notebook.ipynb), nuevo | `requirements-inicio.txt`; ejemplos autocontenidos; sin red, Pandas ni MySQL durante la ejecución |
| [01_1_Markdown](01_1_Markdown.ipynb) | Texto y ejemplos de formato; las imágenes remotas necesitan red para mostrarse |
| [01_2_Notebook](01_2_Notebook.ipynb) | Kernel IPython; montaje de Drive exclusivo de Colab; comandos de sistema y magias |
| [01_3_Elementos del Lenguaje](<01_3_Elementos del Lenguaje.ipynb>) | Biblioteca estándar; una celda solicita datos con `input()` |
| [01_4_Modulos_Paquetes](01_4_Modulos_Paquetes.ipynb) | Pandas y NumPy; paquete local `paquete/`; demostraciones que instalan paquetes y escriben `requirements.txt` |
| [02_01_Repaso Basico Pandas](<02_01_Repaso Basico Pandas.ipynb>) | Pandas y NumPy; una celda descarga un CSV de Google; el resto incluye ejemplos definidos en memoria |
| [02_02_Pandas y Bases de Datos](<02_02_Pandas y Bases de Datos.ipynb>) | MySQL/Sakila, pandas, mysql-connector-python y python-dotenv |
| [03_01_Nulos y repetidos](<03_01_Nulos y repetidos.ipynb>) | Ejemplos en memoria con Pandas, NumPy y scikit-learn; tramo final con MySQL/Sakila |
| [03_02 Visualizacion](<03_02 Visualizacion.ipynb>) | MySQL/Sakila, Pandas, Matplotlib, Seaborn y SciPy para densidad; guarda un PNG |
| [04_01 EDA inicial](<04_01 EDA inicial.ipynb>) | MySQL/Sakila, Pandas y Matplotlib |
| [04_02_Codificacion de Variables](<04_02_Codificacion de Variables.ipynb>) | MySQL/Sakila, Pandas y scikit-learn |
| [04_03_Escalado de Caracteristicas](<04_03_Escalado de Caracteristicas.ipynb>) | MySQL/Sakila, Pandas y scikit-learn |
| [Laboratorio](Laboratorio.ipynb) | MySQL/Sakila y paquetes de análisis; contiene celdas que debe completar el alumno |

Instala las listas correspondientes desde [Entorno y paquetes](../Requisitos/Entorno-y-paquetes.md). Prepara las conexiones con [MySQL y Sakila](../Requisitos/MySQL-Sakila.md).

## Carpeta de trabajo del paquete de ejemplo

`01_4_Modulos_Paquetes.ipynb` importa `paquete`, que está dentro de `Notebooks`. Antes de esa demostración, comprueba la carpeta con `Path.cwd()` y sitúate en `Notebooks`. Si el kernel arrancó en `Intro-Python`, puedes ejecutar esta celda de preparación:

```python
from pathlib import Path
import os

if Path("Notebooks/paquete").is_dir():
    os.chdir("Notebooks")
print(Path.cwd())
```

La carpeta mostrada debe contener `paquete`. No guardes los ejercicios dentro del paquete ni de `.venv`.

## Notas docentes sobre el contenido conservado

Estas observaciones permiten utilizar el contenido original sin borrarlo ni reescribirlo:

- En `01_2`, omitir el montaje de Google Drive en VS Code. `%%html` debe estar en la primera línea de su celda; el comentario anterior del ejemplo histórico debe moverse en la copia de trabajo.
- En `01_3`, los nombres en mayúsculas representan constantes **por convención**, no una prohibición de reasignación. En el ejemplo de stock, `if stock < 2` incluye `stock == 1`, por lo que el `elif` siguiente no se alcanza. En el ejemplo de excepciones, la conversión de `input()` está fuera del `try`: una entrada no numérica no queda protegida por ese bloque. El material nuevo presenta ejemplos corregidos.
- En `01_4`, los comandos `!pip` y `!pip freeze > requirements.txt` son demostraciones, con efectos sobre el entorno y los archivos. Para preparar la clase utiliza las guías actuales. La función `fib` de `py/utils.py` imprime y devuelve implícitamente `None`; `fib2` devuelve una lista. Esto explica la salida adicional de `print(fib(2))`.
- En `02_02` y otros ejemplos MySQL, algunos caminos de error usan variables de conexión o cursor aunque la conexión haya fallado. Algunos convierten `cursor.column_names` después de cerrar el cursor; es necesario revisar ese comportamiento con el conector elegido. Hay concatenaciones de texto con excepciones que requieren `str(err)`. No presentar esos fragmentos como patrones robustos de gestión de conexiones.
- En `03_01`, añadir `is_duplicate` al DataFrame antes de `drop_duplicates()` cambia las columnas consideradas: dos filas antes idénticas pueden diferir por esa nueva columna. Para practicar la eliminación, indicar el `subset` de columnas originales o calcular el indicador aparte. `SimpleImputer` utiliza `strategy`; el comentario histórico sobre cambiar `axis` no describe un parámetro de ese estimador.
- Las salidas guardadas de los notebooks muestran ejecuciones históricas; no acreditan que se hayan ejecutado con el nuevo entorno. Los notebooks que usan MySQL requieren una validación de clase con datos y conexión disponibles.

El laboratorio sigue siendo una práctica para completar. No debe usarse como una prueba automática de «Run All» con resultados finales ya resueltos.

[Volver al curso](../README.md)

# 5 · Paquetes y entornos virtuales

[Inicio](../README.md) › [Sesión 2](README.md) › Paquetes y entornos virtuales

**Tiempo aproximado:** 15 minutos

## La pregunta de Marta

> *"Esto de las listas de diccionarios está muy bien para cinco productos, pero en FraSoHome tenemos más de cien en el catálogo y miles de ventas. ¿No hay algo más potente?"*

Lo hay. La biblioteca estándar de Python es muy completa, pero para analizar datos la comunidad ha creado herramientas mucho más potentes: **NumPy** para cálculo numérico, **pandas** para tablas y **matplotlib** para gráficos. No vienen con Python: hay que **instalarlas**.

## Paquetes, PyPI y `pip`

| Concepto | Qué es | Analogía |
|---|---|---|
| **Paquete** | Un conjunto de módulos que otras personas han escrito y publicado | Una caja de herramientas especializada |
| **PyPI** (*Python Package Index*, pypi.org) | El almacén público donde se publican los paquetes de Python. Tiene cientos de miles | La ferretería |
| **`pip`** | El programa que descarga e instala paquetes desde PyPI. Viene con Python | El dependiente que te trae la caja del almacén |

Instalar un paquete es tan sencillo como escribir en la terminal:

```text
pip install pandas
```

Pero antes de hacerlo hay que resolver un problema.

## El problema: proyectos que se pisan

Imagina que tienes dos proyectos en tu ordenador:

- El proyecto de márgenes de FraSoHome, que funciona con la versión 2 de pandas.
- Un proyecto nuevo que necesita la versión 3.

Si instalas los paquetes "en general", en el Python del ordenador, **solo puede haber una versión** de cada paquete. Al actualizar pandas para el proyecto nuevo, el antiguo puede dejar de funcionar.

## La solución: un entorno virtual por proyecto

Un **entorno virtual** es una carpeta dentro de tu proyecto que contiene **su propio Python y sus propios paquetes**, aislados del resto del ordenador. Cada proyecto tiene el suyo y no se pisan. Por costumbre, esa carpeta se llama **`.venv`**.

> **Idea clave.** **Un proyecto, un entorno virtual.** Nunca instales paquetes en el Python general del ordenador.

## `requirements.txt`: la lista de la compra

Para que cualquier persona pueda recrear tu entorno, se apunta en un archivo de texto llamado **`requirements.txt`** qué paquetes necesita el proyecto, uno por línea. El de este seminario es este:

```text
# Notebooks
ipykernel

# Análisis de datos
numpy
pandas
matplotlib

# Conexión con la base de datos
python-dotenv
mssql-python

# Los usarás más adelante
seaborn
scikit-learn
```

Descárgalo desde [requirements.txt](requirements.txt) y guárdalo en tu carpeta `curso-python`.

> **Idea clave.** Esto conecta con lo que acabas de aprender de Git: la carpeta **`.venv` no se sube a GitHub** (por eso estaba en el `.gitignore`), porque pesa mucho y depende de cada ordenador. Lo que se sube es **`requirements.txt`**, que ocupa unas pocas líneas y permite a cualquiera recrear el entorno.

## Crear el entorno desde VS Code

VS Code lo hace casi todo por ti:

> **Pruébalo.**
>
> 1. Con la carpeta `curso-python` abierta, pulsa `Ctrl + Shift + P` (`Cmd + Shift + P` en Mac) para abrir la **paleta de comandos**.
> 2. Escribe `Python: Create Environment` y pulsa Intro.
> 3. Elige **Venv**.
> 4. Elige el intérprete **Python 3.14**.
> 5. Marca **requirements.txt** cuando te pregunte qué dependencias instalar y pulsa **OK**.
> 6. Espera. Descargar todos los paquetes lleva unos minutos. Al terminar verás la carpeta `.venv` en el Explorador.

Cierra la terminal de VS Code y abre una nueva (**Terminal → New Terminal**). Verás `(.venv)` al principio del prompt: significa que el entorno está **activado** y que `python` y `pip` usan el Python de tu proyecto.

> **Pruébalo. Comprueba que funciona.** En la terminal escribe:
>
> ```text
> python -c "import pandas; print(pandas.__version__)"
> ```
>
> Si ves un número de versión (por ejemplo `3.0.2`), pandas está instalado en tu entorno.

## Lo mismo, desde la terminal

Esto es lo que hace VS Code por debajo. Te servirá en cualquier ordenador:

| Paso | Windows (PowerShell) | Mac (Terminal) |
|---|---|---|
| Crear el entorno | `python -m venv .venv` | `python3 -m venv .venv` |
| Activarlo | `.venv\Scripts\Activate.ps1` | `source .venv/bin/activate` |
| Instalar los paquetes | `pip install -r requirements.txt` | `pip install -r requirements.txt` |
| Ver lo que hay instalado | `pip list` | `pip list` |
| Desactivarlo | `deactivate` | `deactivate` |

> **Cuidado.** En Windows, al activar el entorno puede aparecer un error que dice que *la ejecución de scripts está deshabilitada*. Se soluciona una sola vez con esta orden:
>
> ```text
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

> **Para curiosos.** `pip freeze` muestra los paquetes instalados **con su versión exacta** (`pandas==3.0.2`). Guardar esa salida en `requirements.txt` permite reproducir un entorno idéntico, algo muy importante cuando un análisis tiene que dar el mismo resultado meses después.

## Guarda el cambio en Git

> **Pruébalo.** En Source Control verás `requirements.txt` como archivo nuevo, pero **no** la carpeta `.venv`, porque el `.gitignore` la oculta. Haz commit con el mensaje `Añade requirements.txt` y sincroniza con **Sync Changes**.

---

[← Anterior: Git y GitHub](04-git-y-github.md) · [Índice de la sesión](README.md) · [Siguiente: Notebooks →](06-notebooks.md)


<img src="https://raw.githubusercontent.com/dataging/public-resources/61263724aea5476ba5ebf38478beada519091957/logodataging.png" alt="Dataging" width="200"/>

# Introducción a Python para el análisis de datos

Materiales del curso **Introducción a Python**, orientado a personas que ya
trabajan con datos (Excel, SQL o desarrollo backend) y quieren dar el salto a
Python como herramienta de análisis.

El recorrido va de los elementos básicos del lenguaje al análisis exploratorio,
pasando por la manipulación de datos con Pandas y la limpieza previa que todo
conjunto de datos real necesita.

## Objetivos

- Manejar los elementos fundamentales del lenguaje y organizar el código en
  módulos y paquetes.
- Trabajar con Jupyter Notebooks como entorno de análisis.
- Cargar, transformar y combinar datos con Pandas, incluyendo el acceso a bases
  de datos relacionales.
- Detectar y tratar nulos y duplicados, y visualizar datos para entenderlos.
- Realizar un análisis exploratorio (EDA) completo y preparar las variables
  (codificación y escalado) para su uso posterior.

## Agenda

### 1. Introducción a Python

| Notebook | Contenido |
|---|---|
| [01_1_Markdown](<Notebooks/01_1_Markdown.ipynb>) | Sintaxis Markdown para documentar notebooks |
| [01_2_Notebook](<Notebooks/01_2_Notebook.ipynb>) | Cómo funciona un Jupyter Notebook: celdas, kernel y ejecución |
| [01_3_Elementos del Lenguaje](<Notebooks/01_3_Elementos del Lenguaje.ipynb>) | Tipos, variables, estructuras de control, funciones y colecciones |
| [01_4_Modulos_Paquetes](<Notebooks/01_4_Modulos_Paquetes.ipynb>) | Importaciones, módulos propios y paquetes |

### 2. Trabajo con datos: Pandas

| Notebook | Contenido |
|---|---|
| [02_01 Repaso Básico Pandas](<Notebooks/02_01_Repaso Basico Pandas.ipynb>) | Series y DataFrames: selección, filtrado, agregación |
| [02_02 Pandas y Bases de Datos](<Notebooks/02_02_Pandas y Bases de Datos.ipynb>) | Lectura y escritura contra una base de datos relacional |

### 3. Limpieza y preparación de datos

| Notebook | Contenido |
|---|---|
| [03_01 Nulos y repetidos](<Notebooks/03_01_Nulos y repetidos.ipynb>) | Estrategias de imputación y eliminación de duplicados |
| [03_02 Visualización](<Notebooks/03_02 Visualizacion.ipynb>) | Gráficos para explorar distribuciones y relaciones |

### 4. Análisis exploratorio (EDA)

| Notebook | Contenido |
|---|---|
| [04_01 EDA inicial](<Notebooks/04_01 EDA inicial.ipynb>) | Primer contacto con un dataset desconocido |
| [04_02 Codificación de Variables](<Notebooks/04_02_Codificacion de Variables.ipynb>) | Variables categóricas: *one-hot*, ordinal y otras codificaciones |
| [04_03 Escalado de Características](<Notebooks/04_03_Escalado de Caracteristicas.ipynb>) | Normalización y estandarización, y cuándo hace falta cada una |

### Laboratorio

- [Laboratorio.ipynb](Notebooks/Laboratorio.ipynb) — ejercicio guiado para
  practicar todo el recorrido sobre un conjunto de datos nuevo.

## Estructura del repositorio

```text
Intro-Python/
├── Notebooks/     # Notebooks del curso (demostraciones y laboratorio)
│   └── paquete/   # Paquete de ejemplo usado en el módulo de módulos y paquetes
├── py/            # Los mismos ejemplos como scripts .py, para ejecutar fuera de Jupyter
├── Requisitos/    # Guías de instalación del entorno
└── resources/     # Recursos de apoyo
```

## Requisitos

Antes de la primera sesión, prepara el entorno siguiendo las guías de
[Requisitos/](Requisitos/):

- [Instalar Python](<Requisitos/Instalar Python.md>)
- [Instalar Visual Studio Code](<Requisitos/Instalar Visual Studio Code.md>)
- [Instalar la extensión de Python para VS Code](<Requisitos/Instalar el complemento de Python.md>)
- [Instalar PIP](<Requisitos/Instalar PIP.md>)
- [Instalación de paquetes](<Requisitos/Instalación de Paquetes.md>)

Si prefieres no instalar nada en tu equipo, puedes ejecutar los notebooks en
[Google Colab](https://colab.research.google.com/).

Para los ejemplos con bases de datos se utiliza MySQL con la base de datos de
demostración *Sakila*.

**Conocimientos previos:** se parte de experiencia trabajando con datos (Excel,
SQL o desarrollo backend). No es necesario saber Python de antemano.

## Cómo usar los materiales

1. Clona el repositorio o descarga la carpeta `Notebooks/`.
2. Abre los notebooks en VS Code, Jupyter Lab o Colab.
3. Sigue el orden numérico de los ficheros: cada bloque se apoya en el anterior.

## Licencia

Materiales bajo licencia [MIT](LICENSE).

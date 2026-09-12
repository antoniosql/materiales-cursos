<img src="https://raw.githubusercontent.com/dataging/public-resources/61263724aea5476ba5ebf38478beada519091957/logodataging.png" alt="Dataging" width="200"/>

# Introducción a Python: desde cero hasta el análisis de datos

Materiales para aprender Python empezando por qué es un programa, cómo se ejecuta y qué herramientas necesitas. El recorrido continúa hasta Pandas, limpieza, visualización, análisis exploratorio y preparación de variables.

**No necesitas experiencia previa en programación, Excel o SQL para empezar.** Los bloques de análisis incorporan conceptos adicionales; los ejemplos de Sakila requieren preparación de bases de datos con el docente.

## Empieza por tu punto de partida

- **Nunca he programado:** comienza por [00-Fundamentos](00-Fundamentos/README.md), prepara el equipo y completa [01-Primeros-pasos](01-Primeros-pasos/README.md).
- **Ya programo, pero no en Python:** revisa [instalación](Requisitos/README.md) y [comprobación del entorno](Requisitos/Comprobacion.md); después entra en los notebooks del lenguaje.
- **Ya manejo Python y quiero analizar datos:** prepara [los paquetes del bloque de datos](Requisitos/Entorno-y-paquetes.md) y consulta el [mapa de notebooks y dependencias](Notebooks/GUIA.md).

## Itinerario completo

| Etapa | Material | Qué aprenderás |
|---|---|---|
| 0. Conceptos desde cero | [00-Fundamentos](00-Fundamentos/README.md) | Programa, algoritmo, lenguaje, intérprete, editor, IDE, terminal, shell, CLI, archivos y rutas |
| Preparación | [Windows](Requisitos/Windows.md) / [macOS](Requisitos/macOS.md) y [extensión Python](<Requisitos/Instalar el complemento de Python.md>) | Descargar, instalar y comprobar las herramientas |
| 1. Primeros programas | [01-Primeros-pasos](01-Primeros-pasos/README.md) | Scripts, REPL, valores, variables, entrada, decisiones, bucles, funciones, errores y depuración |
| Práctica inicial | [Ejercicios y miniproyecto](01-Primeros-pasos/05-ejercicios.md) | Resolver problemas pequeños y comprobar sus resultados |
| Puente a notebooks | [Entorno virtual](Requisitos/Entorno-y-paquetes.md), [Jupyter](Requisitos/Jupyter.md) y [primer notebook](Notebooks/00_0_Primer_notebook.ipynb) | Instalar paquetes cuando hagan falta, elegir kernel y ejecutar en orden |
| 2. Lenguaje y documentación | Los cuatro notebooks `01_*` de la tabla inferior | Profundizar en Python, Markdown y organización del código |
| 3. Trabajo con datos | Los notebooks `02_*` | Series, DataFrames, transformaciones y bases de datos |
| 4. Limpieza y visualización | Los notebooks `03_*` | Nulos, duplicados y gráficos |
| 5. Análisis exploratorio | Los notebooks `04_*` | EDA, codificación y escalado |
| Laboratorio | [Laboratorio.ipynb](Notebooks/Laboratorio.ipynb) | Aplicar el recorrido a Sakila |

La numeración de los notebooks originales se mantiene para conservar sus enlaces. El orden de aprendizaje completo lo marca esta tabla, incluyendo los nuevos bloques previos.

## Notebooks del curso original

Los **12 notebooks originales se conservan íntegros y en sus rutas**. Lee primero [sus condiciones de ejecución y notas docentes](Notebooks/GUIA.md): algunos contienen demostraciones de Colab, instalaciones de paquetes, interacción por teclado o acceso a MySQL.

| Notebook | Contenido |
|---|---|
| [01_1_Markdown](Notebooks/01_1_Markdown.ipynb) | Documentación con Markdown |
| [01_2_Notebook](Notebooks/01_2_Notebook.ipynb) | Celdas, kernel, ejecución y magias |
| [01_3_Elementos del Lenguaje](<Notebooks/01_3_Elementos del Lenguaje.ipynb>) | Tipos, variables, control de flujo, funciones y colecciones |
| [01_4_Modulos_Paquetes](Notebooks/01_4_Modulos_Paquetes.ipynb) | Importaciones, módulos propios y paquetes |
| [02_01_Repaso Basico Pandas](<Notebooks/02_01_Repaso Basico Pandas.ipynb>) | Series, DataFrames, selección y transformaciones |
| [02_02_Pandas y Bases de Datos](<Notebooks/02_02_Pandas y Bases de Datos.ipynb>) | Conexión MySQL y combinación de datos |
| [03_01_Nulos y repetidos](<Notebooks/03_01_Nulos y repetidos.ipynb>) | Nulos, imputación y duplicados |
| [03_02 Visualizacion](<Notebooks/03_02 Visualizacion.ipynb>) | Distribuciones y relaciones mediante gráficos |
| [04_01 EDA inicial](<Notebooks/04_01 EDA inicial.ipynb>) | Exploración de un conjunto de datos |
| [04_02_Codificacion de Variables](<Notebooks/04_02_Codificacion de Variables.ipynb>) | Codificación categórica |
| [04_03_Escalado de Caracteristicas](<Notebooks/04_03_Escalado de Caracteristicas.ipynb>) | Estandarización de variables |
| [Laboratorio](Notebooks/Laboratorio.ipynb) | Práctica guiada con Sakila |

## Dónde está cada material

| Carpeta o archivo | Uso |
|---|---|
| [00-Fundamentos](00-Fundamentos/README.md) | Conceptos previos; se pueden leer sin instalar nada |
| [Requisitos](Requisitos/README.md) | Instalación, entornos, Jupyter y solución de problemas |
| [01-Primeros-pasos](01-Primeros-pasos/README.md) | Lecciones, ejemplos ejecutables, ejercicios y soluciones |
| [Notebooks](Notebooks/GUIA.md) | Notebook inicial nuevo, 12 originales y paquete de demostración |
| [py](py/) | Scripts y Markdown originales de apoyo; no equivalen a todos los notebooks |
| [resources](resources/) | Recursos de apoyo originales |
| [requirements-inicio.txt](requirements-inicio.txt) | Dependencia mínima del primer notebook |
| [requirements-datos.txt](requirements-datos.txt) | Dependencias del bloque de análisis |
| [docs](docs/REESTRUCTURACION.md) | Análisis de la reorganización y documentación histórica |

## Cómo trabajar

1. [Descarga y abre el curso](01-Primeros-pasos/01-primer-programa.md). Git es opcional.
2. Escribe tus prácticas en `mis-ejercicios`; conserva los ejemplos para comparar.
3. Predice cada resultado, ejecuta, cambia un dato y explica lo ocurrido.
4. Completa [la comprobación del entorno](Requisitos/Comprobacion.md) antes de avanzar a notebooks.

También puedes utilizar [Google Colab](https://colab.research.google.com/) para el bloque de notebooks, con las condiciones explicadas en [Requisitos](Requisitos/README.md). La ruta desde cero utiliza VS Code local para aprender terminal y archivos.

## Para el docente

El material anterior partía de experiencia con datos. El nuevo tramo inicial permite incorporar alumnado sin esa base: unas **4–5 horas orientativas**, más instalación, según ritmo y ejercicios. Se puede ofrecer como preparación previa o como sesiones iniciales. No sustituye las horas del bloque de análisis.

[Análisis, conservación del contenido y notas de validación](docs/REESTRUCTURACION.md) · [Fuentes oficiales](docs/FUENTES.md) · [Guías anteriores](docs/historico/INDICE.md).

## Licencia

Materiales bajo licencia [MIT](LICENSE).

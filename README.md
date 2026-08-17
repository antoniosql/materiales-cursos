# Materiales de cursos

Repositorio central con los **materiales docentes** de los cursos y seminarios que
imparto: presentaciones, notebooks de demostración, enunciados de laboratorio y
conjuntos de datos.

Cada curso vive en su propio directorio y es autocontenido: dentro encontrarás su
`README.md` con la agenda, los requisitos y las instrucciones para seguirlo.

## Cursos

| Curso | Tema | Contenido |
|---|---|---|
| [Intro-Python](Intro-Python/) | Introducción a Python para el análisis de datos | Fundamentos del lenguaje, Pandas, limpieza de datos y análisis exploratorio (EDA), con notebooks y laboratorio guiado |
| [cursoml](cursoml/) | Desarrollo de soluciones con Machine Learning | Ciclo de vida de un proyecto ML: preparación de datos, algoritmos supervisados y no supervisados, ingeniería de características, despliegue e interpretabilidad |
| [bigdata](bigdata/) | Big Data con Hadoop, Hive, Spark y Databricks | Almacenamiento distribuido, MapReduce, Hive, Spark (RDD, DataFrames, ML, Streaming), Databricks y Delta Lake |
| [IntroBigData](IntroBigData/) | Introducción a Big Data — datos | Conjuntos de datos del curso introductorio (Instacart, sales records, Tiendas 24H, Titanic) y diagrama de arquitectura *medallion* |
| [seminario-fabric](seminario-fabric/) | Seminario: Microsoft Fabric | Arquitectura moderna de datos en Fabric: OneLake, ingesta y ETL, arquitectura medallón, lakehouse y warehouse, tiempo real, Data Activator y Fabric Databases. [Versión online](https://antoniosql.github.io/seminario-fabric/) |
| [rag-copilot-studio](rag-copilot-studio/) | Seminario: RAG con Copilot Studio | Arquitectura RAG empresarial, orígenes de conocimiento, arquitectura híbrida con Dataverse, evaluación, seguridad y gobierno. 5 laboratorios sobre el caso FraSoHome |
| [rag-local-lab](rag-local-lab/) | Taller: RAG local con Ollama, Qdrant y LangChain | Stack RAG 100 % local con Docker: AnythingLLM como demo visual y notebooks para construir el pipeline pieza a pieza |

## Cómo usar este repositorio

```bash
git clone https://github.com/antoniosql/materiales-cursos.git
```

1. Entra en el directorio del curso que te interese.
2. Lee su `README.md`: ahí están la agenda, los requisitos previos y el orden
   recomendado de los materiales.
3. Prepara el entorno **antes** de la primera sesión. Varios cursos incluyen una
   carpeta `Requisitos/` o un documento de requisitos del alumnado.

### Git LFS

Algunos ficheros de datos (`Tiendas24H.sqlite`, `BX-Books.csv`) se almacenan con
[Git LFS](https://git-lfs.com/). Instálalo antes de clonar si vas a trabajar con
el curso de Machine Learning:

```bash
git lfs install
```

### Ficheros de datos grandes

Los datasets de mayor tamaño están divididos en ZIP multivolumen (`.z01`, `.z02`,
…). Descarga todos los volúmenes junto al `.zip` final antes de descomprimir; las
instrucciones concretas están en el README de cada curso.

## Convenciones

- **Idioma:** todo el material está en español.
- **Notebooks:** la mayoría se pueden ejecutar tanto en local (VS Code / Jupyter)
  como en [Google Colab](https://colab.research.google.com/).
- **`demos/`** contiene lo que se ejecuta durante la clase; **`laboratorios/`** o
  **`labs/`**, lo que resuelve el alumnado; **`datos/`** o **`materiales/`**, los
  conjuntos de datos y documentos de apoyo.

## Otros materiales

- [iffe-iagen](https://github.com/antoniosql/iffe-iagen) — *IA Generativa: LLMs,
  OpenAI y agentes* (IFFE Business School). Se mantiene en un repositorio aparte.

## Licencia

Los materiales se publican bajo licencia MIT (ver el fichero `LICENSE` de cada
curso). Los conjuntos de datos conservan la licencia de sus fuentes originales y
se incluyen únicamente con fines docentes.

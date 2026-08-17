# Big Data con Hadoop, Hive, Spark y Databricks

Contenidos, demostraciones y laboratorios del curso de **Big Data**.

El curso recorre el ecosistema Hadoop de principio a fin: desde los fundamentos
de almacenamiento distribuido (HDFS) y el procesamiento por lotes (MapReduce),
hasta el trabajo con Hive como capa SQL y Apache Spark / Databricks como motor
de procesamiento moderno, incluyendo streaming estructurado y Delta Lake.

## Objetivos

- Entender qué problemas resuelve Big Data y cuándo una arquitectura distribuida
  aporta valor frente a un enfoque tradicional.
- Conocer los fundamentos de almacenamiento distribuido y los formatos de fichero
  habituales, así como el papel de las bases de datos NoSQL.
- Configurar, monitorizar y administrar los servicios de un clúster Hadoop.
- Consultar y optimizar datos con Hive.
- Programar con Apache Spark (RDD, DataFrames, ML y Streaming).
- Trabajar en Databricks con DBFS, streaming estructurado y Delta.

## Agenda

| # | Módulo | Material |
|---|---|---|
| 0 | Introducción al curso | [Materiales/0_Introduccion.pdf](Materiales/0_Introduccion.pdf) |
| 1.1 | Introducción a Big Data y Hadoop | [Materiales/1_1 Introduccion a Big Data y Hadoop.pdf](<Materiales/1_1 Introduccion a Big Data y Hadoop.pdf>) |
| 1.2 | NoSQL | [Materiales/1_2 NoSQL.pdf](<Materiales/1_2 NoSQL.pdf>) |
| 1.3 | Patrones y arquitecturas de referencia | [Materiales/1_3 Patrones y Arquitecturas de Referencia.pdf](<Materiales/1_3 Patrones y Arquitecturas de Referencia.pdf>) |
| 2 | Fundamentos de almacenamiento (HDFS) | [Materiales/2_Fundamentos de Almacenamiento.pdf](<Materiales/2_Fundamentos de Almacenamiento.pdf>) |
| 3 | Configuración de servicios Hadoop | [Materiales/3_Configuracion Servicios Hadoop.pdf](<Materiales/3_Configuracion Servicios Hadoop.pdf>) |
| 4 | Ambari: monitorización y administración | [Materiales/4_Uso de Ambari para Monitorización y Administración.pdf](<Materiales/4_Uso de Ambari para Monitorización y Administración.pdf>) |
| 5 | Fundamentos de Hive | [Materiales/5_Fundamentos de HIVE.pdf](<Materiales/5_Fundamentos de HIVE.pdf>) |
| 6 | Arquitectura de Apache Spark | [Materiales/6_Arquitectura de Apache Spark.pdf](<Materiales/6_Arquitectura de Apache Spark.pdf>) |
| 7 | Databricks | [Materiales/7_Databricks.pdf](<Materiales/7_Databricks.pdf>) |

## Estructura del repositorio

```text
bigdata/
├── Materiales/       # Presentaciones en PDF de cada módulo
├── demos/            # Ejemplos que ejecuta el instructor durante las sesiones
├── Laboratorios/     # Enunciados y ficheros de los ejercicios del alumno
│   └── Notebooks/    # Notebooks Jupyter de los laboratorios de Spark
├── datos/            # Conjuntos de datos usados en demos y laboratorios
├── EsquemaAirlines.py  # Definición del esquema del dataset de vuelos para Spark
└── datos.txt         # Datos de acceso al entorno de la edición del curso
```

### Demostraciones

| Demo | Contenido |
|---|---|
| [Demo 02 HDFS.txt](<demos/Demo 02 HDFS.txt>) | Comandos `hadoop fs`: carga, copia, borrado y configuración de HDFS |
| [Demo 03 Mapreduce.txt](<demos/Demo 03 Mapreduce.txt>) | Ejecución de trabajos MapReduce sobre el clúster |
| [Demo 05 A HIVE.hql](<demos/Demo 05 A HIVE.hql>) | Creación de tablas y consultas básicas en Hive |
| [Demo 05 B Optimizacion Hive.hql](<demos/Demo 05 B Optimizacion Hive.hql>) | Particionado, bucketing y formatos columnares |
| [Demo 06 A RDD.ipynb](<demos/Demo 06 A RDD.ipynb>) | Primeros pasos con RDDs en Spark |
| [Demo 06 B Contando palabras.ipynb](<demos/Demo 06 B Contando palabras.ipynb>) | El clásico *word count* con Spark |
| [Demo 07 A Databricks DBFS.ipynb](<demos/Demo 07 A Databricks DBFS.ipynb>) | Trabajo con el sistema de ficheros de Databricks |
| [Demo 07 B Databricks Streaming Estructurado.ipynb](<demos/Demo 07 B Databricks Streaming Estructurado.ipynb>) | Ingesta en streaming estructurado |
| [Demo 07 C Databricks Delta.ipynb](<demos/Demo 07 C Databricks Delta.ipynb>) | Tablas Delta: ACID, time travel y optimización |

### Laboratorios

| Laboratorio | Contenido |
|---|---|
| [Laboratorios Parte I.pdf](<Laboratorios/Laboratorios Parte I.pdf>) | Enunciados de la primera parte del curso (Hadoop, HDFS, Ambari) |
| [Laboratorios Parte II.pdf](<Laboratorios/Laboratorios Parte II.pdf>) | Enunciados de la segunda parte (Hive, Spark, Databricks) |
| [Laboratorio 05 A HIVE.txt](<Laboratorios/Laboratorio 05 A HIVE.txt>) · [Laboratorio 05 B HIVE.txt](<Laboratorios/Laboratorio 05 B HIVE.txt>) | Sentencias de apoyo para los laboratorios de Hive |
| [Notebooks/](Laboratorios/Notebooks/) | Laboratorios 06 A–D: primeros pasos con Spark, DataFrames, SparkML y Spark Streaming |

### Datos

| Fichero | Uso |
|---|---|
| `datos/drivers.csv`, `datos/timesheet.csv`, `datos/truck_event_text_partition.csv` | Caso de la flota de camiones: laboratorios de Hive y Spark |
| `datos/users.tsv`, `datos/products.tsv` | Ejemplos de carga y `JOIN` en Hive |
| `datos/Ventas_1000.csv` | Dataset pequeño para las primeras pruebas con DataFrames |

## Requisitos

- Acceso al entorno de clúster de la edición del curso (los datos de conexión los
  proporciona el instructor; ver `datos.txt`).
- Cuenta de [Databricks Community Edition](https://community.cloud.databricks.com/)
  o workspace de Databricks para los módulos 6 y 7.
- Conocimientos básicos de SQL y de línea de comandos Linux. Se recomienda algo de
  experiencia con Python para los notebooks de Spark.

## Cómo seguir el curso

1. Lee la presentación del módulo en [Materiales/](Materiales/).
2. Sigue las demostraciones de [demos/](demos/) junto con el instructor.
3. Resuelve por tu cuenta los ejercicios de [Laboratorios/](Laboratorios/),
   apoyándote en los ficheros de [datos/](datos/).

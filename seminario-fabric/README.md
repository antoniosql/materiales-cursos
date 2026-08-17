# 🚀 Seminario Microsoft Fabric  
### Arquitectura Moderna de Datos + IA Generativa + Patrones para 2025  
Por **Antonio Soto (@antoniosql)** | Dataging

---


Bienvenido al repositorio oficial del **Seminario de Microsoft Fabric**, un recurso abierto diseñado para profesionales que quieren entender **cómo escalar datos e IA generativa** en la plataforma unificada de Microsoft.

Este seminario reúne **experiencia real en proyectos**, mejores prácticas, patrones arquitectónicos y una visión clara de cómo Fabric está transformando la ingeniería de datos, el BI y la adopción de IA generativa.

🟦 **Versión online del seminario:**  
👉 https://antoniosql.github.io/seminario-fabric/

---

# 🎯 Objetivos del seminario

- Explicar **qué es Microsoft Fabric** y por qué representa un cambio de paradigma.  
- Mostrar cómo unificar **ingeniería de datos, análisis, BI, tiempo real y gobierno**.  
- Identificar errores comunes y cómo evitarlos.  
- Proponer **patrones reales** utilizados actualmente en organizaciones.  

---

# 📚 Contenido del seminario

### **🟠 Módulo 1: Introducción a Microsoft Fabric**

✅ **¿Qué es Microsoft Fabric?** Diferencias con Power BI e integración con otras herramientas. [Ver apuntes](<docs/01 Introduccion a Microsoft Fabric/01-1 Que es Microsoft Fabric.md>)

✅ **El Concepto de OneLake:** Arquitectura y ventajas de un Data Lake unificado. [Ver apuntes](<docs/01 Introduccion a Microsoft Fabric/01-2 El Concepto de Onelake.md>)

✅ **Escenarios End to End:** Implementación de cargas ETL, almacenamiento y análisis. [Ver apuntes](<docs/01 Introduccion a Microsoft Fabric/01-3 Escenarios End-to-End en Microsoft Fabric.md>)

### **🟠 Módulo 2: Carga de Datos en Microsoft Fabric**

✅ **Ingesta de datos:** Panorama de opciones de carga en Fabric. [Ver apuntes](<docs/02 Carga de Datos/02-0 Ingesta de Datos en Microsoft Fabric.md>)

✅ **ETL con Flujos de Datos de Gen2:** Creación, transformación y optimización de datos. [Ver apuntes](<docs/02 Carga de Datos/02-1 ELT con flujos de datos de Gen2.md>)

✅ **Orquestación con Pipelines de Data Factory:** Automatización de cargas y dependencias. [Ver apuntes](<docs/02 Carga de Datos/02-2 Orquestando Cargas con Pipelines de Data Factory.md>)

✅ **Modelado dimensional:** Diseño del modelo analítico. [Ver apuntes](<docs/02 Carga de Datos/02-3 Modelado Dimensional.md>)

✅ **Desarrollo con Apache Spark:** Uso de Notebooks y PySpark para Ingeniería de Datos. [Ver apuntes](<docs/02 Carga de Datos/02-4 Desarrollo con Apache Spark.md>)

✅ **Guía de decisión:** Qué herramienta de carga elegir en cada escenario. [Ver apuntes](<docs/02 Carga de Datos/02-5 Guia de Decisión.md>)

### **🟠 Módulo 3: Ingeniería de Datos con Microsoft Fabric**

✅ **Arquitectura Medallón:** Implementación de un modelo Bronce-Plata-Oro en Fabric. [Ver apuntes](<docs/03 Ingenieria de Datos/03-1 Introducción a la Arquitectura Medallón.md>)

✅ **Lakehouse en Fabric:** Creación y gestión de un Lakehouse, almacenamiento y consultas SQL. [Ver apuntes](<docs/03 Ingenieria de Datos/03-2 Creación y Gestión de un lakehouse.md>)

✅ **Data Warehouses en Fabric:** Optimización de modelos de datos para análisis eficientes. [Ver apuntes](<docs/03 Ingenieria de Datos/03-3 Trabajo con Datawarehouse.md>)

### **🟠 Módulo 4: Análisis Avanzado y Automatización en Fabric**

✅ **Plataforma para Ciencia de Datos:** Fabric como plataforma para el desarrollo de proyectos de Ciencia de Datos. [Ver apuntes](<docs/04 Analisis Avanzado y Automatizacion/04-1 Fabric como plataforma de Data Science.md>)

✅ **Análisis en Tiempo Real:** Analítica de datos en streaming y KQL. [Ver apuntes](<docs/04 Analisis Avanzado y Automatizacion/04-2 Análisis de Datos en Tiempo Real con Microsoft Fabric.md>)

✅ **Data Activator:** Automatización de procesos basada en eventos e integración con Power Automate. [Ver apuntes](<docs/04 Analisis Avanzado y Automatizacion/04-3 Introducción a Data Activator.md>)

### **🟠 Módulo 5: Fabric Databases**

✅ **Introducción a Fabric Databases:** Datos relacionales en Microsoft Fabric. [Ver apuntes](<docs/05 Fabric Databases/05-1 Fabric Databases.md>)

✅ **Escenarios:** Escenarios de utilización de Fabric Databases. [Ver apuntes](<docs/05 Fabric Databases/05-2 Escenarios de Fabric Databases.md>)

---

# 🧪 Demos y laboratorios

**Demos** — guiones paso a paso que se ejecutan durante la sesión:

| Demo | Contenido |
|---|---|
| [Creación de capacidad](<Demos/01 -1 Creación Capacidad.md>) | Alta de una capacidad Fabric y creación del workspace |
| [OneLake](<Demos/01-2 Onelake.md>) | Recorrido por OneLake, el explorador y los accesos directos |
| [ETL básico](<Demos/01-3 ETL básico.md>) | Primera carga end-to-end de datos en Fabric |

**Laboratorios** — ficheros de datos y guiones para practicar por tu cuenta:

| Recurso | Uso |
|---|---|
| [Orígenes de Datos](<Laboratorios/Orígenes de Datos.md>) | Punto de partida: qué datos se cargan y desde dónde |
| [Notebook Fabric](<Laboratorios/Notebook Fabric.md>) | Código PySpark para el laboratorio de ingeniería de datos |
| `bronce.csv`, `plata.csv`, `oro.csv` | Capas de la arquitectura medallón |
| `ventas.csv`, `clientes.csv`, `Ventas_Dataset.csv`, `lakehouse.csv` | Datos para lakehouse y modelado |
| [`data_warehouse.sql`](Laboratorios/data_warehouse.sql) · `data_warehouse.csv` | Creación y carga del Data Warehouse |
| `event_stream.json`, `data_activator_rules.json` | Análisis en tiempo real y reglas de Data Activator |
| [Código para generar los ejemplos](<Laboratorios/Código para generar los ejemplos.md>) | Script con el que se generaron los datasets de ejemplo |

---

# 🗂️ Estructura del repositorio

```text
seminario-fabric/
├── docs/           # Apuntes por módulo (sitio MkDocs)
├── Demos/          # Guiones de las demostraciones en directo
├── Laboratorios/   # Datos y guiones de los ejercicios
├── Materiales/     # Introducción, recursos adicionales e imágenes
└── mkdocs.yml      # Configuración del sitio publicado
```

Complementos: [Introducción](<Materiales/00 Introducción.md>) y
[Recursos](<Materiales/99 Recursos.md>) con enlaces para seguir profundizando.

---

# ✅ Requisitos

- Cuenta de **Microsoft Fabric**: sirve la
  [prueba gratuita](https://learn.microsoft.com/fabric/fundamentals/fabric-trial)
  o una capacidad F/P asignada a tu workspace.
- Permisos para crear workspaces, lakehouses y warehouses.
- Nociones de SQL. Para el módulo de Spark ayuda algo de experiencia con Python.

---

# 📖 Cómo usar estos materiales

La forma más cómoda de leer los apuntes es la
[versión online](https://antoniosql.github.io/seminario-fabric/).

Para levantarlos en local:

```bash
pip install mkdocs-material pymdown-extensions
mkdocs serve
```

Y abre `http://localhost:8000`. El workflow de
[GitHub Actions](.github/workflows/blank.yml) republica el sitio con cada push a
`main`.

Recorrido recomendado: apuntes del módulo en `docs/` → demo correspondiente en
`Demos/` → ejercicio en `Laboratorios/`.

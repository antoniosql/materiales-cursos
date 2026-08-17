# Seminario: RAG con Copilot Studio

Apuntes, laboratorios y materiales del seminario **RAG y Copilot Studio**.

El seminario aborda RAG (*Retrieval Augmented Generation*) desde la práctica
empresarial: cómo se indexa el conocimiento, por qué falla la recuperación, cuándo
RAG no basta y hay que combinarlo con herramientas y datos estructurados, y cómo
evaluar, asegurar y gobernar el resultado.

Todo el contenido se construye alrededor de un caso continuo: **FraSoHome**, una
cadena ficticia de muebles y decoración con operación omnicanal, con datos
fragmentados entre CRM, POS, e-commerce y ERP.

## Qué vas a aprender

- Diseñar una **arquitectura RAG** empresarial: ingesta → indexación → recuperación → respuesta.
- Entender por qué funciona (y por qué falla) la **recuperación semántica**:
  chunking, embeddings, búsqueda híbrida y metadatos.
- Implementar y operar un agente en **Copilot Studio** con conocimiento,
  citaciones y evaluación básica.
- Identificar cuándo RAG no es suficiente y conviene un enfoque **híbrido** con
  herramientas (*tools*) y datos estructurados en Dataverse.
- Medir y mejorar: **evaluación**, **seguridad y gobierno**, **citaciones y trazabilidad**.

## Estructura del seminario

| Sesión | Contenido | Bloques |
|---|---|---|
| 1 — Fundamentos operativos de RAG | Arquitectura, indexación y embeddings | [1.1 Arquitectura RAG](<docs/01 Fundamentos RAG/sesion1_1_arquitectura_rag_entorno_empresarial.md>) · [1.2 Indexación documental](<docs/01 Fundamentos RAG/sesion1_2_proceso_indexacion_documental.md>) · [1.3 Embeddings y recuperación](<docs/01 Fundamentos RAG/sesion1_3_embeddings_y_recuperacion_semantica.md>) |
| 2 — Orígenes de conocimiento y calidad | Qué fuentes soporta Copilot Studio y cómo mejorar la recuperación | [2.1 Orígenes soportados](<docs/02 Origenes Conocimiento/sesion2_1_origenes_soportados_y_tratamiento.md>) · [2.2 Diferencias operativas](<docs/02 Origenes Conocimiento/sesion2_2_diferencias_operativas_clave.md>) · [2.3 Factores de calidad](<docs/02 Origenes Conocimiento/sesion2_3_factores_calidad_recuperacion.md>) |
| 3 — Arquitectura híbrida | RAG + herramientas + datos estructurados | [3.1 Cuándo RAG no basta](<docs/03 Herramientas y Datos Estructurados/sesion3_1_cuando_rag_no_es_suficiente.md>) · [3.2 Herramientas en Copilot Studio](<docs/03 Herramientas y Datos Estructurados/sesion3_2_uso_herramientas_copilot_studio.md>) · [3.3 Datos estructurados](<docs/03 Herramientas y Datos Estructurados/sesion3_3_datos_estructurados_y_agente_datos.md>) |
| 4 — Evaluación, seguridad y gobierno | Medición repetible, controles y trazabilidad | [4.1 Evaluación de calidad](<docs/04 Evaluación, Seguridad y Gobierno/sesion4_1_evaluacion_calidad.md>) · [4.2 Evaluación en Copilot Studio](<docs/04 Evaluación, Seguridad y Gobierno/sesion4_2_evaluacion_en_copilot_studio.md>) · [4.3 Seguridad y gobierno](<docs/04 Evaluación, Seguridad y Gobierno/sesion4_3_seguridad_y_gobierno.md>) · [4.4 Citaciones y trazabilidad](<docs/04 Evaluación, Seguridad y Gobierno/sesion4_4_citaciones_y_trazabilidad.md>) |

## Laboratorios

Los laboratorios construyen, paso a paso, un agente híbrido para FraSoHome.
Empiezan en el LAB 2 ([índice completo](<docs/99 Laboratorios/00 indice.md>)):

| Lab | Contenido |
|---|---|
| [LAB 2](<docs/99 Laboratorios/LAB2_Base_de_conocimiento_RAG_en_Copilot_Studio.md>) | Base de conocimiento RAG: carga de documentos, citaciones y conflicto de versiones |
| [LAB 3](<docs/99 Laboratorios/LAB3_Prompting_Citaciones_y_Control_de_Fallback.md>) | Prompting, citaciones, abstención y pruebas de *prompt injection* |
| [LAB 4](<docs/99 Laboratorios/LAB4_Dataverse_y_Datos_Estructurados.md>) | Dataverse: crear tablas e importar los CSV de ventas, devoluciones y stock |
| [LAB 5](<docs/99 Laboratorios/LAB5_Arquitectura_Hibrida_Tools_y_RAG.md>) | Arquitectura híbrida: Tools de Dataverse + RAG documental |
| [LAB 6](<docs/99 Laboratorios/LAB6_Evaluacion_Seguridad_y_Gobierno.md>) | Evaluación con test sets, seguridad y gobierno |

## Materiales del caso FraSoHome

```text
materiales/
├── Documentos_Knowledge_Clasificados/   # Base documental del agente (.docx)
│   ├── 01_Politicas/                    # Incluye una versión vigente y otra obsoleta a propósito
│   ├── 02_KPI_y_Datos/                  # Diccionario de KPI y reglas de cálculo
│   ├── 03_Operaciones/                  # Manuales de tienda, conciliación y FAQ
│   ├── 04_Catalogo/                     # Taxonomía y reglas de SKU
│   ├── 05_CRM/                          # Guía de fidelización
│   ├── 06_Gobierno_y_Seguridad/         # Política de datos y permisos del asistente
│   └── 07_Test_Security/                # Documento de prueba de prompt injection (NO producción)
├── Datos_Estructurados/                 # CSV para Dataverse: ventas, stock, clientes, tiendas…
└── TestSets/                            # Conjuntos de preguntas para la evaluación (LAB 6)
```

> El documento de `07_Test_Security/` contiene una inyección de prompt
> **intencionada**. Se usa únicamente en el LAB 3 para comprobar que el agente
> resiste el ataque; no lo cargues en un entorno productivo.

## Requisitos

- Licencia o prueba de **Microsoft Copilot Studio** y acceso a un entorno de
  **Power Platform / Dataverse** con permisos para crear tablas.
- Los laboratorios se realizan íntegramente en el navegador; no hace falta
  instalar nada para seguirlos.

## Leer los apuntes en local

Los apuntes están escritos para [MkDocs](https://www.mkdocs.org/) con el tema
Material. Para levantarlos en tu equipo:

```bash
pip install mkdocs-material pymdown-extensions
mkdocs serve
```

Y abre `http://localhost:8000`. El workflow de
[GitHub Actions](.github/workflows/ci.yml) publica el sitio automáticamente en
GitHub Pages con cada push a `main`.

Si prefieres no instalar nada, puedes leer los ficheros Markdown directamente
desde [docs/](docs/), empezando por [docs/index.md](docs/index.md).

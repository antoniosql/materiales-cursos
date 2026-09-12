# Reorganización de Intro-Python

## Diagnóstico

Revisión del curso en el commit `e5252cf787b7fa57b85ffa77ea97b50aa1ef8e0b`: 12 notebooks, scripts de apoyo y guías de requisitos. El README declaraba experiencia previa en Excel, SQL o backend. El contenido empezaba por Markdown, notebooks y elementos del lenguaje, sin presentar antes las herramientas de trabajo.

Las guías de instalación eran breves, mezclaban comandos de terminal e IPython, no separaban Windows y macOS y contenían `pip install sklearn`, `pip install sqlite3` y una fijación antigua de SciPy. No había listas de dependencias del curso ni una ruta de primeras prácticas sin infraestructura externa.

## Decisiones de organización

| Situación anterior | Cambio realizado | Motivo |
|---|---|---|
| Se presupone experiencia técnica | `00-Fundamentos` | Introducir vocabulario y modelo de ejecución antes de instalar |
| Salto directo a notebooks | `01-Primeros-pasos` | Practicar primero archivos, terminal, entrada y cálculos pequeños |
| Instalación genérica | Guías Windows/macOS y extensión común | Distinguir instaladores, arquitecturas, comandos y selección de intérprete |
| Paquetes desde el primer momento | Listas de inicio y datos, con `.venv` | Introducir dependencias cuando se necesitan |
| Dependencias externas poco visibles | Guía de notebooks y preparación Sakila | Explicar qué requiere cada demostración |
| Un único nivel de entrada | Tres rutas en el README | Permitir empezar desde cero o incorporarse al nivel adecuado |

Los nombres y rutas de los notebooks y scripts originales se mantienen para conservar enlaces y la importación del paquete local. La reorganización añade una secuencia de aprendizaje y carpetas introductorias; no renombra todos los archivos históricos.

## Conservación del contenido

- Los 12 notebooks, scripts, paquete local, recursos, licencia y configuración anteriores se conservan sin modificar.
- Las siete guías reemplazadas —README del curso y seis documentos de Requisitos— están copiadas íntegramente en `docs/historico`, con un [índice](historico/INDICE.md) que las identifica como anteriores.
- El `.gitignore` conserva su contenido y añade exclusiones de entornos, cachés, credenciales y ejercicios locales.
- [contenido-original.json](contenido-original.json) registra las rutas y los identificadores Git de todos los archivos originales de este curso. Permite contrastar conservación a nivel de bytes.
- No se modifica contenido de otros cursos del repositorio.

## Secuencia docente propuesta

Un tramo previo de 4–5 horas orientativas, más instalación: conceptos y terminal; primer programa y variables; decisiones y funciones; errores y ejercicios; transición a notebooks. Ajustar según las comprobaciones de avance, no por haber leído los archivos. El bloque original de análisis conserva su propia duración.

Los ejercicios nuevos utilizan datos ficticios, biblioteca estándar y resultados pequeños verificables a mano. Las soluciones incluyen casos de lista vacía, límite de plazas y entradas no numéricas. El primer notebook evita red, MySQL y Pandas durante su ejecución.

## Límites del trabajo

La ampliación no moderniza internamente los 12 notebooks originales. Sus particularidades detectadas se documentan en [Notebooks/GUIA.md](../Notebooks/GUIA.md). Las listas de paquetes no fijan versiones y no prometen compatibilidad completa del bloque histórico.

La instalación de Windows y macOS se contrasta con documentación oficial; no equivale a ejecutar instaladores gráficos en ambos sistemas. La validación local y sus resultados se recogen en [VALIDACION.md](VALIDACION.md).

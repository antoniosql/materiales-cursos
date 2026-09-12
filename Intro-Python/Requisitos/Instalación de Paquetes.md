# Instalar paquetes del curso

La instalación está dividida por etapa en [Entorno virtual y paquetes](Entorno-y-paquetes.md).

| Etapa | Lista |
|---|---|
| Primeros scripts | Ningún paquete externo |
| Primer notebook | [requirements-inicio.txt](../requirements-inicio.txt) |
| Análisis con datos | [requirements-datos.txt](../requirements-datos.txt) |

Las listas no fijan versiones. Antes de usar el bloque histórico, revisa su [mapa de dependencias](../Notebooks/GUIA.md) y valida el entorno de clase. MySQL y Sakila se preparan aparte: instalar un conector no instala el servidor ni los datos.

Las correcciones frente a `pip install sklearn`, `pip install sqlite3` y la antigua fijación de SciPy se explican en la guía común. [Se conserva el texto anterior](../docs/historico/INDICE.md).

[Volver a preparación](README.md)

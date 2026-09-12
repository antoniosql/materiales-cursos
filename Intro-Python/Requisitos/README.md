# Preparar el entorno desde cero

Si no distingues lenguaje, intérprete y editor, empieza por [00-Fundamentos](../00-Fundamentos/README.md). No necesitas saber Git, SQL o Pandas.

## Elige tu sistema operativo

| Sistema | Guía completa |
|---|---|
| Windows | [Instalar Python y VS Code en Windows](Windows.md) |
| macOS: Intel o Apple silicon | [Instalar Python y VS Code en macOS](macOS.md) |

Después sigue esta secuencia común:

1. [Instalar la extensión Python de Microsoft](<Instalar el complemento de Python.md>).
2. [Descargar el curso y ejecutar el primer programa](../01-Primeros-pasos/01-primer-programa.md).
3. Completar las lecciones de [primeros pasos](../01-Primeros-pasos/README.md).
4. [Crear el entorno virtual e instalar paquetes por etapa](Entorno-y-paquetes.md).
5. [Preparar Jupyter y seleccionar el kernel](Jupyter.md).
6. Revisar la [lista de comprobación](Comprobacion.md).

## Qué necesitas en cada momento

| Etapa | Software y recursos |
|---|---|
| Conceptos previos | Navegador |
| Primeros programas | Python 3, VS Code y extensión Python |
| Primer notebook | Extensión Jupyter e `ipykernel` en `.venv` |
| Pandas, limpieza y EDA | Paquetes de `requirements-datos.txt` |
| Ejemplos Sakila | Acceso a MySQL con Sakila y configuración del docente |

Comprueba los requisitos de sistema de las descargas y dispone de conexión a Internet durante la instalación. En equipos gestionados por tu organización, utiliza su mecanismo autorizado de instalación.

MySQL se utiliza en varios notebooks de análisis, no solo en el de bases de datos. Consulta el [mapa de dependencias](../Notebooks/GUIA.md).

## Ayuda y materiales anteriores

- [Solución de problemas](Solucion-de-problemas.md).
- [Qué es pip](<Instalar PIP.md>).
- [Guías originales conservadas](../docs/historico/INDICE.md).
- [Vídeo del material original](https://www.youtube.com/watch?v=Oa_Zo8jtsTE): referencia complementaria; sus pantallas pueden diferir de las actuales.

Se conserva la alternativa [Google Colab](https://colab.research.google.com/), para notebooks en el navegador. No sustituye las prácticas locales de terminal, archivos y VS Code. Una conexión MySQL desde Colab requiere que el servidor sea accesible desde ese entorno.

[Volver al curso](../README.md)

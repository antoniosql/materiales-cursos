# Validación de la ampliación

Fecha: 12 de septiembre de 2026. Entorno de ejecución disponible: Linux, CPython 3.12.14.

## Conservación

Se ha comparado el identificador de contenido Git de los 35 archivos del inventario original: 27 archivos idénticos en su ruta, 7 guías originales conservadas íntegramente en el archivo histórico y `.gitignore` ampliado manteniendo su contenido anterior. Los 12 notebooks originales están dentro de los archivos idénticos. Los cambios afectan únicamente a `Intro-Python`.

## Ejecución del material nuevo

- Ejecutados los 9 scripts nuevos: cuatro ejemplos, el diagnóstico del entorno y cuatro soluciones.
- Comprobados casos de capacidad exacta, exceso de asistentes, cantidad negativa y texto no numérico.
- Verificados los totales del miniproyecto: 6 unidades y 20 euros; al cambiar una cantidad, 7 unidades y 24 euros; con lista vacía, ambos totales cero.
- Ejecutadas las 10 celdas de código de `00_0_Primer_notebook.ipynb` en orden y en un espacio de nombres nuevo de IPython. Formato validado con `nbformat`; se guardan salidas de esta ejecución.

## Enlaces y presentación

Verificados 204 enlaces relativos en los 31 documentos Markdown nuevos o actualizados y en el notebook nuevo; sin destinos ausentes. El texto histórico se excluye de esta comprobación porque se conserva literalmente. JSON de configuración e inventario validado.

Se ha generado una vista HTML del notebook y comprobado que contiene las salidas, pero no se ha podido inspeccionar visualmente en un navegador: el entorno no tiene Chromium disponible y la descarga falló. Al revisar el PR, abrir el notebook en GitHub o VS Code para comprobar su presentación.

## Límites explícitos

El arranque de un kernel externo de Jupyter mediante `nbclient` está impedido en este entorno por restricciones de sockets, tanto TCP como IPC. La alternativa utilizada ejecuta las celdas con IPython en el mismo proceso. Por tanto, la lógica y el orden de celdas están comprobados, pero **no se ha probado aquí la integración completa VS Code–Jupyter ni el ciclo de conexión de un kernel externo**.

Las instalaciones gráficas de Windows y macOS no se han ejecutado en equipos nativos. Las instrucciones se han contrastado con documentación de Python y Microsoft, enlazada en [FUENTES.md](FUENTES.md). La rama 3.14 es la referencia de instalación; las comprobaciones de código de esta revisión usan 3.12.14.

Los notebooks originales se han inspeccionado, pero no ejecutado de principio a fin: varios necesitan MySQL/Sakila, red o interacción, y el laboratorio tiene celdas para completar. Las listas de dependencias de datos no son un lockfile ni un entorno de análisis íntegramente validado.

## Comprobación final en el equipo del alumno o docente

Seguir [Requisitos/Comprobacion.md](../Requisitos/Comprobacion.md): elegir `.venv`, ejecutar los scripts, seleccionar el kernel, reiniciar y ejecutar el notebook nuevo completo. Para los originales, seguir [Notebooks/GUIA.md](../Notebooks/GUIA.md) y preparar Sakila cuando corresponda.

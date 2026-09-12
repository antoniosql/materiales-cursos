# Preparar y utilizar notebooks en VS Code

Un notebook (`.ipynb`) combina celdas de texto y de código. El kernel mantiene las variables en memoria mientras la sesión está abierta. Para este bloque, completa antes [entornos y paquetes](Entorno-y-paquetes.md) e instala `requirements-inicio.txt`.

## 1. Instalar la extensión Jupyter

1. Abre Extensiones: **Ctrl+Shift+X** en Windows o **Cmd+Shift+X** en macOS.
2. Busca `@id:ms-toolsai.jupyter`.
3. Verifica **Jupyter**, de **Microsoft**, y pulsa **Install**. Su [ficha oficial](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) identifica el complemento.

La extensión está en VS Code; `ipykernel` se instala en `.venv`. Son dos componentes diferentes. Para esta ruta no necesitas instalar JupyterLab ni arrancar un servidor manualmente.

## 2. Abrir y seleccionar el kernel

1. Con `Intro-Python` abierto como carpeta, abre [00_0_Primer_notebook.ipynb](../Notebooks/00_0_Primer_notebook.ipynb).
2. Pulsa **Select Kernel** en la esquina superior derecha.
3. Elige **Python Environments** y el intérprete de `.venv`. Si aparece otra pantalla intermedia, selecciona la opción de buscar otro kernel.
4. Ejecuta la primera celda con su botón ▶ o **Shift+Enter**. Mostrará la versión y la ruta del intérprete. Comprueba que la ruta contiene `.venv`.

Si no aparece el entorno, selecciona su ruta desde **Python: Select Interpreter**, recarga la ventana y vuelve al selector de kernel. Si falta `ipykernel`, instala `requirements-inicio.txt` con el ejecutable de `.venv`.

## 3. Ejecutar en orden

- Una celda **Markdown** presenta texto; una celda **Code** ejecuta Python.
- **Run All** ejecuta las celdas en el orden del documento.
- **Restart** reinicia el kernel y borra sus variables; no elimina el código guardado.
- Una salida que ves al abrir un notebook puede ser una salida guardada de una ejecución anterior. No prueba que tu entorno esté preparado.
- Guardar el notebook conserva código y salidas, pero no guarda un proceso vivo con todas sus variables.

Practica primero con el notebook nuevo, que no requiere red, MySQL ni Pandas durante la ejecución. Después sigue el [mapa del bloque original](../Notebooks/GUIA.md).

## 4. Particularidades del material original

En `01_2_Notebook.ipynb`, la celda `from google.colab import drive` es exclusiva de Colab: omítela en VS Code. Los comandos `!` y `%` pertenecen a IPython. Una magia de celda como `%%html` debe ir en la primera línea; en la demostración histórica hay un comentario antes y deberás moverlo o retirarlo en tu copia para ejecutar esa celda.

En `01_4_Modulos_Paquetes.ipynb` hay ejemplos que instalan paquetes y exportan un `requirements.txt`. Léalos antes de ejecutarlos; la preparación del curso se realiza con nuestras listas desde la terminal. Los originales permanecen íntegros y se documentan sus condiciones de uso.

Fuentes: [notebooks en VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks), [gestión de kernels](https://code.visualstudio.com/docs/datascience/jupyter-kernel-management) y [magias de IPython](https://ipython.readthedocs.io/en/stable/interactive/magics.html).

[Siguiente: comprobación](Comprobacion.md) · [Volver al curso](../README.md)

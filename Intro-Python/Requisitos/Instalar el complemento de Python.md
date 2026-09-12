# Instalar la extensión Python de Microsoft en VS Code

Antes deben estar instalados [Python](<Instalar Python.md>) y [VS Code](<Instalar Visual Studio Code.md>). La extensión añade soporte al editor; el intérprete ejecuta el código.

## 1. Instalar el complemento correcto

1. Abre VS Code y pulsa **Extensions / Extensiones** en la barra lateral: **Ctrl+Shift+X** en Windows o **Cmd+Shift+X** en macOS.
2. Busca `@id:ms-python.python`.
3. Comprueba el nombre **Python** y el editor **Microsoft**. Pulsa **Install / Instalar**. Recarga VS Code si se solicita.

Referencia: [Python, Microsoft, ms-python.python](https://marketplace.visualstudio.com/items?itemName=ms-python.python). Puede instalar o recomendar componentes como Pylance y Python Debugger. No necesitas todos los resultados de una búsqueda de «Python».

## 2. Seleccionar el intérprete

Abre una carpeta con **File > Open Folder…**. Para el curso será `Intro-Python`, una vez [descargados los materiales](../01-Primeros-pasos/01-primer-programa.md).

1. Abre la paleta: **Ctrl+Shift+P** en Windows o **Cmd+Shift+P** en macOS.
2. Ejecuta **Python: Select Interpreter**.
3. Selecciona la instalación que has comprobado. Más adelante elegirás `.venv`.
4. Si no aparece, utiliza **Enter interpreter path…**. Averigua la ruta con uno de estos comandos en la terminal:

Windows:

```powershell
py -3.14 -c "import sys; print(sys.executable)"
```

macOS:

```bash
python3.14 -c "import sys; print(sys.executable)"
```

`sys` es un módulo incluido con Python. Aquí solo lo usamos para mostrar la ruta.

## 3. Probar con un archivo

Sigue [crear y ejecutar `hola.py`](../01-Primeros-pasos/01-primer-programa.md). El comando **Run Python File in Terminal** utiliza el intérprete seleccionado. La salida aparece en Terminal. Guardar y ejecutar son acciones distintas.

El curso incluye [extensiones recomendadas](../.vscode/extensions.json); puedes instalar Python ahora y Jupyter después. Estas prácticas locales no requieren una suscripción a Copilot.

## 4. Cuando llegues a notebooks

Sigue [la guía de Jupyter](Jupyter.md): extensión **Jupyter de Microsoft**, `ipykernel` y selección del kernel de `.venv`. Un notebook puede utilizar un entorno distinto del seleccionado para scripts.

Fuentes: [extensión Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python), [inicio rápido](https://code.visualstudio.com/docs/python/python-quick-start) y [entornos en VS Code](https://code.visualstudio.com/docs/python/environments).

[Volver a preparación](README.md)

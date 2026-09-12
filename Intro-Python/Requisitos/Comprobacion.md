# Comprobación del entorno

Marca cada punto cuando lo hayas reproducido. No necesitas completar el bloque de datos para empezar.

## Antes del primer programa

- [ ] Puedo explicar la diferencia entre editor, extensión e intérprete.
- [ ] `py -3.14 --version` en Windows o `python3.14 --version` en macOS muestra Python.
- [ ] He abierto `Intro-Python` como carpeta de trabajo en VS Code.
- [ ] Está instalada la extensión Python de Microsoft.
- [ ] He seleccionado el intérprete y guardado `hola.py`.
- [ ] Puedo ejecutar el programa con el botón de VS Code y desde la terminal.
- [ ] Sé salir de `>>>` escribiendo `exit()`.

## Antes de los notebooks

- [ ] He creado `.venv` y seleccionado ese intérprete.
- [ ] Está instalada la extensión Jupyter de Microsoft.
- [ ] He instalado `requirements-inicio.txt` en `.venv`.
- [ ] He elegido `.venv` como kernel del notebook.
- [ ] He ejecutado `00_0_Primer_notebook.ipynb` desde un kernel reiniciado.

Comprueba el entorno sin mostrar credenciales:

Windows:

```powershell
.\.venv\Scripts\python.exe 01-Primeros-pasos/ejemplos/comprobar_entorno.py
```

macOS:

```bash
./.venv/bin/python 01-Primeros-pasos/ejemplos/comprobar_entorno.py
```

El script informa versión, ejecutable, carpeta, entorno virtual y disponibilidad de paquetes. Que un paquete esté disponible no prueba una conexión de base de datos ni la ejecución de todos los notebooks.

## Antes del bloque de datos

- [ ] He instalado `requirements-datos.txt` y comprobado que no hubo errores.
- [ ] Conozco qué notebooks necesitan Internet o MySQL según [su guía](../Notebooks/GUIA.md).
- [ ] Para Sakila, tengo un servidor accesible, la base de datos y las variables de entorno configuradas según [MySQL y Sakila](MySQL-Sakila.md).

[Solución de problemas](Solucion-de-problemas.md) · [Volver al curso](../README.md)

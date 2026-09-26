# Solución de problemas frecuentes

Empieza por copiar el mensaje completo y comprobar **dónde** lo has escrito. No reinstales todo ante el primer error.

| Síntoma | Qué comprobar | Qué hacer |
|---|---|---|
| `python` no se reconoce o abre la Store en Windows | `py -3.14 --version` y `pymanager list` | Reabre la terminal y usa la versión explícita. Si el gestor no funciona, revisa los alias de ejecución de aplicaciones siguiendo la documentación de Python; no desactives todos los alias indiscriminadamente |
| `py install` busca un archivo llamado `install` | Puede estar respondiendo el lanzador antiguo | Usa `pymanager install 3.14`; no es necesario desinstalar otros intérpretes |
| `python` no existe en macOS | `python3.14 --version` | Fuera de `.venv`, usa `python3.14` o el `python3` que hayas verificado |
| `python3` abre otra versión | `python3.14 -c "import sys; print(sys.executable)"` | Crea `.venv` con la versión explícita y selecciónala en VS Code |
| `code` no se reconoce | VS Code se puede abrir desde Inicio/Aplicaciones | Reabre la terminal; en macOS configura **Shell Command: Install 'code' command in PATH**. También puedes usar **File > Open Folder…** |
| `SyntaxError` al escribir una orden `pip` o `python` | ¿Ves `>>>`? | Escribe `exit()` y ejecuta la orden en la shell |
| `can't open file` o `FileNotFoundError` | Carpeta de trabajo y nombre completo | Usa `Get-Location`/`pwd` y `Get-ChildItem`/`ls`. Comprueba extensión y comillas en rutas con espacios |
| `Activate.ps1 cannot be loaded` | Política de PowerShell | Usa directamente `.\.venv\Scripts\python.exe`; no necesitas activar ni cambiar la política |
| `No module named pip` | Intérprete seleccionado | Ejecuta `python -m ensurepip --upgrade` con el intérprete de `.venv` |
| `ModuleNotFoundError` después de instalar un paquete | Ruta de instalación y kernel | Instala con el ejecutable de `.venv` y selecciona ese kernel; reinícialo si hace falta |
| No aparece **Python: Select Interpreter** | Extensión Python, carpeta y modo restringido | Comprueba que la extensión está instalada y habilitada; confía en la carpeta solo si reconoces su contenido |
| No aparece un kernel | Jupyter e `ipykernel` | Sigue [el apartado de notebooks](../sesion-2/06-notebooks.md), selecciona `.venv` y recarga la ventana |
| `NameError` en un notebook | Orden de ejecución | Reinicia el kernel y ejecuta desde la primera celda |
| Error de certificados en macOS | Distribución instalada desde python.org | Ejecuta su `Install Certificates.command`; si existe proxy corporativo, consulta a soporte |
| `No matching distribution found` | Nombre del paquete, versión y arquitectura de Python | Usa las listas del curso; revisa compatibilidad en la documentación del paquete. No fuerces versiones antiguas de SciPy |
| Error conectando a la base de datos de FraSoHome | `.env`, red y driver | Sigue la tabla de errores de [conexión con la base de datos](../sesion-2/09-conexion-y-cierre.md) |

## Una comprobación útil

En un archivo Python o en una celda de código puedes ejecutar:

```python
import sys
from pathlib import Path

print(sys.executable)
print(Path.cwd())
```

La primera línea de salida identifica **quién ejecuta**; la segunda, **desde dónde**. Compara la salida en terminal y notebook cuando veas comportamientos distintos.

Si pides ayuda, incluye sistema operativo, comando o celda, error completo y ruta del intérprete. No incluyas contraseñas ni el contenido de `.env`.

Referencias: [problemas de Python en Windows](https://docs.python.org/3/using/windows.html#troubleshooting), [entornos en VS Code](https://code.visualstudio.com/docs/python/environments) y [kernels](https://code.visualstudio.com/docs/datascience/jupyter-kernel-management).

[Volver a los anexos](README.md)

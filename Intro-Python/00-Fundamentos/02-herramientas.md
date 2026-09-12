# 2. Lenguaje, intérprete, editor e IDE

## Las piezas y su responsabilidad

| Concepto | Qué es | Ejemplo en el curso |
|---|---|---|
| Lenguaje | Reglas con las que expresamos instrucciones | Python |
| Código fuente | El texto de esas instrucciones | `print("Hola")` |
| Intérprete | Programa que ejecuta código del lenguaje | CPython, instalado desde python.org |
| Editor | Aplicación para crear y modificar archivos de texto | Visual Studio Code |
| IDE | Entorno de desarrollo integrado: reúne edición, ejecución, depuración y otras herramientas | IDLE; VS Code ofrece muchas de estas capacidades mediante extensiones |
| Extensión o complemento | Añade capacidades a una aplicación | Python de Microsoft para VS Code |
| Terminal | Ventana en la que interactúas con programas de texto | Terminal de macOS o terminal integrada de VS Code |
| Shell | Programa que recibe e interpreta órdenes de la terminal | PowerShell en Windows; zsh habitualmente en macOS |
| CLI | Interfaz de línea de comandos: forma de usar una herramienta escribiendo órdenes | `python --version` |
| REPL | Sesión interactiva: lee una instrucción, la ejecuta y muestra su resultado | La consola de Python con el indicador `>>>` |
| Depurador | Permite detener el programa e inspeccionarlo paso a paso | Depurador de Python en VS Code |

**Python, VS Code y la extensión se instalan por separado.** La extensión conecta el editor con un intérprete; no sustituye al intérprete. Visual Studio Code y Visual Studio son productos distintos: descarga Visual Studio **Code**.

La expresión «lenguaje interpretado» es una primera aproximación. En CPython, el código se compila a bytecode que ejecuta su máquina virtual. No hace falta estudiar ese mecanismo ahora; lo relevante es que ejecutaremos nuestros archivos mediante el intérprete.

## Qué sucede al ejecutar un archivo

Guardas `hola.py` en el editor. Al pedir que se ejecute, se inicia el intérprete seleccionado y este procesa el archivo. La salida aparece en la terminal. La misma tarea también se puede iniciar escribiendo una orden en la terminal, sin pulsar un botón del editor.

Una extensión de Python, un paquete de Python y un archivo Python son cosas diferentes:

| Quiero… | Utilizo… |
|---|---|
| Ayuda para escribir Python dentro de VS Code | Una extensión instalada en VS Code |
| Añadir funciones de análisis a mi programa | Un paquete como `pandas`, instalado en un entorno de Python |
| Guardar mis instrucciones | Un archivo con extensión `.py` |
| Ejecutar instrucciones de una en una | La REPL de Python |

## Lo que llegará después

Un **entorno virtual** es una carpeta con un intérprete asociado y paquetes aislados para un proyecto. Usaremos el nombre `.venv`. Un **notebook** (`.ipynb`) contiene celdas de código, texto y resultados. Su **kernel** es el proceso que ejecuta las celdas y mantiene las variables entre ejecuciones. El kernel se debe vincular al entorno correcto.

No intentes dominar todo este vocabulario de memoria. Pregúntate: «¿Estoy editando un archivo, dando una orden al sistema o ejecutando Python?».

**Actividad:** explica por qué instalar únicamente VS Code no basta para ejecutar `hola.py`. Después identifica qué pieza permite poner un punto de interrupción y revisar el valor de una variable.

Fuentes: [configuración de Python en VS Code](https://code.visualstudio.com/docs/python/python-quick-start), [extensión Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python), [uso del intérprete](https://docs.python.org/3/tutorial/interpreter.html) y [notebooks en VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).

[Anterior](01-que-es-programar.md) · [Siguiente: terminal y archivos](03-terminal-y-archivos.md)

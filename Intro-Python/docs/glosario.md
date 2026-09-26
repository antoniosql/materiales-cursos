# Glosario

[Inicio del seminario](README.md) › Glosario

Palabras que aparecen en el seminario, explicadas de forma sencilla y ordenadas alfabéticamente. Entre paréntesis, la sesión y el apartado donde se explican con más detalle.

| Término | Qué significa |
|---|---|
| **Acumulador** | Variable que empieza en cero y va sumando (o contando) algo en cada vuelta de un bucle ([S2 · 1](sesion-2/01-listas-diccionarios-y-bucles.md)) |
| **Algoritmo** | Secuencia de pasos precisos, sin ambigüedades, para resolver un problema ([S1 · 2](sesion-1/02-que-es-programar.md)) |
| **Argumento** | Valor concreto que le pasas a una función al llamarla. En `calcular_importe(2, 31.63)`, los argumentos son `2` y `31.63` |
| **Array** | Colección de NumPy con elementos del mismo tipo, con la que se opera de golpe, sin bucles ([S2 · 7](sesion-2/07-numpy.md)) |
| **Base de datos** | Sistema que guarda grandes cantidades de datos en tablas y permite consultarlos con SQL ([S2 · 9](sesion-2/09-conexion-y-cierre.md)) |
| **Biblioteca estándar** | Conjunto de módulos que vienen incluidos con Python, como `math`, `statistics` o `datetime` ([S2 · 2](sesion-2/02-funciones-y-modulos.md)) |
| **Bit** | La unidad mínima de información: un 0 o un 1 ([S1 · 3](sesion-1/03-como-entiende-el-ordenador-un-programa.md)) |
| **Bloque** | Grupo de líneas sangradas que dependen de un `if`, `for` o `def` ([S1 · 10](sesion-1/10-tomar-decisiones.md)) |
| **`bool` (booleano)** | Tipo de dato con solo dos valores posibles: `True` (verdadero) o `False` (falso) |
| **Bucle** | Instrucción que repite un bloque varias veces. El bucle `for` lo repite una vez por cada elemento de una lista ([S2 · 1](sesion-2/01-listas-diccionarios-y-bucles.md)) |
| **Byte** | Grupo de 8 bits. Puede tomar 256 valores distintos |
| **Bytecode** | Formato intermedio al que CPython traduce tu código antes de ejecutarlo en su máquina virtual. Se guarda en carpetas `__pycache__` ([S1 · 3](sesion-1/03-como-entiende-el-ordenador-un-programa.md)) |
| **Clave** | En un diccionario, la etiqueta con la que se busca un valor. En `{"nombre": "Cuadro Atlas"}`, la clave es `"nombre"` |
| **Clone** | Descargar un repositorio remoto completo, con su historial, en un ordenador nuevo |
| **Código** | Texto con instrucciones escritas en un lenguaje de programación |
| **Código máquina** | Instrucciones en binario que el procesador ejecuta directamente |
| **Comando** | Orden que se escribe en la terminal, como `pwd` o `python hola.py` ([S1 · 6](sesion-1/06-carpetas-y-terminal.md)) |
| **Comentario** | Texto precedido de `#` que Python ignora. Sirve para dejar notas a las personas que lean el código |
| **Commit** | En Git, una "foto" de los archivos en un momento dado, con un mensaje que explica qué cambió ([S2 · 4](sesion-2/04-git-y-github.md)) |
| **Compilador** | Programa que traduce todo el código de un lenguaje a código máquina antes de ejecutarlo. Lo usan lenguajes como C o Rust ([S1 · 3](sesion-1/03-como-entiende-el-ordenador-un-programa.md)) |
| **Concatenar** | Unir textos. `"Madrid" + " Centro"` da `"Madrid Centro"` |
| **Condición** | Expresión que da `True` o `False`, como `stock_cierre < stock_minimo` |
| **CPU (procesador)** | La pieza del ordenador que ejecuta las instrucciones |
| **CPython** | El intérprete oficial de Python, escrito en C. Es el que se descarga de python.org |
| **CSV** | Tabla guardada como texto: una fila por línea y los valores separados por comas ([S2 · 8](sesion-2/08-pandas.md)) |
| **Cursor** | Objeto con el que se ejecutan consultas SQL y se recogen sus resultados desde Python ([S2 · 9](sesion-2/09-conexion-y-cierre.md)) |
| **DataFrame** | Tabla de pandas, con filas y columnas con nombre ([S2 · 8](sesion-2/08-pandas.md)) |
| **Diccionario** | Colección de pares **clave: valor** entre llaves `{}`. Es como una ficha con etiquetas ([S2 · 1](sesion-2/01-listas-diccionarios-y-bucles.md)) |
| **Editor** | Programa para escribir código. Usamos Visual Studio Code |
| **Ejecutar** | Pedir al ordenador que siga las instrucciones de un programa. También se dice "correr" (del inglés *run*) |
| **Entorno virtual** | Carpeta del proyecto (normalmente `.venv`) con su propio Python y sus propios paquetes, aislados del resto del ordenador ([S2 · 5](sesion-2/05-paquetes-y-entornos-virtuales.md)) |
| **`.env`** | Archivo con datos privados, como contraseñas, que el programa lee y que nunca se sube a GitHub ([S2 · 9](sesion-2/09-conexion-y-cierre.md)) |
| **Extensión** | Añadido que amplía lo que sabe hacer un programa. La extensión *Python* hace que VS Code entienda Python |
| **f-string** | Texto con una `f` delante en el que se pueden insertar variables entre llaves: `f"Total: {total:.2f}"` ([S1 · 9](sesion-1/09-preguntar-y-responder.md)) |
| **Filtrado booleano** | Quedarse con los elementos o filas en los que una condición es `True`: `precios[precios > 150]` ([S2 · 7](sesion-2/07-numpy.md)) |
| **`float`** | Tipo de dato para números con decimales, como `221.99`. Se escriben con **punto** y se guardan en 64 bits, lo que hace que algunos decimales no sean exactos ([S1 · 8](sesion-1/08-tipos-de-datos-y-variables.md)) |
| **Función** | Bloque de código con nombre que recibe datos, hace un trabajo y puede devolver un resultado ([S2 · 2](sesion-2/02-funciones-y-modulos.md)) |
| **Git** | Programa de control de versiones: guarda el historial de cambios de una carpeta ([S2 · 4](sesion-2/04-git-y-github.md)) |
| **GitHub** | Servicio web donde se guarda una copia remota de los repositorios de Git ([S2 · 4](sesion-2/04-git-y-github.md)) |
| **`.gitignore`** | Archivo que indica a Git qué archivos no debe guardar nunca, como `.venv` o `.env` ([S2 · 4](sesion-2/04-git-y-github.md)) |
| **`groupby`** | Operación de pandas que agrupa las filas por el valor de una columna y calcula algo para cada grupo ([S2 · 8](sesion-2/08-pandas.md)) |
| **IDE** | Entorno de desarrollo integrado: un editor con herramientas para escribir, ejecutar y revisar código |
| **Importar** | Traer a tu programa las funciones de un módulo con `import` ([S2 · 2](sesion-2/02-funciones-y-modulos.md)) |
| **Indentación o sangría** | Espacios al principio de una línea que indican a qué bloque pertenece. En Python es obligatoria |
| **Índice** | Posición de un elemento en una lista o de un carácter en un texto. **Se empieza a contar desde 0** |
| **Inmutable** | Que no se puede modificar después de crearlo. Los números y los textos son inmutables ([S2 · 1](sesion-2/01-listas-diccionarios-y-bucles.md)) |
| **`int`** | Tipo de dato para números enteros, como `2` o `1850`. En Python no tienen tamaño máximo |
| **Intérprete** | Programa que lee el código y lo ejecuta sobre la marcha. En Python, CPython ([S1 · 3](sesion-1/03-como-entiende-el-ordenador-un-programa.md)) |
| **Kernel** | El proceso de Python que ejecuta las celdas de un notebook y guarda sus variables ([S2 · 6](sesion-2/06-notebooks.md)) |
| **Lenguaje de programación** | Idioma con reglas estrictas para dar instrucciones a un ordenador |
| **Lista** | Colección ordenada y modificable de valores entre corchetes `[]` ([S2 · 1](sesion-2/01-listas-diccionarios-y-bucles.md)) |
| **Local** | El repositorio que está en tu ordenador, donde trabajas y haces los commits ([S2 · 4](sesion-2/04-git-y-github.md)) |
| **Markdown** | Lenguaje de marcado ligero para dar formato a textos con símbolos sencillos como `#` o `**` ([S2 · 3](sesion-2/03-markdown.md)) |
| **Memoria (RAM)** | Donde se guardan los programas y datos que se están usando. Se borra al apagar el ordenador ([S1 · 3](sesion-1/03-como-entiende-el-ordenador-un-programa.md)) |
| **Método** | Función que pertenece a un valor y se escribe con un punto detrás de él: `"madrid".upper()` ([S1 · 8](sesion-1/08-tipos-de-datos-y-variables.md)) |
| **Módulo** | Archivo `.py` con funciones que se pueden importar desde otros programas ([S2 · 2](sesion-2/02-funciones-y-modulos.md)) |
| **Mutable** | Que se puede modificar después de crearlo. Las listas y los diccionarios son mutables ([S2 · 1](sesion-2/01-listas-diccionarios-y-bucles.md)) |
| **NaN** | *Not a Number*: la marca que usan NumPy y pandas para un dato que falta ([S2 · 8](sesion-2/08-pandas.md)) |
| **`None`** | Valor que representa la ausencia de dato. En las bases de datos se llama `NULL` ([S1 · 8](sesion-1/08-tipos-de-datos-y-variables.md)) |
| **Notebook** | Documento `.ipynb` con celdas de código y de Markdown que se ejecutan una a una y guardan sus resultados ([S2 · 6](sesion-2/06-notebooks.md)) |
| **NumPy** | Paquete de cálculo numérico, escrito por dentro en C, base de casi todo el análisis de datos en Python ([S2 · 7](sesion-2/07-numpy.md)) |
| **Operación vectorizada** | Operación que se aplica a todos los elementos de un array o columna a la vez, sin bucle ([S2 · 7](sesion-2/07-numpy.md)) |
| **pandas** | Paquete para trabajar con tablas de datos en Python ([S2 · 8](sesion-2/08-pandas.md)) |
| **Paquete** | Conjunto de módulos publicado para que otros lo usen. Los de terceros, como pandas, se instalan con `pip` ([S2 · 5](sesion-2/05-paquetes-y-entornos-virtuales.md)) |
| **Parámetro** | Nombre que recibe un dato dentro de una función. En `def calcular_importe(cantidad, precio)`, los parámetros son `cantidad` y `precio` |
| **PATH** | Lista de carpetas en las que el sistema busca los programas cuando escribes su nombre en la terminal |
| **`pip`** | Programa que instala paquetes desde PyPI ([S2 · 5](sesion-2/05-paquetes-y-entornos-virtuales.md)) |
| **Prompt** | Texto que muestra la terminal cuando espera una orden, por ejemplo `PS C:\...>` o `>>>` |
| **Pull** | Traer al repositorio local los commits nuevos del remoto ([S2 · 4](sesion-2/04-git-y-github.md)) |
| **Push** | Subir los commits del repositorio local al remoto ([S2 · 4](sesion-2/04-git-y-github.md)) |
| **PyPI** | El almacén público de paquetes de Python (pypi.org) |
| **README** | Archivo `README.md` que explica qué es un proyecto y cómo se usa. GitHub lo muestra como portada ([S2 · 3](sesion-2/03-markdown.md)) |
| **Remoto** | La copia del repositorio en GitHub ([S2 · 4](sesion-2/04-git-y-github.md)) |
| **REPL** | Modo interactivo de Python, con el símbolo `>>>`, en el que cada línea se ejecuta al pulsar Intro ([S1 · 6](sesion-1/06-carpetas-y-terminal.md)) |
| **Repositorio** | Carpeta cuyo historial de versiones controla Git ([S2 · 4](sesion-2/04-git-y-github.md)) |
| **`requirements.txt`** | Lista de los paquetes que necesita un proyecto, para poder recrear su entorno ([S2 · 5](sesion-2/05-paquetes-y-entornos-virtuales.md)) |
| **`return`** | Instrucción que hace que una función devuelva un resultado ([S2 · 2](sesion-2/02-funciones-y-modulos.md)) |
| **Ruta** | Dirección de un archivo o carpeta, como `C:\Users\Ana\Documents\curso-python\hola.py` |
| **Script** | Archivo `.py` con un programa que se ejecuta de principio a fin |
| **Series** | Una columna de un DataFrame de pandas ([S2 · 8](sesion-2/08-pandas.md)) |
| **Shell** | Programa que interpreta las órdenes que escribes en la terminal. En Windows, PowerShell |
| **SQL** | Lenguaje para consultar bases de datos: `SELECT COUNT(*) FROM raw_retail.productos` ([S2 · 9](sesion-2/09-conexion-y-cierre.md)) |
| **`str` (texto o cadena)** | Tipo de dato para textos: una secuencia de caracteres Unicode. Van siempre entre comillas: `"Madrid Centro"` |
| **Terminal** | Ventana en la que se dan órdenes al ordenador escribiendo |
| **Tipado dinámico** | El tipo lo tiene el valor, no la variable: una misma variable puede guardar valores de tipos distintos ([S1 · 8](sesion-1/08-tipos-de-datos-y-variables.md)) |
| **Tipado fuerte** | El lenguaje no mezcla tipos por su cuenta: `"2" + 2` da error en Python ([S1 · 8](sesion-1/08-tipos-de-datos-y-variables.md)) |
| **Tipo de dato** | Clase de valor (`int`, `float`, `str`, `bool`, `None`...). Determina cómo se guarda y qué operaciones se pueden hacer con él |
| **Traceback** | Mensaje de error de Python. Se lee de abajo arriba ([S1 · 11](sesion-1/11-cuando-algo-falla.md)) |
| **Tupla** | Colección ordenada como una lista, pero inmutable. Se escribe entre paréntesis `()` |
| **Unicode** | Tabla universal que asigna un número a cada carácter de cualquier idioma. UTF-8 es la forma más habitual de guardarlo en bytes |
| **Valor** | Un dato concreto: `2`, `31.63`, `"Cuadro Atlas"`, `True` |
| **Variable** | Nombre que apunta a un valor guardado en memoria. Se crea con `=` ([S1 · 8](sesion-1/08-tipos-de-datos-y-variables.md)) |

---

[Inicio del seminario](README.md) · [Sesión 1](sesion-1/README.md) · [Sesión 2](sesion-2/README.md)

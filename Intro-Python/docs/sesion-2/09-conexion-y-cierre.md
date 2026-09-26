# 9 · Conexión con la base de datos y cierre

[Inicio](../README.md) › [Sesión 2](README.md) › Conexión con la base de datos y cierre

**Tiempo aproximado:** 10 minutos

## La pregunta de Marta

> *"Lo de los archivos CSV está bien, pero cada vez que quiero datos nuevos alguien tiene que exportarlos del sistema y mandármelos. ¿No puedes leerlos directamente de donde están?"*

Sí. Los datos de una empresa no suelen vivir en archivos sueltos, sino en **bases de datos**. FraSoHome tiene la suya en la nube, y Python puede conectarse a ella.

## Qué es una base de datos

Una **base de datos** es un sistema especializado en guardar grandes cantidades de datos de forma segura y ordenada, y en permitir que muchas personas y programas los consulten a la vez. Los datos se organizan en **tablas**, como las que acabas de manejar con pandas, y se consultan con un lenguaje llamado **SQL**.

| Pieza | Qué es | En FraSoHome |
|---|---|---|
| **Servidor** | El ordenador (en este caso, en la nube) donde funciona la base de datos | Un servidor de Azure SQL, el servicio de bases de datos en la nube de Microsoft |
| **Base de datos** | Un conjunto de tablas relacionadas | `frasohome` |
| **Esquema** | Una carpeta que agrupa tablas dentro de la base de datos | `raw_retail`: los datos de venta, tal como salen de los sistemas |
| **Tabla** | Una tabla de datos, con filas y columnas | `productos`, `tiendas`, `ventas_pos`... |
| **Usuario y contraseña** | Tus credenciales de acceso. El vuestro solo permite **leer**, no modificar | Te los da el profesor |
| **Driver** | El paquete que permite a Python "hablar" con la base de datos | `mssql-python`, que ya instalaste con `requirements.txt` |

Una consulta SQL se lee casi como una frase en inglés:

```sql
SELECT COUNT(*) FROM raw_retail.productos
```

*"Selecciona el número de filas de la tabla productos del esquema raw_retail."*

## Las credenciales, fuera del código

Para conectarte necesitas un usuario y una contraseña. **Nunca** se escriben dentro del código: si lo subes a GitHub, cualquiera con acceso al repositorio las vería, y quedarían en el historial para siempre.

La práctica habitual es guardarlas en un archivo **`.env`**, que está en el `.gitignore` desde el [apartado 4](04-git-y-github.md), y leerlas desde Python con el paquete `python-dotenv`.

> **Pruébalo.**
>
> 1. Descarga [ejemplo.env](ejemplos/ejemplo.env) y guárdalo en tu carpeta `curso-python` con el nombre **`.env`**, empezando por punto y sin nada más.
> 2. Rellena el servidor, el usuario y la contraseña que te dará el profesor.
> 3. Comprueba en Source Control que `.env` **no aparece** como cambio: Git lo está ignorando.

## Tu primera conexión

> **Pruébalo.** Descarga [03_comprobar_conexion.py](ejemplos/03_comprobar_conexion.py) en `curso-python`, léelo con calma (está comentado paso a paso) y ejecútalo con el botón ▶. Si todo va bien, verás:
>
> ```text
> Conectado a la base de datos frasohome
> Productos en la base de datos: 101
> ```
>
> seguido de una pequeña tabla con los cinco primeros productos.

**Son los mismos 101 productos del archivo `productos.csv`**, pero esta vez vienen directamente de la base de datos de la empresa.

El programa hace, en orden:

1. Lee las credenciales del `.env` con `load_dotenv()` y `os.getenv()`.
2. Construye la **cadena de conexión**: un texto con el servidor, la base de datos, el usuario, la contraseña y la indicación de que la conexión va **cifrada**.
3. Se conecta con `mssql_python.connect()` dentro de un `try`, por si falla.
4. Ejecuta una consulta SQL con un **cursor** y recoge el resultado con `fetchone()`.
5. Ejecuta otra consulta, recoge las filas con `fetchall()` y las convierte en un **DataFrame** de pandas.
6. **Cierra** la conexión.

> **Pruébalo.** Mira el tipo de la columna `precio_venta` del DataFrame con `productos.dtypes`. ¿Es número o texto? Pista: en el esquema `raw_retail` los datos se guardaron tal y como salían de los sistemas, errores incluidos.

### Si no conecta

| Mensaje | Causa probable | Qué hacer |
|---|---|---|
| `Faltan datos en el archivo .env` | El archivo no se llama exactamente `.env`, no está en `curso-python` o le falta algún dato | Revisa el nombre (sin `.txt` al final) y el contenido |
| `Login failed for user` | Usuario o contraseña incorrectos | Revisa el `.env`: sin espacios ni comillas de más |
| `Client unable to establish connection` o un error de tiempo de espera | La red no llega al servidor (a veces por el cortafuegos de la red de la empresa o de la universidad) | Avisa al profesor |
| Mac: un error que menciona **OpenSSL** o `libssl` | En Mac, `mssql-python` necesita la librería OpenSSL | Avisa al profesor. Si usas Homebrew, se instala con `brew install openssl` |

> **Cuidado.** La base de datos es compartida por todo el grupo. Tu usuario solo puede **leer**, así que no puedes estropear nada, pero sí saturarla: no lances consultas en bucle.

Haz un último commit (`Añade la comprobación de conexión`) y **Sync Changes**. Comprueba en GitHub que `.env` **no** se ha subido.

---

## Cierre del seminario

### Lo que has conseguido

Hace dos sesiones no sabías qué era un intérprete. Ahora tienes:

| Lo que sabes hacer | Con qué |
|---|---|
| Entender cómo se ejecuta un programa | Intérprete, bytecode, memoria, tipos de datos |
| Escribir programas que calculan, preguntan y deciden | Variables, `input`, `if`, `try` |
| Trabajar con colecciones de datos | Listas, diccionarios, bucles, funciones y módulos |
| Documentar tu trabajo | Markdown y un `README.md` |
| Guardar el historial y trabajar con un remoto | Git y GitHub: commit, push y pull |
| Preparar un entorno reproducible | `.venv` y `requirements.txt` |
| Explorar y analizar datos | Notebooks, NumPy y pandas |
| Leer datos de una base de datos de forma segura | `mssql-python`, SQL y `.env` |

Y un repositorio en GitHub que lo demuestra.

### Autoevaluación

- [ ] Explicar qué es un entorno virtual y por qué `.venv` no se sube a GitHub.
- [ ] Explicar la diferencia entre commit, push y pull.
- [ ] Escribir un `README.md` con títulos, listas y una tabla.
- [ ] Explicar por qué `precios * 1.21` funciona con un array de NumPy y no con una lista.
- [ ] Leer un CSV con pandas y explorarlo con `head`, `info` y `describe`.
- [ ] Convertir a número una columna que llega como texto.
- [ ] Filtrar filas con una condición y agrupar con `groupby`.
- [ ] Explicar por qué las contraseñas van en un `.env` y no en el código.

### Retos para practicar (voluntarios)

Con el catálogo ya limpio (precios convertidos a número y categorías unificadas):

1. ¿Cuántos productos hay de cada **marca**? ¿Cuál es la marca con el precio medio más alto?
2. ¿Qué porcentaje del catálogo está **descatalogado**? Pista: `value_counts(normalize=True)`.
3. Crea una columna `margen_pct` con el margen en porcentaje y muestra los 5 productos con **menor** margen porcentual. ¿Aparece alguno con datos imposibles?
4. Dibuja un gráfico de barras con el **número de productos activos por categoría**.

<details markdown>
<summary>Ver soluciones</summary>

```python
# 1
productos["marca"] = productos["marca"].str.strip()
productos["marca"].value_counts()
productos.groupby("marca")["precio_venta"].mean().sort_values(ascending=False).head(1)

# 2
productos["estado_producto"].value_counts(normalize=True) * 100

# 3
productos["margen_pct"] = productos["margen"] / productos["precio_venta"] * 100
productos.sort_values("margen_pct")[["nombre_producto", "precio_venta", "coste_unitario", "margen_pct"]].head(5)

# 4
activos = productos[productos["estado_producto"] == "Activo"]
activos["categoria"].value_counts().plot(kind="bar", title="Productos activos por categoría")
```

En el reto 1, si no usas `.str.strip()`, la marca **FraSoHome** aparece dos veces: una de ellas es `"FraSoHome "`, con un espacio al final y un solo producto. Una vez limpia, FraSoHome es la marca con el precio medio más alto (423,83 €).

En el reto 3, el *Espejo Élite 80cm* (precio 0) da un margen de `-inf` (menos infinito) por dividir entre cero: pandas no se detiene como Python, pero el resultado no tiene sentido. Otro dato que habría que revisar con el equipo de Marta.

</details>

### Para seguir aprendiendo

- ***Python for Data Analysis***, de Wes McKinney, el creador de pandas. Está disponible gratis en inglés en su web.
- La guía **"10 minutes to pandas"** de la documentación oficial de pandas.
- ***Piensa en Python*** (*Think Python*), de Allen B. Downey, gratuito en castellano, para reforzar los fundamentos.

> Marta te escribe un último mensaje: *"En dos días has pasado de no saber qué era un programa a leer los datos de mi tienda directamente de la base de datos. Ahora sí que tengo preguntas para ti."*

---

[← Anterior: Primeros datos con pandas](08-pandas.md) · [Índice de la sesión](README.md) · [Inicio del seminario](../README.md)

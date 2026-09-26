# Comprueba la conexión con la base de datos de FraSoHome
# Necesita un archivo .env en la misma carpeta, con los datos de conexión.

import os

import mssql_python
import pandas as pd
from dotenv import load_dotenv

# 1. Leer los datos de conexión del archivo .env (nunca escritos en el código)
load_dotenv()
servidor = os.getenv("SQL_SERVER")
base_datos = os.getenv("SQL_DATABASE")
usuario = os.getenv("SQL_USER")
contrasena = os.getenv("SQL_PASSWORD")

if not servidor or not usuario or not contrasena:
    print("Faltan datos en el archivo .env. Revisa que existe y que está completo.")
    raise SystemExit

# 2. Construir la cadena de conexión
cadena = (
    f"Server=tcp:{servidor},1433;"
    f"Database={base_datos};"
    f"Uid={usuario};"
    f"Pwd={contrasena};"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
)

# 3. Conectar
try:
    conexion = mssql_python.connect(cadena)
except mssql_python.Error as error:
    print("No se ha podido conectar con la base de datos:")
    print(error)
    raise SystemExit

print(f"Conectado a la base de datos {base_datos}")

# 4. Primera consulta: ¿cuántos productos hay?
cursor = conexion.cursor()
cursor.execute("SELECT COUNT(*) FROM raw_retail.productos")
total = cursor.fetchone()[0]
print(f"Productos en la base de datos: {total}")

# 5. Segunda consulta: los cinco primeros productos, en un DataFrame
cursor.execute(
    "SELECT TOP 5 product_id, nombre_producto, categoria, precio_venta "
    "FROM raw_retail.productos ORDER BY product_id"
)
filas = cursor.fetchall()
columnas = [descripcion[0] for descripcion in cursor.description]
productos = pd.DataFrame([tuple(fila) for fila in filas], columns=columnas)
print(productos)

# 6. Cerrar siempre la conexión al terminar
conexion.close()

"""Diagnóstico de solo lectura: ejecutar desde la carpeta Intro-Python."""
import importlib.util
from pathlib import Path
import sys

print("Python:", sys.version.split()[0])
print("Ejecutable:", sys.executable)
print("Carpeta de trabajo:", Path.cwd())
print("Entorno virtual:", "sí" if sys.prefix != sys.base_prefix else "no")

paquetes = {
    "ipykernel": "ipykernel (notebooks)",
    "pandas": "pandas (análisis)",
    "numpy": "numpy (análisis)",
    "matplotlib": "matplotlib (gráficos)",
    "seaborn": "seaborn (gráficos)",
    "scipy": "scipy (cálculo científico)",
    "sklearn": "scikit-learn (preparación de variables)",
    "mysql.connector": "mysql-connector-python (Sakila)",
    "dotenv": "python-dotenv (Sakila)",
}
for modulo, descripcion in paquetes.items():
    try:
        disponible = importlib.util.find_spec(modulo) is not None
    except (ModuleNotFoundError, ValueError):
        disponible = False
    estado = "disponible" if disponible else "no encontrado"
    print(f"{descripcion}: {estado}")

print("Los scripts iniciales no requieren estos paquetes.")
print("Disponibilidad no equivale a validar importaciones ni conexiones MySQL.")

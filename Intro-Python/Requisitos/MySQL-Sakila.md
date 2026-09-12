# Preparación del bloque MySQL y Sakila

Este bloque llega después de los fundamentos. Los notebooks originales utilizan un servidor **MySQL** con la base de datos de ejemplo **Sakila**. Un servidor de base de datos guarda y consulta los datos; `mysql-connector-python` permite que nuestro programa se conecte a él. Instalar el conector no instala MySQL ni Sakila.

## Preparación con el docente

1. Disponer de un servidor MySQL y cargar Sakila siguiendo la [guía oficial de instalación de Sakila](https://dev.mysql.com/doc/sakila/en/sakila-installation.html), o utilizar el servidor preparado por el docente.
2. Obtener el nombre o dirección del servidor, usuario y contraseña, y comprobar que acepta conexiones desde tu equipo. Los ejemplos usan el puerto predeterminado del conector; si tu servidor tiene otro puerto, se debe adaptar la conexión en la copia de trabajo.
3. Instalar [requirements-datos.txt](../requirements-datos.txt) dentro de `.venv`.
4. Copiar [.env.example](../.env.example) a un archivo llamado `.env` en `Intro-Python` y rellenar sus valores reales localmente. Para evitar dudas sobre su búsqueda, ejecuta los notebooks con la carpeta de trabajo `Intro-Python` o `Intro-Python/Notebooks`.

Los nombres que esperan los notebooks son `SERVIDOR_MYSQL`, `USUARIO_MYSQL` y `PASSWORD_MYSQL`; la base de datos `sakila` figura en el código. `.env` queda excluido de Git. La plantilla contiene únicamente campos vacíos.

No ejecutes automáticamente un notebook completo para comprobar la conexión. Revisa primero las consultas y el [mapa de dependencias](../Notebooks/GUIA.md). Los ejemplos con acceso a datos externos no forman parte de la comprobación del bloque nuevo desde cero.

Referencias: [Sakila](https://dev.mysql.com/doc/sakila/en/), [Connector/Python](https://dev.mysql.com/doc/connector-python/en/connector-python-installation-binary.html) y [python-dotenv](https://bbc2.github.io/python-dotenv/).

[Volver a preparación](README.md)

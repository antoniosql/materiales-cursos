# Introducción a Big Data

Materiales de datos del curso **Introducción a Big Data**.

Este directorio contiene los **conjuntos de datos** que se utilizan durante las
demostraciones y los laboratorios del curso. Los notebooks y guiones de las
sesiones se entregan en la plataforma de trabajo del curso (Databricks / Fabric /
Colab, según la edición), por lo que aquí solo se versionan los datos de partida
y los recursos gráficos de apoyo.

## Contenido

| Elemento | Descripción |
|---|---|
| [datos/](datos/) | Datasets del curso (ver tabla más abajo) |
| [Medallion.png](Medallion.png) | Diagrama de la arquitectura *medallion* (bronze / silver / gold) usado en las sesiones de arquitectura de datos |
| [LICENSE](LICENSE) | Licencia MIT |

## Datasets

| Fichero | Descripción | Formato |
|---|---|---|
| `datos/titanic_data.csv` | Pasajeros del Titanic. Dataset pequeño para las primeras pruebas de carga y exploración | CSV |
| `datos/Tiendas24H.zip` | Datos de la cadena ficticia *Tiendas 24H* (ventas, tiendas, productos) usados en los ejercicios de modelado | ZIP |
| `datos/instacart_2017_05_01_chunks.zip` + `.z01`…`.z08` | Pedidos de Instacart (2017). Volumen medio, pensado para ejercicios de agregación y particionado | ZIP multivolumen |
| `datos/sales_records_5M_chunks.zip` + `.z07` | 5 millones de registros de ventas. Volumen alto, para ilustrar el coste del procesamiento distribuido | ZIP multivolumen |

### Cómo descomprimir los ZIP multivolumen

Los ficheros grandes están divididos en volúmenes (`.z01`, `.z02`, …) para poder
almacenarlos en Git. **Descarga todos los volúmenes junto al `.zip` final** antes
de descomprimir; el fichero `.zip` por sí solo no sirve.

**Windows (7-Zip)**

Haz clic derecho sobre el fichero `.zip` (no sobre los `.z01`) y elige
*7-Zip → Extraer aquí*. 7-Zip localiza el resto de volúmenes automáticamente.

**Linux / macOS**

```bash
cd datos
zip -s 0 instacart_2017_05_01_chunks.zip --out instacart_completo.zip
unzip instacart_completo.zip
```

## Cómo usar estos datos

1. Clona el repositorio o descarga únicamente la carpeta `datos/`.
2. Descomprime el dataset que indique el instructor en cada sesión.
3. Sube el fichero resultante al entorno de trabajo del curso (DBFS, OneLake,
   almacenamiento de objetos o el sistema de ficheros local, según la sesión).

> Aviso: algunos ficheros superan los 100 MB una vez descomprimidos. Ten espacio
> libre en disco antes de extraerlos.

## Licencia

Código y materiales bajo licencia [MIT](LICENSE). Los datasets mantienen la
licencia de sus fuentes originales y se incluyen únicamente con fines docentes.

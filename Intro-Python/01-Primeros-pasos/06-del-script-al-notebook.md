# 6. Del script al notebook

Ya puedes construir un programa pequeño. Ahora utilizaremos notebooks para combinar cálculos y explicaciones, como en el bloque de análisis de datos.

| Aspecto | Script `.py` | Notebook `.ipynb` |
|---|---|---|
| Organización | Archivo de instrucciones | Celdas de código y Markdown |
| Ejecución habitual | El archivo empieza desde el principio en un proceso nuevo | Las celdas comparten variables del kernel |
| Texto explicativo | Comentarios | Celdas Markdown |
| Resultado visible | Necesita `print` u otra salida explícita | Puede mostrar automáticamente la última expresión |
| Riesgo común | Ejecutar otro archivo o no guardar | Reutilizar variables de celdas ejecutadas fuera de orden |

Prepara [el entorno virtual](../Requisitos/Entorno-y-paquetes.md) y [Jupyter](../Requisitos/Jupyter.md). Abre [00_0_Primer_notebook.ipynb](../Notebooks/00_0_Primer_notebook.ipynb), selecciona `.venv` y realiza sus prácticas.

El primer notebook utiliza datos definidos en las propias celdas. No necesita MySQL, Pandas ni descargas de datos. Ejecuta todo desde un kernel reiniciado y compara los resultados con los del miniproyecto.

Después continúa con [la guía de los notebooks originales](../Notebooks/GUIA.md): Markdown, funcionamiento de notebooks, elementos del lenguaje y módulos. Las guías señalan qué ejemplos necesitan preparación adicional.

Fuentes: [notebooks de VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) y [documentación de Jupyter Notebook](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html).

[Volver al curso](../README.md)

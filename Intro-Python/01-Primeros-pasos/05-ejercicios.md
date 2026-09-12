# 5. Ejercicios y miniproyecto

Guarda cada respuesta en un archivo de `mis-ejercicios` y ejecútalo desde la terminal. Puedes consultar las lecciones. Antes de mirar las soluciones, compara tus resultados con los casos indicados.

## Ejercicio 1. Conversión de minutos

Define una variable `minutos` y calcula cuántos segundos representa. Muestra una frase. Prueba `5` → `300`, `0` → `0` y `12` → `720`.

Pista: no necesitas ninguna biblioteca. [Solución](soluciones/01_minutos.py).

## Ejercicio 2. Entrada y decisión

Pregunta cuántas personas van a asistir a un taller de 12 plazas. Si la cantidad está entre 0 y 12, muestra cuántas plazas quedan. Si supera 12, muestra que no hay capacidad; si es negativa o no es un entero, muestra un mensaje apropiado.

Prueba `5` → `7` plazas, `12` → `0`, `13` → sin capacidad, `-1` → cantidad no válida y `cinco` → entrada no válida. [Solución](soluciones/02_plazas.py).

## Ejercicio 3. Lista y función

Escribe una función que reciba una lista de cantidades y devuelva su suma mediante un bucle. Prueba `[2, 3, 1]` → `6` y `[]` → `0`. Después compárala con `sum()`.

Pista: inicializa el acumulador antes del `for` y coloca `return` después del bucle. [Solución](soluciones/03_sumar.py).

## Miniproyecto. Resumen de tres ventas

Una papelería tiene estas ventas **ficticias**, expresadas como lista de diccionarios:

```python
ventas = [
    {"producto": "Cuaderno", "cantidad": 3, "precio": 4.0},
    {"producto": "Bolígrafo", "cantidad": 2, "precio": 1.5},
    {"producto": "Carpeta", "cantidad": 1, "precio": 5.0},
]
```

Construye un programa que:

1. Defina `calcular_importe(cantidad, precio)`.
2. Recorra las ventas y muestre producto e importe con dos decimales.
3. Acumule el total de unidades y el total de euros.
4. Muestre los dos totales.

Salida esperada:

```text
Cuaderno: 12.00 euros
Bolígrafo: 3.00 euros
Carpeta: 5.00 euros
Unidades: 6
Total: 20.00 euros
```

Comprueba también la lista vacía: `0` unidades y `0.00` euros. Cambia la cantidad de cuadernos a `4`: `7` unidades y `24.00` euros. No añadas lectura de ficheros, interfaces o bases de datos todavía.

[Solución comentada](soluciones/04_resumen_ventas.py).

## Criterio de avance

Puedes continuar si puedes guardar y ejecutar el programa, explicar la diferencia entre `print` y `return`, cambiar datos sin copiar otra solución y localizar un error de nombre. Si el miniproyecto resulta demasiado difícil, repite los ejemplos de listas y funciones antes de pasar a Pandas.

[Siguiente: del script al notebook](06-del-script-al-notebook.md) · [Índice](README.md)

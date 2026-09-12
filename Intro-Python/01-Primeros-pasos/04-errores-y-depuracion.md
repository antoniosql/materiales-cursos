# 4. Leer errores y depurar

Equivocarse forma parte de programar. Un mensaje de error aporta información para localizar el problema.

## Leer un traceback

Crea un archivo con este error deliberado y ejecútalo:

```python
cantidad = 3
print(cantida)
```

Python indica el archivo, la línea y un `NameError`, porque `cantida` no tiene valor asignado. Empieza por la última línea del mensaje, localiza la línea de tu archivo y corrige el nombre. El texto exacto y las sugerencias pueden variar según la versión.

| Error | Causa de ejemplo | Primera comprobación |
|---|---|---|
| `SyntaxError` | Paréntesis o comillas sin cerrar | Sintaxis de esa línea y la anterior |
| `IndentationError` | Falta la sangría de un bloque | Espacios después de `if`, `for` o `def` |
| `NameError` | Nombre mal escrito o aún no definido | Nombre y orden de ejecución |
| `TypeError` | Sumar texto y número directamente | Tipos de los operandos |
| `ValueError` | `int("tres")` | Contenido que intentas convertir |
| `ZeroDivisionError` | Dividir por cero | Valor del divisor |

## Tratar una entrada incorrecta

```python
try:
    cantidad = int(input("Cantidad entera: "))
    if cantidad < 0:
        print("La cantidad no puede ser negativa")
    else:
        print(f"Importe: {cantidad * 4} euros")
except ValueError:
    print("Escribe un número entero, por ejemplo 3")
```

Prueba `3`, `-1` y `tres`. La conversión está dentro del `try`, porque es la operación que puede fallar. Capturamos `ValueError`, no cualquier fallo indiscriminadamente. El programa muestra un mensaje y termina: no vuelve a preguntar.

## Detectar un error lógico

```python
cantidad = 3
precio = 4
importe = cantidad + precio
print(importe)
```

No habrá excepción, pero `7` no es el importe esperado (`12`). Corrige la operación y prueba además con cantidad `0` y `1`. Asegurarte de que «no da error» no basta.

## Usar el depurador de VS Code

1. Guarda el ejemplo como `mis-ejercicios/depurar.py`.
2. Haz clic a la izquierda del número de línea de `importe = ...`. Aparecerá un punto de interrupción.
3. Abre **Run > Start Debugging**; también puedes usar F5. Si se solicita, selecciona **Python Debugger > Python File**.
4. Al detenerse, observa `cantidad` y `precio` en **Variables**. La línea resaltada todavía está pendiente de ejecutarse.
5. Pulsa **Step Over / Paso a paso por procedimientos** y observa `importe`.
6. Finaliza la ejecución, cambia `+` por `*`, guarda y repite.

Si no aparece el depurador, comprueba la extensión Python y el componente **Python Debugger**, de Microsoft. Puedes empezar usando `print` para inspeccionar valores; el depurador facilita esa misma observación sin añadir instrucciones al archivo.

Fuentes: [errores de Python](https://docs.python.org/3/tutorial/errors.html) y [depuración en VS Code](https://code.visualstudio.com/docs/python/debugging).

[Siguiente: ejercicios](05-ejercicios.md) · [Índice](README.md)

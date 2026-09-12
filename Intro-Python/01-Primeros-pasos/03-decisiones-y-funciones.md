# 3. Decisiones, repeticiones y funciones

Hasta ahora ejecutábamos instrucciones una tras otra. Ahora elegiremos entre alternativas, repetiremos una operación y le daremos nombre a un cálculo.

## Tomar una decisión

```python
stock = 1
if stock == 0:
    print("Sin existencias")
elif stock < 3:
    print("Hay que reponer")
else:
    print("Stock suficiente")
```

`if` comprueba una condición, `elif` otra si la anterior no se cumple y `else` cubre el resto. Solo se ejecuta una de estas ramas. Los dos puntos abren el bloque y los **cuatro espacios** de sangría indican qué instrucciones pertenecen a él. Utiliza espacios de forma consistente.

Prueba `stock` con `0`, `1` y `5`. Debes obtener, respectivamente, los tres mensajes del ejemplo. El orden importa: si comprobases primero `stock < 3`, también incluirías el caso `0`.

## Guardar y recorrer una lista

```python
cantidades = [2, 3, 1]
print(cantidades[0])
for cantidad in cantidades:
    print(cantidad * 4)
```

Una lista agrupa valores. Los índices empiezan en cero: el primer `print` muestra `2`. El bucle `for` toma cada elemento y ejecuta su bloque. Después veremos `8`, `12` y `4`.

Para acumular un resultado:

```python
cantidades = [2, 3, 1]
total = 0
for cantidad in cantidades:
    total = total + cantidad
print(total)
```

Esperamos `6`. La inicialización va **antes** del bucle. Si colocas `total = 0` dentro, reiniciarás el contador en cada vuelta. Cuando ya entiendas el recorrido puedes usar `sum(cantidades)`.

## Reutilizar con una función

```python
def calcular_importe(cantidad, precio):
    return cantidad * precio

importe = calcular_importe(3, 4)
print(importe)
```

`def` define la función. `cantidad` y `precio` son parámetros; `3` y `4` son los argumentos de esta llamada. `return` devuelve el resultado al lugar de la llamada. Definir la función no ejecuta su cuerpo: hay que llamarla.

`print` muestra un valor; `return` lo entrega para que otro cálculo pueda utilizarlo. Una función que termina sin devolver explícitamente un valor devuelve `None`.

## Dar nombre a los campos de un registro

```python
venta = {"producto": "Cuaderno", "cantidad": 3, "precio": 4}
print(venta["producto"])
print(calcular_importe(venta["cantidad"], venta["precio"]))
```

Ejecuta este fragmento debajo de la definición de `calcular_importe`. Un diccionario asocia claves con valores. Una lista de diccionarios nos permitirá representar varias ventas antes de aprender Pandas.

**Práctica:** escribe una función `necesita_reposicion(stock)` que devuelva `True` si `stock < 3` y `False` en caso contrario. Llámala con `0`, `2` y `3`. Comprueba `True`, `True`, `False`.

Apoyo: [pedidos](ejemplos/04_pedidos.py). Fuentes: [control de flujo](https://docs.python.org/3/tutorial/controlflow.html) y [estructuras de datos](https://docs.python.org/3/tutorial/datastructures.html).

[Siguiente: errores](04-errores-y-depuracion.md) · [Índice](README.md)

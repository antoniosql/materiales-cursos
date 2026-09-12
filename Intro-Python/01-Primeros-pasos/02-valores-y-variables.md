# 2. Valores, variables y entrada del usuario

Crea tus archivos en `mis-ejercicios`. Ejecuta cada ejemplo con **Run Python File in Terminal**, como en la lección anterior.

## Dar nombre a los datos

```python
producto = "Cuaderno"
precio = 4.0
cantidad = 3
hay_stock = True
importe = precio * cantidad
print(producto)
print(importe)
```

`producto` es texto (`str`), `precio` un número con decimales (`float`), `cantidad` un entero (`int`) y `hay_stock` un booleano (`bool`): verdadero o falso. Puedes comprobarlo escribiendo `print(type(precio))`.

Una variable es un nombre asociado a un objeto. `=` asigna un valor; no comprueba una igualdad. La comparación se escribe con `==`. Los nombres distinguen mayúsculas: `precio` y `Precio` son diferentes. Usa nombres descriptivos con guion bajo, como `precio_unitario`.

En Python escribimos decimales con punto: `4.5`. `"4.5"` es texto. Esta distinción importa:

```python
print(3 + 2)
print("3" + "2")
```

Resultados: `5` y `32`. En el segundo caso se concatenan dos textos.

## Mostrar un resultado comprensible

```python
producto = "Cuaderno"
cantidad = 3
precio = 4.0
importe = precio * cantidad
print(f"{cantidad} unidades de {producto}: {importe:.2f} euros")
```

La `f` permite insertar expresiones entre llaves. `:.2f` muestra dos decimales. Esperamos `3 unidades de Cuaderno: 12.00 euros`. Es una práctica de formato con datos ficticios, no una implementación de contabilidad.

## Pedir información

```python
nombre = input("¿Cómo te llamas? ")
print(f"Hola, {nombre}")
```

El programa espera hasta que escribes en la terminal y pulsas Intro. `input()` devuelve texto. Para pedir una cantidad numérica:

```python
cantidad_texto = input("Número de cuadernos: ")
cantidad = int(cantidad_texto)
print(cantidad * 4)
```

Con `3` debe mostrar `12`. Si introduces `tres` o `3.5`, `int()` producirá un error. Aprenderemos a tratarlo en la lección de errores. No confundas que el programa esté esperando una respuesta con que esté bloqueado.

## Comentarios y constantes

```python
# Calculamos el importe de tres cuadernos.
PRECIO_CUADERNO = 4
importe = 3 * PRECIO_CUADERNO
print(importe)
```

`#` inicia un comentario hasta el final de la línea. Escribir un nombre en mayúsculas comunica la intención de tratarlo como constante, pero Python **no impide reasignarlo**. Un texto entre comillas triples es un literal de cadena; no es un tipo especial de comentario.

**Práctica:** crea `entrada.py` que pregunte tu nombre y cuántos cursos has realizado. Muestra una frase con ambos datos. Después muestra cuántos habrás realizado al completar uno más. Si respondes `Ana` y `2`, el segundo número debe ser `3`.

Apoyo: [saludo interactivo](ejemplos/02_saludo.py) y [cálculo sencillo](ejemplos/03_importe.py).

Fuentes: [introducción de Python](https://docs.python.org/3/tutorial/introduction.html), [funciones incorporadas](https://docs.python.org/3/library/functions.html) y [convención de constantes](https://peps.python.org/pep-0008/#constants).

[Siguiente: decisiones y funciones](03-decisiones-y-funciones.md) · [Índice](README.md)

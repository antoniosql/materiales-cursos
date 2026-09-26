# 11 · Cuando algo falla

[Inicio](../README.md) › [Sesión 1](README.md) › Cuando algo falla

**Tiempo aproximado:** 10 minutos

## Equivocarse es parte del trabajo

A estas alturas ya habrás visto algún mensaje de error en rojo. Es posible que te hayas asustado un poco. Vamos a cambiar eso.

Un mensaje de error **no es un suspenso**, es Python explicándote qué no ha entendido y dónde. Todas las personas que programan, incluidas las que llevan veinte años haciéndolo, ven errores **todos los días**. La diferencia es que saben leerlos.

## Cómo leer un mensaje de error

Crea un archivo `error.py` con un error a propósito:

```python
cantidad = 2
print(cantida)
```

Al ejecutarlo, Python muestra algo así:

```text
Traceback (most recent call last):
  File "C:\Users\Ana\Documents\curso-python\error.py", line 2, in <module>
    print(cantida)
          ^^^^^^^
NameError: name 'cantida' is not defined. Did you mean: 'cantidad'?
```

Este mensaje se llama **traceback** y se lee **de abajo arriba**:

| Paso | Dónde mirar | Qué te dice |
|---|---|---|
| 1 | **La última línea** | El **tipo de error** (`NameError`) y una explicación: no existe nada llamado `cantida`. ¡Incluso sugiere `cantidad`! |
| 2 | La línea con **`line 2`** | En **qué línea** de tu archivo está el problema |
| 3 | El código con **`^^^^`** debajo | **Qué parte** exacta de la línea ha causado el error |

> **Idea clave.** Ante un error, **empieza siempre por la última línea**. Ahí está casi toda la información.

## Los errores más frecuentes

| Error | Qué significa | Ejemplo con FraSoHome | Qué revisar |
|---|---|---|---|
| `SyntaxError` | Python no entiende cómo está escrito | `print("Cuadro Atlas)` (falta una comilla) | Comillas, paréntesis y dos puntos de esa línea **y de la anterior** |
| `IndentationError` | La sangría no es correcta | Un `print` sin sangría después de `if stock_cierre == 0:` | Que el bloque esté sangrado 4 espacios |
| `NameError` | Usas un nombre que no existe | `print(cantida)` o `Print("Hola")` | Faltas de ortografía, mayúsculas, o que la variable se cree **antes** de usarla |
| `TypeError` | Operación con tipos que no encajan | `"2" * 31.63` (texto por decimal) | ¿Algún dato es texto cuando debería ser número? ¿Olvidaste `int()` o `float()`? |
| `ValueError` | El tipo es correcto, pero el valor no se puede usar | `float("221,99")` (con coma) o `int("dos")` | Lo que escribió el usuario o lo que venía en los datos |
| `ZeroDivisionError` | División entre cero | `margen / precio_venta` con `precio_venta = 0` | ¿Puede ese divisor ser cero? |
| `IndexError` | Esa posición no existe | `"Madrid"[6]` (un texto de 6 caracteres va de la posición 0 a la 5) | Recuerda: se empieza a contar en 0 |

> **Para curiosos.** El `ValueError` de `float("221,99")` no es un caso raro de laboratorio. Muchos archivos de datos españoles usan coma decimal, y muchos precios llegan con el símbolo `€` pegado. Convertir esos textos en números será una tarea habitual cuando trabajes con datos reales.

## Caza del error

> **Pruébalo (en parejas).** Cada fragmento tiene **un** error. Sin ejecutarlo, intenta decir **qué tipo de error** dará y **por qué**. Después ejecútalo, compruébalo y corrígelo.
>
> **Fragmento A**
>
> ```python
> producto = "Sofá Aurora 160cm"
> if producto == "Sofá Aurora 160cm"
>     print("Es un sofá")
> ```
>
> **Fragmento B**
>
> ```python
> unidades = input("¿Cuántas unidades? ")
> total = unidades * 31.63
> print(total)
> ```
>
> **Fragmento C** (el *Espejo Élite 80cm* tiene de verdad precio de venta 0 en los datos de FraSoHome)
>
> ```python
> precio_venta = 0
> coste_unitario = 150.82
> margen_pct = (precio_venta - coste_unitario) / precio_venta * 100
> print(margen_pct)
> ```

<details markdown>
<summary>Ver soluciones</summary>

**A · `SyntaxError`.** Faltan los **dos puntos** al final de la línea del `if`. Correcto: `if producto == "Sofá Aurora 160cm":`

**B · `TypeError`.** `input` devuelve texto y no se puede multiplicar un texto por un decimal. Correcto: `unidades = int(input("¿Cuántas unidades? "))`

**C · `ZeroDivisionError`.** No se puede dividir entre un precio de 0. Aquí el código no tiene ningún fallo de escritura: el problema está **en el dato**. Un precio de venta de 0 € es casi seguro un error de registro, y lo correcto es comprobarlo antes de calcular:

```python
if precio_venta == 0:
    print("Precio de venta 0: revisa el dato antes de calcular el margen")
else:
    margen_pct = (precio_venta - coste_unitario) / precio_venta * 100
    print(margen_pct)
```

</details>

## Adelantarse a los errores: `try` y `except`

A veces sabes que algo **puede** fallar; por ejemplo, que alguien escriba el precio con coma. En lugar de dejar que el programa se detenga, puedes prepararte:

```python
texto = input("Precio de venta: ")

try:
    precio = float(texto)
    print(f"Precio registrado: {precio:.2f} euros")
except ValueError:
    print("Eso no es un precio válido. Usa punto decimal, por ejemplo 221.99")
```

Léelo así: *"**intenta** (`try`) convertir el texto en número; **si falla** con un `ValueError` (`except`), muestra un mensaje amable en lugar de detenerte"*.

> **Pruébalo.** Ejecuta el código y prueba con `221.99`, con `221,99` y con `mucho`.

## Pedir ayuda a la IA (bien)

Cuando no entiendas un error, una herramienta de IA puede ayudarte **si la usas como profesora**:

| Bien | Mal |
|---|---|
| "Tengo este error en Python: *(pegas el traceback)*. ¿Qué significa y en qué debería fijarme?" | "Arréglame este código" y copiar la respuesta sin leerla |
| "¿Por qué `input` devuelve texto?" | "Hazme el ejercicio de los márgenes" |

Si la IA te da la solución, **no la copies sin más**: asegúrate de entender por qué funciona. El objetivo no es que el programa funcione hoy, sino que tú sepas hacer que funcione mañana.

---

[← Anterior: Tomar decisiones](10-tomar-decisiones.md) · [Índice de la sesión](README.md) · [Siguiente: Resumen y retos →](12-resumen-y-retos.md)

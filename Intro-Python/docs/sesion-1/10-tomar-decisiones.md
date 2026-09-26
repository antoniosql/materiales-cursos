# 10 · Tomar decisiones

[Inicio](../README.md) › [Sesión 1](README.md) › Tomar decisiones

**Tiempo aproximado:** 10 minutos

## La pregunta de Marta

> *"Cada noche el sistema me dice cuántas unidades me quedan de cada producto. Para cada uno tengo un **stock mínimo**: si bajo de ese número, tengo que pedir más. Y si me quedo a cero, es urgente. ¿Puede el programa decirme qué hacer?"*

Hasta ahora nuestros programas hacían siempre lo mismo. Ahora necesitamos que **decidan**: que hagan una cosa u otra según los datos.

## Comparar

Para decidir, primero hay que comparar. Una comparación siempre da como resultado `True` (verdadero) o `False` (falso):

| Pregunta | En Python | Ejemplo | Resultado |
|---|---|---|---|
| ¿Es igual? | `==` | `stock == 0` con `stock = 1` | `False` |
| ¿Es distinto? | `!=` | `tienda != "S001"` con `tienda = "S002"` | `True` |
| ¿Es menor? | `<` | `1 < 3` | `True` |
| ¿Es mayor? | `>` | `1 > 3` | `False` |
| ¿Es menor o igual? | `<=` | `3 <= 3` | `True` |
| ¿Es mayor o igual? | `>=` | `11 >= 5` | `True` |

> **Cuidado.** Un `=` **guarda** un valor. Dos `==` **comparan**. Confundirlos es uno de los errores más frecuentes al empezar.

> **Cuidado.** Con decimales (`float`), evita comparar con `==`. Como viste en el [apartado 8](08-tipos-de-datos-y-variables.md), `0.1 + 0.2 == 0.3` da `False`. Compara redondeando, `round(0.1 + 0.2, 2) == 0.3`, o usa `<` y `>`.

## `if`, `elif` y `else`

```python
producto = "Sofá Boreal Compact"
stock_cierre = 1     # unidades en tienda al cerrar el día
stock_minimo = 3     # por debajo de esto, hay que pedir más

if stock_cierre == 0:
    print(f"{producto}: SIN EXISTENCIAS. Pedido urgente.")
elif stock_cierre < stock_minimo:
    print(f"{producto}: hay que reponer.")
else:
    print(f"{producto}: stock suficiente.")
```

```text
Sofá Boreal Compact: hay que reponer.
```

Léelo en castellano:

- **`if`** (si) el stock es cero → pedido urgente.
- **`elif`** (si no, pero si...) el stock está por debajo del mínimo → reponer.
- **`else`** (en cualquier otro caso) → stock suficiente.

Python comprueba las condiciones **de arriba abajo** y ejecuta **solo el primer bloque** cuya condición sea verdadera. Los demás los salta.

> Los datos no son inventados: la noche del 2 de septiembre de 2025, la tienda de Madrid Centro cerró con **1 Sofá Boreal Compact** y su stock mínimo era **3**.

## La sangría importa

Fíjate en que las líneas con `print` están **desplazadas hacia la derecha** (4 espacios). Esto se llama **sangría** o **indentación**, y en Python no es decorativa: indica qué instrucciones pertenecen a cada bloque.

| Regla | Detalle |
|---|---|
| La línea con `if`, `elif` o `else` termina con **dos puntos** `:` | `if stock_cierre == 0:` |
| Las instrucciones del bloque van **sangradas** | 4 espacios. VS Code los pone solo al pulsar Intro después de `:` |
| El bloque termina cuando **deja de haber sangría** | La siguiente línea sin sangría ya no depende del `if` |

> **Cuidado.** Si olvidas los dos puntos o la sangría, Python mostrará un `SyntaxError` o un `IndentationError`. Es su forma de decir "no entiendo dónde empieza o termina este bloque".

> **Pruébalo.** Crea `stock.py` con el código de arriba y:
>
> 1. **Predice** el resultado con `stock_cierre = 0`, con `stock_cierre = 3` y con `stock_cierre = 11`. Ejecuta y comprueba.
> 2. Cambia el programa para que **pregunte** el stock con `input` (recuerda convertirlo con `int`).

## El orden de las condiciones importa

> **Pruébalo.** Cambia el orden de las dos primeras condiciones:
>
> ```python
> if stock_cierre < stock_minimo:
>     print(f"{producto}: hay que reponer.")
> elif stock_cierre == 0:
>     print(f"{producto}: SIN EXISTENCIAS. Pedido urgente.")
> else:
>     print(f"{producto}: stock suficiente.")
> ```
>
> Ejecútalo con `stock_cierre = 0`. ¿Qué dice? ¿Por qué **nunca** llegará a decir "SIN EXISTENCIAS"?

<details markdown>
<summary>Ver explicación</summary>

Cuando el stock es 0, la primera condición (`0 < 3`) ya es verdadera, así que Python dice "hay que reponer" y **se salta el resto**. La condición `stock_cierre == 0` nunca se llega a comprobar. Por eso los casos más concretos (stock exactamente cero) van **antes** que los más generales (stock por debajo del mínimo).

</details>

## Combinar condiciones: `and` y `or`

A veces una decisión depende de dos cosas a la vez:

```python
importe_pedido = 620.00
es_cliente_fidelizado = True

if importe_pedido >= 500 and es_cliente_fidelizado:
    print("Envío gratis")
else:
    print("Gastos de envío: 9.99 euros")
```

| Palabra | Significa | Es verdadero cuando... |
|---|---|---|
| `and` | y | **Las dos** condiciones son verdaderas |
| `or` | o | **Al menos una** es verdadera |

> **Pruébalo.** Supongamos que la regla de FraSoHome es: *envío gratis si el pedido llega a 500 € **o** si el cliente está fidelizado*. Cambia `and` por `or` y prueba varias combinaciones de importe y fidelización. ¿En qué casos se cobra el envío?

Puedes comparar con el ejemplo [04_stock.py](ejemplos/04_stock.py).

---

[← Anterior: Preguntar y responder](09-preguntar-y-responder.md) · [Índice de la sesión](README.md) · [Siguiente: Cuando algo falla →](11-cuando-algo-falla.md)

# 2 · Qué es programar

[Inicio](../README.md) › [Sesión 1](README.md) › Qué es programar

**Tiempo aproximado:** 15 minutos

## La primera pregunta de Marta

> *"Un cliente se lleva **2 Cuadro Atlas**. Cada uno cuesta **31,63 €**. ¿Cuánto tiene que pagar?"*

Seguramente lo has calculado ya de cabeza o con el móvil: 63,26 €. Pero fíjate en **cómo** lo has hecho, porque ahí está la clave de la programación. Sin darte cuenta, has seguido unos pasos:

1. Saber cuántos cuadros se lleva: **2**.
2. Saber cuánto cuesta cada uno: **31,63 €**.
3. Multiplicar la cantidad por el precio.
4. Decir el resultado.

Esa lista de pasos tiene nombre: es un **algoritmo**.

## Algoritmo: una receta sin ambigüedades

Un **algoritmo** es una secuencia de pasos precisos para resolver un problema. Se parece mucho a una receta de cocina, con una diferencia importante: la persona que sigue la receta tiene sentido común, y el ordenador **no**.

Si una receta dice "añade sal al gusto", tú decides cuánta. Si le das esa instrucción a un ordenador, no sabrá qué hacer. **El ordenador hace exactamente lo que le dices, no lo que quieres decir.**

> **Idea clave.** Programar consiste en escribir algoritmos tan precisos que una máquina sin sentido común pueda seguirlos.

## Del castellano al código

El mismo algoritmo se puede escribir de varias formas. En castellano:

> Guarda que la cantidad es 2. Guarda que el precio es 31,63. Multiplica la cantidad por el precio y guarda el resultado como importe. Muestra el importe.

Y en Python:

```python
cantidad = 2
precio = 31.63
importe = cantidad * precio
print(importe)
```

Resultado:

```text
63.26
```

Aunque nunca hayas visto Python, probablemente intuyes qué hace cada línea:

| Línea | Qué hace |
|---|---|
| `cantidad = 2` | Guarda el número 2 con el nombre `cantidad` |
| `precio = 31.63` | Guarda el número 31,63 con el nombre `precio`. **En Python los decimales se escriben con punto** |
| `importe = cantidad * precio` | Multiplica (`*`) y guarda el resultado con el nombre `importe` |
| `print(importe)` | Muestra en pantalla el valor de `importe` |

No te preocupes todavía por los detalles. Los verás uno a uno durante la sesión.

## Lenguaje de programación

Un **lenguaje de programación** es un idioma con reglas muy estrictas para dar instrucciones a un ordenador. Como cualquier idioma, tiene:

- **Sintaxis:** cómo se escribe. Por ejemplo, en Python los decimales llevan punto y `print` lleva paréntesis.
- **Semántica:** qué significa lo que escribes. Por ejemplo, `*` significa multiplicar.

Un idioma humano tolera errores: si escribes "grasias", te entienden. Un lenguaje de programación **no los tolera**: si escribes `prnt(importe)`, Python no sabe qué es `prnt` y se detiene. Eso no es un fracaso, es una conversación. En el [apartado 11](11-cuando-algo-falla.md) aprenderás a entender lo que Python te dice cuando algo no le cuadra.

## Actividad sin ordenador: el ticket con descuento

> **Pruébalo.**
>
> Marta necesita calcular el importe final de este ticket:
>
> - 2 Cuadro Atlas a 31,63 € cada uno.
> - 1 Sábana Nórdico 140x200 a 103,97 €.
> - Este mes hay un **10 % de descuento** en todo el ticket.
>
> Escribid en papel los pasos, **numerados**, para calcular el total a pagar. Imaginad que se los vais a dar a alguien que obedece al pie de la letra y no tiene ningún sentido común.

Cuando terminéis, intercambiad vuestros pasos con otra pareja y buscad **ambigüedades**. Algunas preguntas para ayudaros:

- ¿Queda claro si el descuento se aplica a cada producto o al total?
- ¿Se dice en algún momento qué hay que hacer con el resultado (mostrarlo, apuntarlo)?
- ¿Qué pasaría si el cliente comprara 0 cuadros? ¿Y 100?
- ¿Se redondea a céntimos? ¿Cuándo?

<details markdown>
<summary>Ver una posible solución</summary>

1. Anota la cantidad de Cuadro Atlas: 2.
2. Anota el precio del Cuadro Atlas: 31,63.
3. Multiplica cantidad por precio y anótalo como "importe cuadros" (63,26).
4. Anota la cantidad de sábanas: 1.
5. Anota el precio de la sábana: 103,97.
6. Multiplica cantidad por precio y anótalo como "importe sábanas" (103,97).
7. Suma "importe cuadros" e "importe sábanas" y anótalo como "subtotal" (167,23).
8. Calcula el 10 % del subtotal: multiplica el subtotal por 0,10 y anótalo como "descuento" (16,723).
9. Resta el descuento al subtotal y anótalo como "total" (150,507).
10. Redondea el total a dos decimales (150,51).
11. Muestra el total al cliente.

Fíjate en cuántos pasos hay para algo que "sabíamos hacer de cabeza". Así piensa un programa.

</details>

> **Idea clave.** La parte difícil de programar no es escribir código: es **pensar los pasos con precisión**. El código es solo la traducción.

---

[← Anterior: Bienvenida a FraSoHome](01-bienvenida-a-frasohome.md) · [Índice de la sesión](README.md) · [Siguiente: Cómo entiende el ordenador un programa →](03-como-entiende-el-ordenador-un-programa.md)

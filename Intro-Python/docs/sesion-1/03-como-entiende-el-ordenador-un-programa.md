# 3 · Cómo entiende el ordenador un programa

[Inicio](../README.md) › [Sesión 1](README.md) › Cómo entiende el ordenador un programa

**Tiempo aproximado:** 20 minutos

## Bajar un nivel

En el apartado anterior escribiste `importe = cantidad * precio` y Python calculó `63.26`. Parece magia, pero no lo es. Antes de instalar nada, vamos a bajar un nivel para entender **qué ocurre por dentro**. No hace falta para escribir tus primeros programas, pero te ayudará a entender por qué Python se comporta como lo hace y por qué algunos errores son como son.

## Las tres piezas de un ordenador que importan aquí

| Pieza | Qué hace | Analogía en la tienda de Marta |
|---|---|---|
| **Procesador (CPU)** | Ejecuta instrucciones muy simples (sumar, comparar, copiar un dato), miles de millones de veces por segundo | El dependiente que atiende, muy rápido pero que solo sabe hacer tareas sencillas |
| **Memoria (RAM)** | Guarda los datos y programas **que se están usando ahora**. Es rápida, pero se borra al apagar | El mostrador: lo que tienes a mano mientras atiendes |
| **Disco (almacenamiento)** | Guarda archivos de forma **permanente**. Es más lento, pero no se borra | El almacén: todo lo que tienes, aunque no lo estés usando |

Cuando ejecutas un programa, sus instrucciones y sus datos pasan del **disco** a la **memoria**, y el **procesador** los va ejecutando uno a uno. Cuando creas una variable en Python, su valor vive en la **memoria**. Por eso, cuando el programa termina, las variables desaparecen: si quieres conservar algo, tienes que **guardarlo en un archivo** en disco.

## Todo son ceros y unos

Por dentro, un ordenador solo entiende dos estados: hay corriente o no hay corriente. Los representamos con **1** y **0**. Cada uno de esos dígitos es un **bit**.

| Unidad | Equivale a | Ejemplo |
|---|---|---|
| **Bit** | Un 0 o un 1 | La respuesta a "¿el producto está activo?" |
| **Byte** | 8 bits | Puede tomar 2⁸ = **256** valores distintos (de 0 a 255) |
| **Kilobyte (KB)** | Unos 1.000 bytes | Un archivo de código pequeño |
| **Megabyte (MB)** | Unos 1.000.000 bytes | Una foto de móvil |
| **Gigabyte (GB)** | Unos 1.000.000.000 bytes | La memoria RAM de un portátil tiene 8, 16 o 32 GB |

Con ceros y unos se puede representar **cualquier cosa**, siempre que acordemos un código:

- **Números.** El número 5 se escribe `101` en binario: 1×4 + 0×2 + 1×1.
- **Textos.** Cada carácter tiene asignado un número en una gran tabla universal llamada **Unicode**: la `A` es el 65, la `ñ` el 241 y el `€` el 8364. Para guardarlos en disco, esos números se convierten en bytes siguiendo una regla llamada **UTF-8**.
- **Imágenes, sonido, vídeo...** También son, al final, muchos números.

> **Idea clave.** Un mismo conjunto de bits puede significar cosas distintas según **cómo se interprete**: un número, una letra, un color... Por eso los lenguajes de programación necesitan saber de qué **tipo** es cada dato. Lo verás en el [apartado 8](08-tipos-de-datos-y-variables.md).

> **Para curiosos.** ¿Te has encontrado alguna vez un texto con caracteres raros como `DecoraciÃ³n` en lugar de `Decoración`? Ocurre cuando un archivo se guardó con una codificación (por ejemplo UTF-8) y se abrió con otra. Es un problema muy común al trabajar con datos de distintos sistemas.

## De tu código a los ceros y unos

El procesador no entiende Python. Solo entiende **código máquina**: instrucciones en binario, muy simples y específicas de cada tipo de procesador. Escribir directamente en código máquina es casi imposible para una persona, así que se inventaron lenguajes cada vez más cercanos a nuestra forma de pensar:

| Nivel | Ejemplo | Cómo se ve "sumar dos números" |
|---|---|---|
| **Código máquina** | Binario | `10110000 01100001 ...` |
| **Bajo nivel** | Ensamblador | `mov eax, 2` / `add eax, 3` |
| **Alto nivel** | C, Java | `int total = 2 + 3;` |
| **Muy alto nivel** | Python | `total = 2 + 3` |

Cuanto más alto es el nivel, más fácil es de leer y escribir para las personas, y más trabajo de "traducción" hay que hacer hasta llegar al código máquina. Esa traducción se puede hacer de dos maneras.

## Compilado frente a interpretado

Imagina que Marta recibe un catálogo de un proveedor escrito en alemán. Tiene dos opciones:

1. **Encargar una traducción completa** a una agencia. Tarda un poco al principio, pero después tiene un catálogo en castellano que puede leer tantas veces como quiera, muy rápido. Si el proveedor cambia algo, hay que volver a traducirlo entero.
2. **Contratar a un intérprete** que le vaya traduciendo en voz alta, frase a frase, mientras lo leen juntos. Puede empezar al momento y, si hay un cambio, el intérprete lo traduce sobre la marcha. A cambio, cada lectura es algo más lenta.

Los lenguajes de programación funcionan igual:

| | **Lenguaje compilado** | **Lenguaje interpretado** |
|---|---|---|
| Cómo funciona | Un programa llamado **compilador** traduce **todo** el código a código máquina **antes** de ejecutarlo. El resultado es un **ejecutable** (por ejemplo, un `.exe`) | Un programa llamado **intérprete** lee el código y lo va ejecutando **sobre la marcha** |
| Ejemplos | C, C++, Rust, Go | Python, R, JavaScript |
| Velocidad | Muy rápido al ejecutarse | Más lento |
| Cuándo detecta errores | Muchos, **al compilar**, antes de ejecutar nada | Al llegar a la línea que falla, **durante la ejecución** |
| Portabilidad | El ejecutable sirve para un sistema concreto (Windows, Mac...) | El mismo código funciona en cualquier sistema que tenga el intérprete |
| Probar cosas rápido | Hay que compilar cada vez | Puedes ejecutar una línea y ver el resultado al instante |

### ¿Y Python exactamente?

Python se suele llamar "lenguaje interpretado", y como primera idea es correcto. Siendo precisos, el intérprete oficial de Python (llamado **CPython**, porque está escrito en C) funciona en dos pasos:

1. **Traduce** tu archivo `.py` a un formato intermedio llamado **bytecode**, más sencillo que Python pero que todavía no es código máquina. Si alguna vez ves una carpeta `__pycache__` con archivos `.pyc`, contiene ese bytecode ya traducido, guardado para ir más rápido la próxima vez.
2. Una **máquina virtual** de Python ejecuta ese bytecode instrucción a instrucción.

Java hace algo parecido: compila a bytecode y lo ejecuta en su propia máquina virtual. Por eso la frontera entre "compilado" e "interpretado" no es tan nítida como parece.

> **Idea clave.** Para ti, hoy, la consecuencia práctica es esta: **Python ejecuta tu programa de arriba abajo y se detiene en la primera línea que no puede ejecutar.** Todo lo anterior a esa línea sí se habrá ejecutado.

### Si Python es "lento", ¿por qué se usa tanto para datos?

Buena pregunta. Porque las herramientas de análisis de datos que se usan desde Python están escritas por dentro en lenguajes compilados como C o Fortran. Python actúa como un **director de orquesta**: tú escribes instrucciones sencillas y legibles, y el trabajo pesado lo hacen piezas compiladas muy rápidas. Tienes lo mejor de los dos mundos: facilidad para escribir y velocidad al ejecutar.

> **Para curiosos.** Las versiones más recientes de CPython incluyen de forma experimental un **compilador JIT** (*just in time*), que traduce a código máquina, mientras el programa se ejecuta, las partes que más se repiten. Es la misma técnica que usan Java y los navegadores con JavaScript.

## Comprueba lo que has entendido

> **Pruébalo.** Responded sin mirar:
>
> 1. Acabas de calcular el margen de un producto en Python y cierras el programa. ¿Dónde estaba guardado el resultado? ¿Sigue ahí?
> 2. ¿Cuántos valores distintos caben en un byte?
> 3. Un compañero dice: "Python es interpretado, así que no se traduce nada". ¿Qué le responderíais?
> 4. Un programa tiene un error en la línea 10. ¿Se ejecutan las líneas 1 a 9?

<details markdown>
<summary>Ver respuestas</summary>

1. En la **memoria RAM**. Al terminar el programa se libera, así que el resultado desaparece salvo que lo hayas guardado en un archivo.
2. **256** (de 0 a 255), porque son 8 bits: 2⁸ = 256.
3. Que CPython sí traduce: convierte el código a **bytecode**, y una máquina virtual lo ejecuta. Lo que no hace es generar un ejecutable en código máquina antes de empezar, como un lenguaje compilado.
4. **Sí**. Python ejecuta de arriba abajo y se detiene al llegar a la línea que falla. (La excepción son los errores de escritura, como un paréntesis sin cerrar: Python los detecta al traducir el archivo, antes de ejecutar nada.)

</details>

---

[← Anterior: Qué es programar](02-que-es-programar.md) · [Índice de la sesión](README.md) · [Siguiente: Las piezas de tu entorno →](04-las-piezas-del-entorno.md)

# 4 · Git y GitHub

[Inicio](../README.md) › [Sesión 2](README.md) › Git y GitHub

**Tiempo aproximado:** 15 minutos

## La pregunta de Marta

> *"Ayer me pasaste el programa del ticket y hoy otra versión. Ahora tengo `ticket.py`, `ticket_v2.py`, `ticket_final.py` y `ticket_final_BUENO.py`. ¿Cuál es el bueno? ¿Qué cambió entre uno y otro?"*

Seguro que te suena: `informe_v3_revisado_def.docx`, adjuntos que van y vienen por correo, cambios que se pierden... Para resolverlo existe el **control de versiones**, y la herramienta más usada del mundo es **Git**.

## Git y GitHub no son lo mismo

| | **Git** | **GitHub** |
|---|---|---|
| Qué es | Un **programa** que instalaste en la sesión 1 | Un **servicio web** (github.com) |
| Para qué sirve | Guardar en tu ordenador el **historial de versiones** de una carpeta | Guardar una **copia** de esa carpeta, con todo su historial, en internet |
| ¿Necesita internet? | No | Sí |

Una analogía: **Git es el historial de versiones de una carpeta**, y **GitHub es la nube** donde guardas esa carpeta para tener una copia de seguridad, trabajar desde otro ordenador o compartirla.

## Cuatro ideas y cuatro acciones

| Idea | Qué es |
|---|---|
| **Repositorio** (repo) | Una carpeta cuyo historial controla Git. Git lo guarda en una subcarpeta oculta llamada `.git` |
| **Commit** | Una **foto** de tus archivos en un momento dado, con un mensaje que explica qué cambió |
| **Local** | El repositorio que está **en tu ordenador**. Aquí trabajas siempre |
| **Remoto** | La copia del repositorio **en GitHub** |

| Acción | Qué hace | Botón en VS Code | Orden en la terminal |
|---|---|---|---|
| **Commit** | Guarda una foto en tu repositorio **local** | **Commit** | `git add .` y `git commit -m "mensaje"` |
| **Push** | **Sube** tus commits del local al remoto | **Sync Changes** o **Publish Branch** | `git push` |
| **Pull** | **Baja** al local los commits nuevos del remoto | **Sync Changes** | `git pull` |
| **Clone** | Descarga un repositorio remoto completo en un ordenador nuevo | **Clone Repository** | `git clone <dirección>` |

> **Idea clave.** Trabajas siempre en **local**: editas, guardas y haces commits en tu ordenador, incluso sin internet. Cuando quieres, sincronizas con el **remoto**: **push** para subir y **pull** para bajar.

## Práctica 1: tu repositorio local

> **Pruébalo.**
>
> 1. Abre tu carpeta `curso-python` en VS Code.
> 2. Pulsa el icono de **Source Control** (Control de código fuente) en la barra de la izquierda: tres círculos unidos por líneas. Atajo: `Ctrl + Shift + G` (`Cmd + Shift + G` en Mac).
> 3. Pulsa **Initialize Repository**. Tu carpeta ya es un repositorio.
> 4. Tus archivos aparecen con una **U** (*Untracked*): Git los ve, pero aún no los guarda.
> 5. Pasa el ratón sobre **Changes** y pulsa **+** para prepararlos todos.
> 6. Escribe un mensaje en la caja de texto: `Programas de la sesión 1 y README`.
> 7. Pulsa **Commit**.

Ahora cambia algo:

> **Pruébalo.** Añade una línea al final de `README.md` y guarda. En Source Control el archivo aparece con una **M** (*Modified*). Haz clic sobre él: VS Code te muestra en verde lo que has añadido. Pulsa **+**, escribe `Amplía el README` y haz **Commit**.

En la terminal, `git log --oneline` te enseña el historial:

```text
22edfb9 Amplía el README
fac7376 Programas de la sesión 1 y README
```

Cada commit tiene un identificador único. Con él se puede volver a ese estado exacto del proyecto cuando se quiera.

> **Cuidado.** Escribe mensajes que expliquen el cambio: `Añade el cálculo del margen`, no `cambios` ni `asdf`. Dentro de un mes, tú serás la persona que los lea.

## Lo que nunca debe subirse: `.gitignore`

Algunos archivos no deben entrar en el historial, sobre todo los que contienen **contraseñas**: lo que entra en un commit queda guardado **para siempre**. Para que Git los ignore, crea en `curso-python` un archivo llamado exactamente **`.gitignore`**:

```text
.venv/
__pycache__/
.env
.DS_Store
```

Haz un commit con el mensaje `Añade .gitignore`. En los próximos apartados verás qué son `.venv` y `.env`, y por qué no deben subirse.

## Práctica 2: el remoto en GitHub (push)

> **Pruébalo.**
>
> 1. En Source Control, pulsa **Publish Branch**.
> 2. La primera vez, VS Code te pedirá **iniciar sesión en GitHub**: se abrirá el navegador, entra con tu cuenta y pulsa **Authorize**. Vuelve a VS Code.
> 3. Elige **repositorio privado** (*private*).
> 4. Cuando termine, pulsa **Open on GitHub**.

Acabas de hacer tu primer **push**: se ha creado el remoto en GitHub con todos tus commits. En el navegador verás tus archivos y, debajo, tu **`README.md` convertido en la portada** del proyecto.

## Práctica 3: traer cambios del remoto (pull)

Vamos a simular que otra persona (o tú desde otro ordenador) cambia algo en el remoto:

> **Pruébalo.**
>
> 1. En GitHub, abre tu `README.md` y pulsa el **lápiz** (*Edit this file*).
> 2. Añade una frase, por ejemplo: `Proyecto revisado por Marta Sánchez.`
> 3. Pulsa **Commit changes...** y confírmalo. Acabas de hacer un commit **en el remoto**.
> 4. Vuelve a VS Code. Tu `README.md` local todavía **no** tiene esa frase.
> 5. En Source Control, pulsa **Sync Changes** (o escribe `git pull` en la terminal).
> 6. Abre `README.md`: la frase ya está en tu ordenador.

## El ciclo de trabajo

A partir de ahora, trabajarás siempre así:

1. **Pull** al empezar, por si hay cambios en el remoto.
2. Editas y guardas tus archivos.
3. **Commit** cada vez que terminas un cambio con sentido.
4. **Push** para subirlo a GitHub.

En VS Code, **Sync Changes** hace el pull y el push de una vez.

> **Para curiosos.** Tus repositorios públicos de GitHub son también tu **portafolio**: muchos equipos de datos miran el GitHub de un candidato además de su CV.

## Comprueba lo que has entendido

> **Pruébalo (en parejas, 2 minutos).**
>
> 1. ¿Cuál es la diferencia entre Git y GitHub?
> 2. Has hecho un commit, pero en GitHub no aparece. ¿Qué te falta?
> 3. Un compañero ha subido cambios al remoto. ¿Cómo los traes a tu ordenador?
> 4. ¿Por qué `.env` está en el `.gitignore`?

<details markdown>
<summary>Ver respuestas</summary>

1. Git es un programa que guarda el historial en tu ordenador. GitHub es un servicio web donde se guarda una copia remota de ese repositorio.
2. Hacer **push** (**Sync Changes** o `git push`). El commit está en tu repositorio local, pero no en el remoto.
3. Con **pull** (**Sync Changes** o `git pull`).
4. Porque contiene contraseñas. Lo que entra en un commit queda en el historial para siempre y, si se sube a GitHub, puede quedar expuesto.

</details>

---

[← Anterior: Markdown](03-markdown.md) · [Índice de la sesión](README.md) · [Siguiente: Paquetes y entornos virtuales →](05-paquetes-y-entornos-virtuales.md)

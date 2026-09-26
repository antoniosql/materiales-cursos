# 5 · Instalación guiada

[Inicio](../README.md) › [Sesión 1](README.md) › Instalación guiada

**Tiempo aproximado:** 35 minutos

## Lo que vamos a hacer

Vamos a instalar las cuatro piezas del apartado anterior, **en este orden**:

1. **Python**, el intérprete.
2. **Visual Studio Code**, el editor.
3. La **extensión Python** para VS Code, que conecta los dos.
4. **Git**, el programa que guarda el historial de tus archivos. No lo usaremos hoy, pero así lo tendrás listo para la sesión 2.

Lo haremos todos a la vez, siguiendo la pantalla del profesor. Si te quedas atrás, **levanta la mano**: nadie sigue hasta que el grupo esté listo.

> **Cuidado.** Descarga siempre desde las **páginas oficiales** que aparecen aquí. Hay webs que imitan a las oficiales para colar programas no deseados.

Elige tu sistema operativo:

- [Instalación en Windows](#windows)
- [Instalación en macOS](#macos)
- [Configurar Git (todos)](#git-config)
- [Si algo falla: plan B](#plan-b)

---

<a id="windows"></a>

## Windows

### Paso 1. Instalar Python

1. Abre la página oficial de descargas para Windows: [python.org/downloads/windows](https://www.python.org/downloads/windows/).
2. Descarga el **Python install manager**. Es el instalador que recomienda python.org desde la versión 3.14.
3. Abre el archivo descargado y pulsa **Install**.
4. Abre **PowerShell**: pulsa la tecla de Windows, escribe `PowerShell` y pulsa Intro. Se abrirá una ventana, normalmente azul o negra, con un texto parecido a `PS C:\Users\TuNombre>`. Es la terminal.
5. Escribe esta orden y pulsa Intro para instalar la versión 3.14 de Python:

   ```powershell
   py install 3.14
   ```

   Si te hace alguna pregunta (por ejemplo, si quieres añadir algo al *PATH*), acepta la opción recomendada escribiendo `y` y pulsando Intro.

6. **Comprueba** que funciona:

   ```powershell
   python --version
   ```

   Debes ver algo como `Python 3.14.2`. El último número puede ser distinto: no importa.

> **Para curiosos.** Si tu ordenador instala Python con el **instalador clásico** (un archivo `.exe` con el nombre de la versión), en la primera pantalla marca la casilla **"Add python.exe to PATH"** antes de pulsar *Install Now*. Si no la marcas, Windows no encontrará Python desde la terminal.

### Paso 2. Instalar Visual Studio Code

1. Abre [code.visualstudio.com/Download](https://code.visualstudio.com/Download).
2. Pulsa el botón grande de **Windows**. Descarga el *User Installer*, que no suele pedir permisos de administrador.
3. Abre el archivo descargado y acepta las opciones por defecto. Si ves la casilla **"Add to PATH"**, déjala marcada.
4. Al terminar, abre **Visual Studio Code** desde el menú Inicio.

### Paso 3. Instalar Git

1. Abre [git-scm.com/downloads/win](https://git-scm.com/downloads/win) y descarga el instalador de **Git for Windows** (*64-bit Git for Windows Setup*).
2. Abre el archivo. El asistente tiene **muchas pantallas**: acepta las opciones por defecto (**Next**) **salvo en dos**:
   - En *Choosing the default editor used by Git*, elige **Use Visual Studio Code as Git's default editor**.
   - En *Adjusting the name of the initial branch in new repositories*, elige **Override the default branch name** y deja escrito `main`.
3. Pulsa **Install** y, al terminar, **Finish**.
4. **Cierra PowerShell, ábrelo de nuevo** y comprueba:

   ```powershell
   git --version
   ```

   Debes ver algo como `git version 2.xx.x.windows.1` (los números pueden variar).

### Paso 4. Instalar la extensión Python

Este paso es igual en Windows y en Mac: sigue en [La extensión Python](#extension).

---

<a id="macos"></a>

## macOS

### Paso 0. Empieza por Git (se instala mientras haces lo demás)

En Mac, Git viene con las **herramientas de línea de comandos para desarrolladores** de Apple. La descarga tarda unos minutos, así que la lanzamos **lo primero** y seguimos con lo demás mientras tanto.

1. Abre la **Terminal**: pulsa `Cmd + Espacio`, escribe `Terminal` y pulsa Intro. Verás un texto parecido a `tunombre@MacBook ~ %`.
2. Escribe:

   ```bash
   git --version
   ```

3. Si ya tienes Git, verás algo como `git version 2.xx.x (Apple Git-xxx)`: pasa al paso 1.
4. Si aparece una ventana que ofrece instalar las **herramientas de línea de comandos** (*command line developer tools*), pulsa **Instalar** y acepta la licencia. **No esperes a que termine**: sigue con el paso 1. Cuando acabe, vuelve a escribir `git --version` para comprobarlo.

### Paso 1. Instalar Python

1. Abre la página oficial de descargas para Mac: [python.org/downloads/macos](https://www.python.org/downloads/macos/).
2. Busca la versión estable más reciente de **Python 3.14** y descarga el **macOS 64-bit universal2 installer** (un archivo `.pkg`). Sirve para cualquier Mac, con chip Apple o Intel.
3. Abre el archivo y sigue el asistente: **Continuar → Instalar**. Te pedirá la contraseña de tu Mac.
4. Al terminar se abrirá una carpeta **Python 3.14**. Haz doble clic en **Install Certificates.command** y espera a que termine. Prepara a Python para descargar cosas de internet de forma segura.
5. Vuelve a la **Terminal**. Si estaba abierta desde el paso 0, ciérrala y ábrela de nuevo.
6. **Comprueba** que funciona:

   ```bash
   python3 --version
   ```

   Debes ver algo como `Python 3.14.2`.

> **Cuidado.** En Mac el comando es **`python3`**, con el 3 al final. Si escribes solo `python`, puede que no funcione o que abra una versión antigua. Cada vez que en estos materiales veas `python`, en tu Mac escribe `python3`.

### Paso 2. Instalar Visual Studio Code

1. Abre [code.visualstudio.com/Download](https://code.visualstudio.com/Download) y descarga la versión para **Mac** (*Universal* sirve para todos).
2. Abre el archivo descargado y arrastra **Visual Studio Code** a la carpeta **Aplicaciones**.
3. Abre VS Code desde Aplicaciones. Si el Mac pregunta si quieres abrir una aplicación descargada de internet, pulsa **Abrir**.

---

<a id="extension"></a>

## La extensión Python (Windows y Mac)

1. En VS Code, pulsa el icono de **Extensiones** en la barra de la izquierda. Son cuatro cuadraditos. También puedes pulsar `Ctrl + Shift + X` (Windows) o `Cmd + Shift + X` (Mac).
2. En el buscador escribe `Python`.
3. Elige la que se llama **Python** y está publicada por **Microsoft**. Suele ser la primera y tiene un icono azul y amarillo con una marca de verificación.
4. Pulsa **Install**.

> **Cuidado.** Aparecerán muchas extensiones con "Python" en el nombre. Instala solo la de **Microsoft**. Las demás no las necesitas.

---

<a id="git-config"></a>

## Configurar Git (Windows y Mac)

Git firma cada cambio que guardas con tu nombre y tu correo, así que hay que decírselos **una sola vez**. En la terminal, escribe estas tres órdenes, cambiando el nombre y el correo por los tuyos. Usa el **mismo correo** con el que creaste tu cuenta de GitHub:

```text
git config --global user.name "Ana García"
git config --global user.email "ana.garcia@ejemplo.com"
git config --global init.defaultBranch main
```

Estas órdenes no muestran nada si todo va bien. Para comprobarlo:

```text
git config --global --list
```

Debes ver tu nombre, tu correo y `init.defaultbranch=main`.

> **Para curiosos.** `--global` significa "para todos mis proyectos de este ordenador". La tercera orden hace que la línea principal de historial de tus proyectos (la *rama* principal) se llame `main`, que es el nombre que usa GitHub.

---

## Comprobación final

Si todo ha ido bien, esto es lo que tienes:

- [ ] En la terminal, `python --version` (Windows) o `python3 --version` (Mac) muestra `Python 3.14.x`.
- [ ] VS Code se abre.
- [ ] En VS Code, la extensión **Python** de Microsoft aparece como instalada.
- [ ] `git --version` muestra una versión y `git config --global --list` muestra tu nombre y tu correo.

Si tienes las cuatro marcas, **enhorabuena: tu ordenador ya está preparado para programar**. La comprobación definitiva será ejecutar tu primer programa en el [apartado 7](07-tu-primer-programa.md).

---

<a id="plan-b"></a>

## Si algo falla: plan B

Las instalaciones fallan a veces, sobre todo en ordenadores de empresa con restricciones. **No es culpa tuya y no te vas a quedar atrás.**

Si a la hora de la comprobación final no lo tienes todo funcionando:

1. Díselo al profesor.
2. Abre el **[entorno en la nube del seminario](https://codespaces.new/antoniosql/materiales-cursos?devcontainer_path=.devcontainer%2Fintro-python%2Fdevcontainer.json)**. Es un espacio de **GitHub Codespaces**: un VS Code completo, con Python y todos los paquetes del seminario ya instalados, que funciona dentro del navegador. Solo necesitas iniciar sesión con tu cuenta de GitHub y pulsar **Create codespace**. La primera vez tarda unos minutos en prepararse.
3. Sigue la clase desde ahí. Todo lo que aprendas es exactamente igual.
4. Durante el descanso o al final de la clase, el profesor te ayudará con la instalación en tu ordenador.

### Problemas frecuentes

Tienes más casos y guías paso a paso en los [anexos](../anexos/README.md).

| Síntoma | Causa probable | Qué hacer |
|---|---|---|
| Windows: `python` no se reconoce como comando | La terminal se abrió antes de terminar la instalación | Cierra PowerShell, ábrelo de nuevo y repite la comprobación |
| Windows: al escribir `python` se abre la Microsoft Store | Windows tiene un "atajo" que apunta a la tienda | Asegúrate de haber completado `py install 3.14` y vuelve a abrir PowerShell |
| Mac: `python3 --version` no muestra 3.14 | La Terminal usa el Python de Apple, que viene con las herramientas de línea de comandos | Cierra la Terminal, ábrela de nuevo y prueba `python3.14 --version`. Si funciona, usa `python3.14` en lugar de `python3` |
| `git` no se reconoce como comando | La terminal se abrió antes de instalar Git | Cierra la terminal (también la de VS Code), ábrela de nuevo y repite |
| Mac: la instalación de las herramientas de línea de comandos tarda mucho | Es una descarga grande | Sigue la clase: Git no se usa hasta la sesión 2 |
| No te deja instalar nada | El ordenador tiene restricciones de la empresa | Plan B y pedir permisos al soporte de tu empresa |

---

[← Anterior: Las piezas de tu entorno](04-las-piezas-del-entorno.md) · [Índice de la sesión](README.md) · [Siguiente: Carpetas y terminal →](06-carpetas-y-terminal.md)

# Instalar Python y Visual Studio Code en macOS

Objetivo: disponer de un intérprete y un editor para el curso. Escribe los comandos en **Terminal**.

## 1. Identificar tu Mac

Abre **menú Apple > Acerca de este Mac**. «Chip Apple M…» indica Apple silicon; «Procesador Intel», un Mac Intel. Anota la versión de macOS y comprueba que las descargas la admiten.

## 2. Descargar e instalar Python

1. Abre [Python para macOS](https://www.python.org/downloads/macos/) y entra en una versión estable de Python 3.14, la rama de referencia de esta guía. Evita alpha, beta o release candidate para empezar.
2. Descarga **macOS 64-bit universal2 installer** (`.pkg`), compatible con Intel y Apple silicon en los macOS indicados en la descarga.
3. Abre el archivo y sigue **Continue > Install**. Introduce credenciales de administrador si el sistema las solicita.
4. En **Aplicaciones > Python 3.14**, abre **Install Certificates.command** y espera a que termine. Prepara los certificados que usa esta distribución para HTTPS.
5. Pulsa **Cmd+Espacio**, escribe `Terminal` y pulsa Intro. Abre una nueva sesión si ya estaba abierta.

```bash
python3.14 --version
python3.14 -c "print('Python funciona')"
python3 --version
```

Los dos primeros comandos deben mostrar `Python 3.14.x` y `Python funciona`. El tercero identifica qué versión abre el nombre general `python3`. Si difiere, utiliza `python3.14` en los siguientes pasos.

No modifiques ni elimines el Python que pueda existir en `/usr/bin`. No necesitas Homebrew, Anaconda ni Xcode para esta ruta de instalación. Si ya tienes un entorno para otros proyectos, identifícalo antes de añadir otra instalación.

Fuentes: [Python en macOS](https://docs.python.org/3/using/mac.html) y [descargas para macOS](https://www.python.org/downloads/macos/).

## 3. Descargar e instalar Visual Studio Code

1. Abre [Download Visual Studio Code](https://code.visualstudio.com/Download).
2. Elige **Apple silicon**, **Intel chip** o **Universal**, según tu Mac y las opciones disponibles.
3. Abre el archivo descargado. Si es `.dmg`, arrastra **Visual Studio Code.app** a **Applications / Aplicaciones**. Si es `.zip`, descomprímelo y mueve la aplicación a Aplicaciones.
4. Abre VS Code desde Aplicaciones y confirma su apertura si macOS pregunta por la aplicación descargada.

### Activar `code` —opcional—

En VS Code, pulsa **Cmd+Shift+P** y ejecuta **Shell Command: Install 'code' command in PATH**. Abre una nueva Terminal y prueba:

```bash
code --version
```

Esto permite abrir la carpeta actual con `code .`. También puedes utilizar **File > Open Folder…** sin configurar este comando.

Fuentes: [VS Code en macOS](https://code.visualstudio.com/docs/setup/mac) y [CLI de VS Code](https://code.visualstudio.com/docs/configure/command-line).

## 4. Instalar el complemento Python

Continúa con [la extensión Python](extension-python.md) y [tu primer programa](../sesion-1/07-tu-primer-programa.md). Git se instala y configura como se explica en la [instalación guiada](../sesion-1/05-instalacion-guiada.md).

**Antes de continuar:** debe funcionar `python3.14 --version` y debes poder abrir VS Code. No se garantiza que instalar la última versión permita ejecutar sin cambios todos los notebooks históricos.

[Volver a los anexos](README.md) · [Guía Windows](instalacion-windows.md)

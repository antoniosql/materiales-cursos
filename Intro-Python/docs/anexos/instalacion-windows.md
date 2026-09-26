# Instalar Python y Visual Studio Code en Windows

Objetivo: comprobar que intérprete y editor funcionan antes de empezar. Escribe los comandos de esta página en **PowerShell**, no dentro de `>>>`.

## 1. Descargar e instalar Python

1. Abre [las descargas oficiales para Windows](https://www.python.org/downloads/windows/).
2. Para una instalación nueva, elige **Python install manager**. Abre el archivo descargado y pulsa **Install**. También puedes acceder a Microsoft Store mediante el enlace de python.org. El gestor descargará después el intérprete.
3. Abre Inicio, busca **PowerShell** y ábrelo. Si estaba abierto durante la instalación, ciérralo y vuelve a abrirlo.
4. Instala la rama estable 3.14 utilizada como referencia en esta guía:

```powershell
pymanager install 3.14
py -3.14 --version
py -3.14 -c "print('Python funciona')"
```

Debes ver `Python 3.14.x` y `Python funciona`. La `x` representa la revisión instalada: no debes escribirla en los comandos. Usamos `pymanager` al instalar para distinguirlo del antiguo lanzador `py`.

Si ya utilizas Python para otros proyectos, revisa primero `py --version` y `py -0p`. Los ejemplos nuevos emplean funciones básicas de Python 3. Las dependencias del bloque de datos se preparan aparte; no se garantiza la compatibilidad automática de todos los notebooks antiguos con la versión más reciente.

### Si utilizas un instalador clásico `.exe`

Si la página ofrece un instalador independiente para la versión elegida, selecciona la arquitectura de tu equipo, marca **Add python.exe to PATH** si aparece y pulsa **Install Now**. Consulta la arquitectura en **Configuración > Sistema > Acerca de > Tipo de sistema**. No elijas el paquete «embeddable» para este curso.

La casilla de PATH pertenece al instalador clásico: **no esperes verla con el install manager**. Comprueba los Windows admitidos en la descarga. Si la organización bloquea la instalación, solicita el paquete a su soporte.

Fuentes: [Python en Windows](https://docs.python.org/3/using/windows.html) y [descargas oficiales](https://www.python.org/downloads/windows/).

## 2. Descargar e instalar Visual Studio Code

1. Abre [Download Visual Studio Code](https://code.visualstudio.com/Download).
2. En Windows selecciona **User Installer**: x64 para Intel/AMD de 64 bits o Arm64 para Windows ARM. El instalador de usuario no requiere normalmente permisos de administrador.
3. Abre `VSCodeUserSetup-...exe` y sigue el asistente. Mantén habilitada la opción de añadir a PATH si se muestra. Puedes activar las opciones de abrir carpetas con Code.
4. Abre **Visual Studio Code** desde Inicio. Es distinto de Visual Studio.
5. Abre una nueva PowerShell y prueba:

```powershell
code --version
```

Verás la versión y otros datos del editor. Si no se reconoce, abre VS Code desde Inicio y consulta [solución de problemas](solucion-de-problemas.md).

Fuentes: [VS Code en Windows](https://code.visualstudio.com/docs/setup/windows) y [CLI de VS Code](https://code.visualstudio.com/docs/configure/command-line).

## 3. Instalar el complemento Python

Sigue [la guía común de la extensión Python](extension-python.md) y después [crea tu primer programa](../sesion-1/07-tu-primer-programa.md). Git se instala y configura como se explica en la [instalación guiada](../sesion-1/05-instalacion-guiada.md).

**Antes de continuar:** debe funcionar `py -3.14 --version` y debes poder abrir VS Code.

[Volver a los anexos](README.md) · [Guía macOS](instalacion-macos.md)

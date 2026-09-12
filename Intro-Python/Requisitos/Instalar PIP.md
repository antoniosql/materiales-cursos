# Qué es pip y cómo comprobarlo

`pip` es el instalador de paquetes de Python. PyPI es un índice de paquetes. Anaconda es una distribución; no es otro nombre para pip. Instalar paquetes y escribir `import` son acciones diferentes.

Las instalaciones oficiales utilizadas en estas guías incluyen normalmente pip. Compruébalo antes de instalar nada.

Windows:

```powershell
py -3.14 -m pip --version
```

macOS:

```bash
python3.14 -m pip --version
```

Si la instalación oficial informa `No module named pip`, prueba su módulo incorporado `ensurepip`:

Windows:

```powershell
py -3.14 -m ensurepip --upgrade
```

macOS:

```bash
python3.14 -m ensurepip --upgrade
```

Después repite la comprobación. En `.venv` utiliza el ejecutable del entorno en lugar del intérprete global. La forma `python -m pip` vincula la operación al Python elegido; un comando `pip` aislado puede apuntar a otra instalación.

La descarga de `get-pip.py` se conserva en el [material histórico](../docs/historico/INDICE.md), pero no es el paso inicial de esta guía. Para instalar paquetes del curso sigue [entornos y paquetes](Entorno-y-paquetes.md).

Fuentes: [instalación de pip](https://pip.pypa.io/en/stable/installation/) y [entornos y paquetes de Python](https://docs.python.org/3/tutorial/venv.html).

[Volver a preparación](README.md)

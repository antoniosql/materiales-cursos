# Funciones: dar nombre a un cálculo para reutilizarlo


def calcular_importe(cantidad, precio):
    """Devuelve cantidad x precio."""
    return cantidad * precio


def aplicar_descuento(importe, descuento_pct):
    """Devuelve el importe después de aplicar un descuento en %."""
    return importe * (1 - descuento_pct / 100)


importe = calcular_importe(2, 31.63)
print(f"2 Cuadro Atlas: {importe:.2f} euros")

con_descuento = aplicar_descuento(importe, 10)
print(f"Con un 10 % de descuento: {con_descuento:.2f} euros")

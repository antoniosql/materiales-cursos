def calcular_importe(cantidad, precio):
    return cantidad * precio


cantidades = [2, 3, 1]
for cantidad in cantidades:
    importe = calcular_importe(cantidad, 4)
    print(f"{cantidad} unidades: {importe:.2f} euros")

stock = 1
if stock == 0:
    print("Sin existencias")
elif stock < 3:
    print("Hay que reponer")
else:
    print("Stock suficiente")

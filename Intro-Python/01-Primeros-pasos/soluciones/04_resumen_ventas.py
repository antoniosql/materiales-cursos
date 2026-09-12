# Datos ficticios y cantidades válidas para practicar los fundamentos.
ventas = [
    {"producto": "Cuaderno", "cantidad": 3, "precio": 4.0},
    {"producto": "Bolígrafo", "cantidad": 2, "precio": 1.5},
    {"producto": "Carpeta", "cantidad": 1, "precio": 5.0},
]


def calcular_importe(cantidad, precio):
    return cantidad * precio


# Inicializamos antes del bucle para no reiniciar los totales en cada vuelta.
total_unidades = 0
total_euros = 0
for venta in ventas:
    importe = calcular_importe(venta["cantidad"], venta["precio"])
    print(f"{venta['producto']}: {importe:.2f} euros")
    total_unidades = total_unidades + venta["cantidad"]
    total_euros = total_euros + importe

print(f"Unidades: {total_unidades}")
print(f"Total: {total_euros:.2f} euros")

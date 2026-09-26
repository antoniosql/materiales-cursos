# Margen de un producto de FraSoHome: Sofá Aurora 160cm (P1000)

producto = "Sofá Aurora 160cm"
precio_venta = 221.99      # euros que paga el cliente
coste_unitario = 143.47    # euros que le cuesta a FraSoHome

margen = precio_venta - coste_unitario
margen_pct = margen / precio_venta * 100

print(producto)
print("Margen en euros:", margen)
print(f"Margen en euros (redondeado): {margen:.2f}")
print(f"Margen sobre el precio: {margen_pct:.1f} %")

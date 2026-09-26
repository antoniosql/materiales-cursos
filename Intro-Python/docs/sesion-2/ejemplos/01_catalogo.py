# Listas, diccionarios y bucles con productos de FraSoHome

# Una lista: varios valores en orden
categorias = ["Muebles", "Decoración", "Iluminación", "Textil hogar"]
print("Primera categoría:", categorias[0])
print("Número de categorías:", len(categorias))

# Un diccionario: una ficha con etiquetas (clave: valor)
producto = {
    "id": "P1001",
    "nombre": "Cuadro Atlas",
    "categoria": "Decoración",
    "precio_venta": 31.63,
}
print("Nombre:", producto["nombre"])
print("Precio:", producto["precio_venta"])

# Un bucle: repetir lo mismo para cada elemento
for categoria in categorias:
    print("- Categoría:", categoria)

# Una lista de diccionarios: ¡esto ya parece una tabla!
catalogo = [
    {"nombre": "Cuadro Atlas", "precio_venta": 31.63},
    {"nombre": "Sábana Nórdico 140x200", "precio_venta": 103.97},
    {"nombre": "Sofá Aurora 160cm", "precio_venta": 221.99},
]
for p in catalogo:
    if p["precio_venta"] > 100:
        print(f"{p['nombre']}: {p['precio_venta']:.2f} euros (más de 100)")
    else:
        print(f"{p['nombre']}: {p['precio_venta']:.2f} euros")

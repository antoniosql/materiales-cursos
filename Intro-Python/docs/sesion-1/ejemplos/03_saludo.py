# Pedir datos a la persona que usa el programa

nombre = input("¿Cómo te llamas? ")
tienda = input("¿En qué tienda de FraSoHome compras? ")

print(f"Hola, {nombre}. Te esperamos en FraSoHome {tienda}.")

# input() siempre devuelve texto. Para calcular, hay que convertirlo.
unidades = int(input("¿Cuántos Cuadro Atlas quieres? "))
precio = 31.63
print(f"Total: {unidades * precio:.2f} euros")

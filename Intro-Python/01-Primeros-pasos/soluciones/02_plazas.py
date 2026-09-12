CAPACIDAD = 12
try:
    asistentes = int(input("Número de asistentes: "))
    if asistentes < 0:
        print("La cantidad no puede ser negativa")
    elif asistentes > CAPACIDAD:
        print("No hay capacidad suficiente")
    else:
        print(f"Plazas disponibles: {CAPACIDAD - asistentes}")
except ValueError:
    print("Escribe un número entero, por ejemplo 5")

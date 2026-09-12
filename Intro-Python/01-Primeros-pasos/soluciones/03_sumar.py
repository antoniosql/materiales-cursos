def sumar_cantidades(cantidades):
    total = 0
    for cantidad in cantidades:
        total = total + cantidad
    return total


print(sumar_cantidades([2, 3, 1]))
print(sumar_cantidades([]))

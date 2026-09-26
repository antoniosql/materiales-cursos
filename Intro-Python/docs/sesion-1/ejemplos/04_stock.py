# ¿Hay que reponer? Datos reales del stock de Madrid Centro (S001)

producto = "Sofá Boreal Compact"
stock_cierre = 1     # unidades en tienda al cerrar el día
stock_minimo = 3     # por debajo de esto, hay que pedir más

if stock_cierre == 0:
    print(f"{producto}: SIN EXISTENCIAS. Pedido urgente.")
elif stock_cierre < stock_minimo:
    print(f"{producto}: hay que reponer.")
else:
    print(f"{producto}: stock suficiente.")

#  Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana.

ventas = [
    [5, 7, 3, 4, 6, 8, 2],   # Producto 1
    [2, 4, 6, 3, 5, 7, 9],   # Producto 2
    [8, 6, 5, 7, 4, 3, 6],   # Producto 3
    [1, 3, 2, 5, 4, 9, 7]    # Producto 4
]

mayores_ventas_semana = 0

print("=== TOTAL VENTAS ===")
for prod in range(len(ventas)):
    total_vendido_producto = 0
    for dia in range(len(ventas[prod])):
        total_vendido_producto += ventas[prod][dia]
    print(f"Producto {prod+1}: {total_vendido_producto}")
    if total_vendido_producto > mayores_ventas_semana:
        mayores_ventas_semana = total_vendido_producto
        indice_mas_vendido = prod

print(f"Producto mas vendido de la semana: {indice_mas_vendido + 1}")

mayores_ventas = 0
for dia in range(7):
    total_vendido_dia= 0
    for prod in range(len(ventas)):
        total_vendido_dia += ventas[prod][dia]
    if total_vendido_dia > mayores_ventas:
        mayores_ventas = total_vendido_dia
        indice_mejor_dia = dia

mejor_dia = "Mejor día de ventas: "
if indice_mejor_dia == 0:
    print(mejor_dia + "Lunes")
elif indice_mejor_dia == 1:
    print(mejor_dia + "Martes")
elif indice_mejor_dia == 2:
    print(mejor_dia + "Miércoles")
elif indice_mejor_dia == 3:
    print(mejor_dia + "Jueves")
elif indice_mejor_dia == 4:
    print(mejor_dia + "Viernes")
elif indice_mejor_dia == 5:
    print(mejor_dia + "Sábado")
else:
    print(mejor_dia + "Domingo")



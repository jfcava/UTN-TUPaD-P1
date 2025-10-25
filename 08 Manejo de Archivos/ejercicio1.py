# 1. Crear archivo inicial con productos: Crear un archivo de texto llamado
# productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad

productos = [
    "Pantalon,80000,25",
    "Campera,250000,10",
    "Remera,250000,80"
]

with open("productos.txt", "w") as archivo:
    for linea in productos:
        archivo.write(f"{linea}\n")

# Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
# línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
# formato: Producto: Lapicera | Precio: $120.5 | Cantidad: 30

with open("productos.txt", "r") as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        lista = linea.strip().split(",")
        print(lista)

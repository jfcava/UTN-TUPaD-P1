# Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
#   • Consultar el stock de un producto ingresado.
#   • Agregar unidades al stock si el producto ya existe.
#   • Agregar un nuevo producto si no existe.

import os

#Funcion para limpiar consola
def limpiar():
    os.system("cls")

#Funcion para mostrar menu
def mostrar_menu():
    for opcion in menu:
        print(opcion)

menu = ["\n=== STOCK DE PRODUCTOS ===",
        "1. Consultar Stock",
        "2. Agregar unidades",
        "3. Agregar nuevo producto",
        "4. Salir"]

#Stock inicial de productos
stock_productos = {
    "Leche": 15,
    "Pan": 32,
    "Arroz": 20,
    "Fideos": 45,
    "Aceite": 10
}

mostrar_menu()
print()

opcion = input("Ingrese una opcion: ")

while opcion not in "1234":
    print("Opcion incorrecta. Vuelva a intentarlo.")
    mostrar_menu()
    opcion = input("Ingrese una opcion: ")
    
match int(opcion):
    case 1:
        print("\n--- Consultar Stock")
        busqueda = input("Ingrese el producto a buscar: ")
        if busqueda in stock_productos:
            print(f"\nProducto: {busqueda}")
            print(f"Stock: {stock_productos[busqueda]}")
        else:
            print("Producto no encontrado.")
    case 2:
        print("\n--- Agregar unidades al stock")
        producto = input("Ingrese el producto: ")
        while producto not in stock_productos:
            print("Producto inexistente. Volve a intentarlo.")
            producto = input("\nIngrese el producto: ")
        unidades_agregadas = input("Cantidad de unidades a agregar: ")
        while not unidades_agregadas.isdigit():
            print("Solo se aceptan números positivos. Volvé a intentarlo.")
            unidades_agregadas = input("Cantidad de unidades a agregar: ")
        stock_productos[producto] += int(unidades_agregadas)
        print(f"\nUnidades disponibles de {producto}: {stock_productos[producto]}")
    case 3:
        print("\n--- Agregar nuevo producto")
        nuevo_producto = input("Ingrese el nombre del nuevo producto: ")
        while nuevo_producto in stock_productos:
            print("El producto ya se encuentra ingresado. Volve a intentarlo.")
            nuevo_producto = input("\nIngrese el nombre del nuevo producto: ")
        unidades = input("Ingrese la cantidad de unidades: ")
        while not unidades.isdigit():
            print("Solo se aceptan números positivos. Volvé a intentarlo.")
            unidades = input("Ingrese la cantidad de unidades: ")
        stock_productos[nuevo_producto] = int(unidades)
        print("Producto agregado exitosamente.")
        print(stock_productos)
    case 4:
        print("\nPrograma terminado. Hasta la próxima!")




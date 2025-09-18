# 2) Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.

# Inicializo variable
productos = []

print("Ingrese 5 productos a la lista")
for x in range(5):
    productos.append(input(f"Producto {x + 1}: ")) # Solicito ingreso de productos y cargo la lista

lista_ordenada = sorted(productos) # Ordeno la lista alfabeticamente

# Imprimo la lista en pantalla
print("=== Tu lista de productos ===")
for x in range(len(lista_ordenada)):
    print(f"{x + 1}.{lista_ordenada[x]}")

print("Cual producto queres eliminar? (Ingresa su numero - 0 para terminar)")
opc = int(input()) - 1

# Mientras la opcion sea distinta de -1 (0 que cargue el usuario) elimino el producto que selecciono,
# o imprimo mensaje.
while opc != -1:
    if opc <= 4:
        lista_ordenada.pop(opc)
        print("LISTA ACTUALIZADA:")
        for x in range(len(lista_ordenada)):
            print(f"{x + 1}.{lista_ordenada[x]}")
    else:
        print("El producto que queres eliminar no existe")
    
    print("Cual producto queres eliminar? (Ingresa su numero - 0 para terminar)")
    opc = int(input()) - 1

print("Programa terminado")

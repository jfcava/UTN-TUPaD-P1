# 2) Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.

productos = []

print("Ingrese 5 productos a la lista")
for x in range(5):
    productos.append(input(f"Producto {x + 1}: "))

lista_ordenada = sorted(productos)

print("=== Tu lista de productos ===")
for x in range(len(lista_ordenada)):
    print(f"{x + 1}.{lista_ordenada[x]}")

print("Cual producto queres eliminar? (Ingresa su numero)")
lista_ordenada.pop(int(input()) - 1)
print("LISTA ACTUALIZADA:")
for x in range(len(lista_ordenada)):
    print(f"{x + 1}.{lista_ordenada[x]}")


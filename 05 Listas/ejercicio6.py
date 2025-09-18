# Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
# último pasa a ser el primero).

# Inicializo la lista
numeros = [3, 5, 8, 9, 1, 2, 6]
print("=== LISTA ORIGINAL ===")
print(numeros)

# Guardo el primer elemento de la lista
aux = numeros[0] 
# Guardo el ultimo elemento de la lista
ultimo = numeros[-1]

# Recorro la lista desde el segundo elemento, guardo en variable temporal e intercambio valores
for x in range(1, len(numeros)):
    temp = numeros[x]   
    numeros[x] = aux    
    aux = temp  

# El ultimo valor de la lista, lo coloco en la primera posicion
numeros[0] = ultimo

print("\n=== LISTA ROTADA HACIA LA DERECHA ===")
print(numeros)
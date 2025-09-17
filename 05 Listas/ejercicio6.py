# Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
# último pasa a ser el primero).

numeros = [3, 5, 8, 9, 1, 2, 6]
aux = numeros[0] # guardo el 3
ultimo = numeros[-1]
print("ultimo:",ultimo)

for x in range(1, len(numeros)):
    temp = numeros[x]   
    numeros[x] = aux    
    aux = temp  

numeros[0] = ultimo

print(numeros)
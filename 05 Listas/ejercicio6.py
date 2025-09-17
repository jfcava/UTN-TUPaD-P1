# Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
# último pasa a ser el primero).

numeros = [3, 5, 8, 9, 1, 2, 6]
aux = numeros[0] # guardo el 3

for x in range(1, len(numeros)):
    temp = numeros[x]   
    numeros[x] = aux    
    aux = temp  

print(numeros)
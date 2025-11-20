# Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛
# 𝑚 = 𝑛 ∗ 𝑛(𝑚−1)
# . Prueba esta función en un algoritmo general.

def potencia(n, m):
    if m == 0:
        return 1
    else:
        return n * potencia(n, m - 1)
    
numero = int(input("Ingrese un numero: "))
potencia_seleccionada = int(input("Ingrese la potencia: "))

if potencia_seleccionada < 0:
    print("Solo se aceptan exponentes enteros no negativos.")
else:
    print(potencia(numero, potencia_seleccionada))

    


# Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

print("===== SUMÁ NUMEROS! =====")

print("Ingrese un número:")
num = int(input())
suma = 0

while num != 0:
    suma += num
    print("Ingrese un número:")
    num = int(input()) 
    
print("Resultado:", suma)

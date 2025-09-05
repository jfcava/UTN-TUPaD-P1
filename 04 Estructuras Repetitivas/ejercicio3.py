# Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

print("=================================================")
print("====== CALCULADORA DE NÚMEROS COMPRENDIDOS ======")
print("=================================================")

num1 = int(input("Ingrese el primer valor del rango:"))
num2 = int(input("Ingrese el segundo valor del rango:"))

if num2 < num1:
    aux = num2
    num2 = num1
    num1 = aux

suma = 0

for x in range(num1 + 1, num2):
    suma += x

print(f"La suma de los números comprendidos entre {num1} y {num2} es: {suma}")

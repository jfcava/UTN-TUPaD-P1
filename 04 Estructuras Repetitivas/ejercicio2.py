# Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

num = int(input("Ingrese un numero: "))
cant_digitos = 0

if num < 0:
    num = -num

while num > 0:
    num = num // 10
    cant_digitos += 1

print("El numero ingresado tiene",cant_digitos, "digitos.")

# Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

print("==============================")
print("=== CALCULADORA DE DÍGITOS ===")
print("==============================")

num = int(input("Ingrese un número: "))
cant_digitos = 0

if num < 0: # Cambio de signo en caso que sea negativo
    num = -num

while num > 0: # Division entera por 10 y cuento digitos
    num = num // 10
    cant_digitos += 1

print("Cantidad de dígitos:",cant_digitos)

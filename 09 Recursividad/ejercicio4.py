# Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.


def decimal_binario(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return decimal_binario(n//2) + str(n % 2)

num_decimal = int(input("Ingrese un numero: "))

if num_decimal < 0:
    print("Solo se aceptan números enteros positivos.")
else:
    print(decimal_binario(num_decimal))


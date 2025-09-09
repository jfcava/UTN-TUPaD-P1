# Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

print("================================")
print("=== CLASIFICACIÓN DE NÚMEROS ===")
print("================================")

# Inicializo variables en 0, y constante para la cantidad de intentos.
CANT_NUMEROS = 100
pares = 0
impares = 0
negativos = 0
positivos = 0

# Recorro desde 1 hasta la cantidad de numeros + 1 y evaluo.
for x in range(1, CANT_NUMEROS + 1):
    num = int(input(f"Ingrese el número {x}:"))
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")


# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

CANT_NUMEROS = 5
suma = 0

for x in range(CANT_NUMEROS):
    num = int(input("Ingresá un número:"))
    suma += num

print(f"La media de los valores ingresados es: {suma/CANT_NUMEROS}")
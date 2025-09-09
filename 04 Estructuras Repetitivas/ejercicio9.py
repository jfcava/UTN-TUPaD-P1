# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

print("========================")
print("=== CALCULO DE MEDIA ===")
print("========================")

# Inicializo la constante de CANT_NUMEROS y la suma en 0
CANT_NUMEROS = 100
suma = 0

# Pido numeros hasta la cantidad establecida y realizo la sumatoria.
for x in range(CANT_NUMEROS):
    num = int(input("Ingresá un número:"))
    suma += num

print(f"La media de los valores ingresados es: {suma/CANT_NUMEROS}")
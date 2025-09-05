# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

num = int(input("Ingrese un número: "))

while num > 0:
    suma = 0
    for x in range(num + 1):
        suma += x
    print("Resultado:", suma)
    num = int(input("Ingrese otro número: "))
else:
    print("Debes ingresar un número positivo")
# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

print("================================")
print("=== SUMA ENTRE 0 Y UN NUMERO ===")
print("================================")

num = int(input("Ingrese un número: "))

# Mientras el numero ingresado sea positivo, sumo los numeros comprendidos entre 0
# y el numero ingresado. Sino imprimo mensaje de ingresar un numero positivo.
while num > 0:
    suma = 0
    for x in range(1, num):
        suma += x
    print("Resultado:", suma)
    num = int(input("Ingrese otro número: "))
else:
    print("Debes ingresar un número positivo")
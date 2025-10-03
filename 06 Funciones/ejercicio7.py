# Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros 
# y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
# Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    return [a+b, a-b, a*b, round(a/b,2)]

print("=== OPERACIONES BÁSICAS ===")
num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))

operaciones = operaciones_basicas(num1, num2)
print()
print(f"=== RESULTADOS ===")
print(f"Suma: {operaciones[0]}")
print(f"Resta: {operaciones[1]}")
print(f"Multiplicación: {operaciones[2]}")
print(f"División: {operaciones[3]}")
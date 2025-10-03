# Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros 
# y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a, b, c):
    return round(((a + b + c) / 3), 2)

print("=== CALCULAR PROMEDIO DE TRES NÚMEROS ===")
num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))
num3 = float(input("Número 3: "))
print(f"Promedio: {calcular_promedio(num1, num2, num3)}")
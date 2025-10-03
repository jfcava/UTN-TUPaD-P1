# Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos 
# y la altura en metros, y devuelva el índice de masa corporal (IMC). 
# Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.


def calcular_imc(peso, altura):
    return round(peso / (altura ** 2), 2)

print("=== CALCULADORA IMC ===")
peso = float(input("Ingresá tu peso: "))
while peso < 0:
    print("No se aceptan números negativos.")
    peso = float(input("Ingresá tu peso: "))

altura = float(input("Ingresá tu altura: "))
while altura < 0:
    print("No se aceptan números negativos.")
    altura = float(input("Ingresá tu altura: "))

print()
print(f"IMC: {calcular_imc(peso, altura)}")





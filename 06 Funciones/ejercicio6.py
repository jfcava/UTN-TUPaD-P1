# Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range (1, 11):
        print(f"{numero} X {i} = {numero * i} ")

print("=== TABLA DE MULTIPLICAR ===")
num = input("Ingresá un número: ")

while not num.isdigit():
    print("Solo se acepta un número positivo.")
    num = input("Ingresá un número: ")

print()
print(f"TABLA DE MULTIPLICAR DEL NÚMERO {num}")
print()
tabla_multiplicar(int(num))
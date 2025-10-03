# Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro 
# y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro 
# y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

import math

def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

print("=== CALCULOS DE UN CIRCULO ===")
radio = input("Radio: ")

while not radio.isdigit():
    print("Solo se aceptan números positivos.")
    radio = input("Radio: ")

print(f"Área del círculo: {round(calcular_area_circulo(float(radio)), 2)}")
print(f"Perímetro del círculo: {round(calcular_perimetro_circulo(float(radio)), 2)}")

# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

# Genero numero aleatorio entre 0 y 9
aleatorio = random.randint(0,9)
cant_intentos = 0

print("==========================")
print("=== ADIVINÁ EL NÚMERO! ===")
print("==========================")

# Pido un numero y sumo 1 intento
num = int(input("Probá con un número: "))
cant_intentos += 1

# Mientras el numero ingresado no sea igual, vuelvo a pedir otro numero,
# sumo un intento, sino imprimo mensaje de Ganador
while num != aleatorio:
    print("No adivinaste :( \nVolvé a intentarlo!")
    cant_intentos += 1
    num = int(input("Probá con otro número: "))
else:
    print(f"Ganaste! Acertaste el número en {cant_intentos} intentos.")
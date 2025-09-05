# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

aleatorio = random.randint(0,9)
intentos = 0

print("=== ADIVINÁ EL NÚMERO! ===")

num = int(input("Probá con un número: "))
intentos += 1

while num != aleatorio:
    print("No adivinaste :( \nVolvé a intentarlo!")
    intentos += 1
    num = int(input("Probá con otro número: "))
else:
    print(f"Ganaste! Acertaste el número en {intentos} intentos.")
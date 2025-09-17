# 3) Generar una lista con 15 números enteros al azar entre 1 y 100.
# • Crear una lista con los pares y otra con los impares.
# • Mostrar cuántos números tiene cada lista.

import random

lista = []

for x in range(15):
    lista.append(random.randint(1,100))

pares = []
impares = []

for x in range(len(lista)):
    if lista[x] % 2 == 0:
        pares.append(lista[x])
    else:
        impares.append(lista[x])

print(lista)
print(f"lista pares: {pares}")
print(f"lista impares: {impares}")
print(f"Lista de pares: {len(pares)}")
print(f"Lista de impares: {len(impares)}")
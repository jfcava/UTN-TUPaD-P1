# 3) Generar una lista con 15 números enteros al azar entre 1 y 100.
# • Crear una lista con los pares y otra con los impares.
# • Mostrar cuántos números tiene cada lista.

import random

# Inicializo listas vacias
lista = []
pares = []
impares = []

# Genero 15 numeros al azar en la lista
for x in range(15):
    lista.append(random.randint(1,100))

# Recorro la lista y comparo para obtener pares e impares y cargar cada lista
for x in range(len(lista)):
    if lista[x] % 2 == 0:
        pares.append(lista[x])
    else:
        impares.append(lista[x])

# Imprimo resultados
print("=== LISTA DE NÚMEROS AL AZAR ===")
print(lista)

print(f"\nLista de números pares: {pares}")
print(f"Cantidad de pares: {len(pares)}\n")
print(f"Lista de números impares: {impares}")
print(f"Cantidad de impares: {len(impares)}")
# 1) Crear una lista con las notas de 10 estudiantes.
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota más alta y la más baja.

import math

# Inicializo variables
notas = [2, 4, 9, 10, 8, 5, 6, 7, 9, 8]
cant_notas = len(notas)
sumatoria = 0
nota_mas_alta = float("-inf")
nota_mas_baja = math.inf

print("=== LISTA DE NOTAS ===")
for x in range(cant_notas):
    print(f"Nota {x + 1}: {notas[x]}") # Muestro cada nota
    sumatoria += notas[x] # Realizo sumatoria de cada nota
    if notas[x] > nota_mas_alta:
        nota_mas_alta = notas[x] # Obtengo la nota mas alta
    if notas[x] < nota_mas_baja:
        nota_mas_baja = notas[x] # Obtengo la nota mas baja

promedio = sumatoria / cant_notas # Calculo promedio

# Imprimo resultados
print("======================")
print(f"Promedio de notas: {promedio}")
print(f"Nota mas alta: {nota_mas_alta}")
print(f"Nota mas baja: {nota_mas_baja}")




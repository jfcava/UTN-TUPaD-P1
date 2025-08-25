# EJERCICIO 6

# Escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma:

import random
from statistics import mode, median, mean

# Creo la lista de numeros aleatorios
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcula la moda, mediana y media de la los numeros en la lista
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

# Comparo para mostrar el resultado
if media > mediana and mediana > moda:
    print("Sesgo positivo")
elif media < mediana and mediana < moda:
    print("Sesgo negativo")
elif moda == mediana and moda == media:
    print("Sin sesgo")

print("Programa terminado.")


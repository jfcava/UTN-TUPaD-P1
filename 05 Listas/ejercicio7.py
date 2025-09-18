# Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
# • Calcular el promedio de las mínimas y el de las máximas.
# • Mostrar en qué día se registró la mayor amplitud térmica.

# Inicializo las variables
temperaturas = [
    [8, 12],
    [9, 13],
    [10, 19],
    [7, 15],
    [5, 13],
    [8, 15],
    [9, 20]
]

sum_minimas = 0
sum_maximas = 0
max_amplitud = 0
indice_mayor_amplitud = 0
dia_mayor_amplitud = ""

# Recorro la matriz
for x in range(len(temperaturas)):
    sum_minimas += temperaturas[x][0] # Sumatoria de minimas
    sum_maximas += temperaturas[x][1] # Sumatoria de maximas
    amplitud = temperaturas[x][1] - temperaturas[x][0] # Calculo la amplitud de cada dia
    if amplitud > max_amplitud: # Obtengo la maxima amplitud y guardo el indice
        max_amplitud = amplitud
        indice_mayor_amplitud = x

# Comparo el indice para mostrar el dia de la maxima amplitud
if indice_mayor_amplitud == 0:
    dia_mayor_amplitud = "Lunes"
elif indice_mayor_amplitud == 1:
    dia_mayor_amplitud = "Martes"
elif indice_mayor_amplitud == 2:
    dia_mayor_amplitud = "Miercoles"
elif indice_mayor_amplitud == 3:
    dia_mayor_amplitud = "Jueves"
elif indice_mayor_amplitud == 4:
    dia_mayor_amplitud = "Viernes"
elif indice_mayor_amplitud == 5:
    dia_mayor_amplitud = "Sabado"
elif indice_mayor_amplitud == 6:
    dia_mayor_amplitud = "Domingo"

# Imprimo en pantalla
print("============================")
print(f"Promedio Mínimas: {round(sum_minimas / len(temperaturas), 2)}")
print("============================")
print(f"Promedio Máximas: {round(sum_maximas / len(temperaturas), 2)}")
print("============================")
print(f"Mayor amplitud térmica: {dia_mayor_amplitud}")
print("============================")

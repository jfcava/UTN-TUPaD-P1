# Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia.

notas = [
    [7, 8, 6],  # Estudiante 1
    [5, 9, 7],  # Estudiante 2
    [8, 6, 10], # Estudiante 3
    [4, 7, 5],  # Estudiante 4
    [9, 8, 9]   # Estudiante 5
]

sum_materia1 = 0
sum_materia2 = 0
sum_materia3 = 0

print("=== PROMEDIOS ESTUDIANTES ===")

for x in range(len(notas)):
    suma = 0
    for y in range(len(notas[x])):
        suma += (notas[x][y])
        if y == 0:
            sum_materia1 += notas[x][y]
        elif y == 1:
            sum_materia2 += notas[x][y]
        else:
            sum_materia3 += notas[x][y]

    print(f"Promedio Estudiante {x + 1}: {round(suma/3,2)}")

print("\n=== PROMEDIO MATERIAS ===")
print(f"Promedio materia 1: {round(sum_materia1/len(notas), 2)}")
print(f"Promedio materia 2: {round(sum_materia2/len(notas), 2)}")
print(f"Promedio materia 3: {round(sum_materia3/len(notas), 2)}")


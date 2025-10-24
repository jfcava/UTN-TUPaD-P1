# Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

print("=== PROMEDIO ALUMNOS ===")

alumnos = {}

#Carga de 3 alumnos
for alumno in range(3):
    nombre = input(f"Alumno {alumno + 1} - Nombre: ")
    
    notas = []
    # Se carga la lista con 3 notas, y luego se transforma a tupla
    for i in range(3):
        nota = float(input(f"Nota {i + 1}: "))
        notas.append(nota)

    alumnos[nombre] = tuple(notas)
    
print("\n=== PROMEDIOS ===")

# Se recorre el diccionario y se calcula promedio de cada uno
for nombre, notas in alumnos.items():
    total = 0
    for nota in notas:
        total += nota
    promedio = total / len(notas)
    print(f"Promedio Alumno {nombre}: {round(promedio,2)}") 

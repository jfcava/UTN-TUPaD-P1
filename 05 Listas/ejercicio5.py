# Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.

estudiantes = ["Lucía", "Martín", "Camila", "Julián", "Sofía", "Mateo", "Valentina", "Tomás"]

print("=== LISTA DE ESTUDIANTES ===")
for x in range(len(estudiantes)):
    print(f"{x + 1}.{estudiantes[x]}")

print("=== MENU DE OPCIONES ===")
print("1. Agregar un estudiante")
print("2. Eliminar un estudiante")
print("3. Salir")
respuesta = int(input("Opcion: "))

while respuesta != 3:
    if respuesta == 1:
        estudiantes.append(input("Ingrese el nombre del estudiante a agregar: "))
        print("=== LISTA DE ESTUDIANTES ===")
        for x in range(len(estudiantes)):
            print(f"{x + 1}.{estudiantes[x]}")
    elif respuesta == 2:
        estudiante_a_remover = (input("Ingrese el nombre del estudiante a eliminar: "))
        if estudiante_a_remover not in estudiantes:
            print("El nombre ingresado no se encuentra en la lista")
        else:
            estudiantes.remove(estudiante_a_remover)
            print("=== LISTA DE ESTUDIANTES ===")
            for x in range(len(estudiantes)):
                print(f"{x + 1}.{estudiantes[x]}")
    else:
        print("Opcion incorrecta, vuelva a ejecutar el programa")
    
    print("=== MENU DE OPCIONES ===")
    print("1. Agregar un estudiante")
    print("2. Eliminar un estudiante")
    print("3. Salir")
    respuesta = int(input("Opcion: "))


# Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.

# Inicializo variable
estudiantes = ["Lucía", "Martín", "Camila", "Julián", "Sofía", "Mateo", "Valentina", "Tomás"]

# Imprimo la lista en pantalla
print("=== LISTA DE ESTUDIANTES ===")
for x in range(len(estudiantes)):
    print(f"{x + 1}.{estudiantes[x]}")

# Muestro menu de opciones
print("\n*** MENU DE OPCIONES ***")
print("1. Agregar un estudiante")
print("2. Eliminar un estudiante")
print("3. Salir")
respuesta = int(input("Opcion: "))

# Ingresa al ciclo while, para realizar las acciones hasta que la opcion seleccionada sea 3 (Salir)
while respuesta != 3:
    if respuesta == 1:
        # Agrego un nombre a la lista
        estudiantes.append(input("Ingrese el nombre del estudiante a agregar: ")) 
        # Imprimo en pantalla lista actualizada
        print("=== LISTA DE ESTUDIANTES ===") 
        for x in range(len(estudiantes)):
            print(f"{x + 1}.{estudiantes[x]}")
    elif respuesta == 2:
        # Obtengo nombre de estudiante a remover de la lista
        estudiante_a_remover = (input("Ingrese el nombre del estudiante a eliminar: "))
        if estudiante_a_remover not in estudiantes: # Si no esta en la lista, imprimo mensaje de error
            print("El nombre ingresado no se encuentra en la lista")
        else:
            estudiantes.remove(estudiante_a_remover) # Elimino nombre de la lista
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

print("Programa terminado")


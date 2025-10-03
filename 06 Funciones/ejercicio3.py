# Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: 
# “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")


print("=== DATOS PERSONALES ===")
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")

while not edad.isdigit():
    print("Solo se aceptan números positivos.")
    edad = input("Edad: ")

residencia = input("Residencia: ")

informacion_personal(nombre, apellido, int(edad), residencia)
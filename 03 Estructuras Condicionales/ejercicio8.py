# EJERCICIO 8

# Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input("Ingrese su nombre: ")

print("*** OPCIONES ***")
print("1. Si quiere su nombre en mayúsculas.")
print("2. Si quiere su nombre en minúsculas.")
print("3. Si quiere su nombre con la primera letra mayúscula.")

opcion = int(input("Ingrese su opción: "))

if opcion == 1:
    print(f"{nombre.upper()}")
elif opcion == 2:
    print(f"{nombre.lower()}")
elif opcion == 3:
    print(f"{nombre.title()}")
else:
    print("Seleccionaste una opción incorrecta.")

print("Programa terminado.")


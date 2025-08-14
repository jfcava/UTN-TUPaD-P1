# EJERCICIO 1
# Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”

print("********** EJERCICIO 1 **********")
print("Hola Mundo!")


# EJERCICIO 2
""" Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
realizar la impresión por pantalla."""

print("********** EJERCICIO 2 **********")
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}! Bienvenido!")


# EJERCICIO 3
""" Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
la impresión por pantalla. """

print("********** EJERCICIO 3 **********")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar_residencia = input("Ingrese su lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}")


# EJERCICIO 4
"""  Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
su perímetro. """

print("********** EJERCICIO 4 **********")

# A = π * r²
# P = 2 * π * r
import math
pi = math.pi

radio = float(input("Ingrese el radio del círculo: "))
area = pi * radio * radio
perimetro = 2 * pi * radio

print(f"El area del circulo es: {area}")
print(f"El perímetro del circulo es: {perimetro}")

# EJERCICIO 5
"""  Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
cuántas horas equivale. """

print("********** EJERCICIO 5 **********")

segundos = float(input("Ingrese la cantidad de segundos: "))
horas = (segundos // 3600)

print(f"{segundos} segundos equivalen a {horas} horas")


# EJERCICIO 6
""" Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
multiplicar de dicho número. """

print("********** EJERCICIO 6 **********")

num = int(input("Ingrese un número para conocer su tabla de multiplicación: "))
print(f"{num} X 1 = {num * 1}")
print(f"{num} X 2 = {num * 2}")
print(f"{num} X 3 = {num * 3}")
print(f"{num} X 4 = {num * 4}")
print(f"{num} X 5 = {num * 5}")
print(f"{num} X 6 = {num * 6}")
print(f"{num} X 7 = {num * 7}")
print(f"{num} X 8 = {num * 8}")
print(f"{num} X 9 = {num * 9}")
print(f"{num} X 10 = {num * 10}")


# EJERCICIO 7
""" Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. """

print("********** EJERCICIO 7 **********")

num1 = int(input("Ingrese un número entero distinto de cero: "))
num2 = int(input("Ingrese otro número entero distinto de cero: "))

print(f"Suma: {num1 + num2}")
print(f"División: {num1 / num2}")
print(f"Multiplicación: {num1 * num2}")
print(f"Resta: {num1 - num2}")


# EJERCICIO 8
""" Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
modo: 
IMC = (peso en kg) / (altura en m)² """

print("********** EJERCICIO 8 **********")
print("*** CONOZCA SU IMC (Índice de Masa Corporal) ***")

altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))

imc = peso / (altura ** 2)

print(f"Su IMC es: {imc}")


# EJERCICIO 9
""" Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:

TEMP EN FAHRENHEIT = (9/5) * TEMP EN CELSIUS + 32 """

print("********** EJERCICIO 9 **********")
print("*** CONVERTIDOR GRADOS CELSIUS A FAHRENHEIT ***")

grados_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
grados_fahrenheit = (9/5) * grados_celsius + 32

print(f"{grados_celsius} grados Celsius equivalen a {grados_fahrenheit} grados Fahrenheit")


# EJERCICIO 10
""" Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
dichos números. """

print("********** EJERCICIO 10 **********")
print("*** CALCULE EL PROMEDIO DE 3 NÚMEROS")

num1 = float(input("Ingrese el número 1: "))
num2 = float(input("Ingrese el número 2: "))
num3 = float(input("Ingrese el número 3: "))

promedio = (num1 + num2 + num3) / 3

print(f"El promedio entre los 3 números ingresados es: {promedio}")






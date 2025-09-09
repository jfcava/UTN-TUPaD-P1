# Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

print("===========================")
print("=== INVERSOR DE NÚMEROS ===")
print("===========================")

num = int(input("Ingrese un número: "))
num_invertido = 0

# Si el numero es negativo, asigno su valor absoluto y guardo su signo en variable "signo"
if num < 0:
    num = abs(num)
    signo = -1
else:
    signo = 1

# Calculo la longitud del numero
longitud_numero = len(str(num)) -1
print(f"longitud del numero: {longitud_numero}")

# Obtengo el ultimo digito y lo guardo en "num_invertido" multiplicado por la base correspondiente
# segun la longitud del numero.
# Luego realizo division entera del numero para guardar el resto de digitos y resto 1 a la
# variable "longitud_numero".
while num > 0:
    digito = num % 10
    num_invertido += digito * (10**longitud_numero)
    num = num // 10 
    longitud_numero -= 1

# Multiplico por variable signo para volver a obtener el numero negativo si asi lo fuera
num_invertido *= signo

print("Número invertido:", num_invertido)

# Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = int(input("Ingrese un número: "))
num_invertido = 0

if num < 0:
    num = abs(num)
    signo = -1
else:
    signo = 1

longitud_numero = len(str(num)) -1

while num > 0:
    digito = num % 10
    num_invertido += digito * (10**longitud_numero)
    num = num // 10
    longitud_numero -= 1

num_invertido *= signo

print("Número invertido:", num_invertido)

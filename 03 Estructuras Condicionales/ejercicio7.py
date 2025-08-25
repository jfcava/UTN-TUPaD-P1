# EJERCICIO 8

# Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.


frase = input("Ingrese una palabra o frase: ")

# Obtengo la ultima letra y la asigno a la variable.
ultima_letra = frase[len(frase) - 1]

# Comparo la ultima letra con las vocales y concateno signo de admiracion en caso que corresponda.
if ultima_letra == "a" or ultima_letra == "e" or ultima_letra == "i" or ultima_letra == "o" or ultima_letra == "u":
    print(f"{frase}!")
else:
    print(frase)

print("Programa terminado.")


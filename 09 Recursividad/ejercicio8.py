# Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.
#  Ejemplos:
# contar_digito(12233421, 2) → 3
# contar_digito(5555, 5) → 4 
# contar_digito(123456, 7) → 0

def contar_digito(numero, digito):
    if numero < 10:
        if numero == digito:
            return 1
        else:
            return 0
    else:
        if numero % 10 == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)

numero = input("Ingrese un numero: ")

if not numero.isdigit():
    print("Solo se aceptan numeros enteros positivos.")
else:
    numero = int(numero)
    digito = input("Ingrese un digito entre 0 y 9: ")

    if not digito.isdigit() or not (0 <= int(digito) <= 9):
        print("El digito debe ser entre 0 y 9.")
    else:
        digito = int(digito)
        print(f"El digito aparece {contar_digito(numero, digito)} veces dentro del numero.")
    
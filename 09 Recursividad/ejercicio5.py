# Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
# Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().

def es_palindromo(cadena):
    
    if len(cadena) <=1:
        return True
    
    if cadena[0] != cadena[-1]:
        return False
    
    return es_palindromo(cadena[1:-1])

def es_valida(cadena):
    tildes = "áéíóúÁÉÍÓÚ"
    
    if " " in cadena:
        return False

    for letra in cadena:
        if letra in tildes:
            return False

    return True

print("=== ES PALÍNDROMO? ===")
cadena = input("Ingrese una cadena de texto: ")

if es_valida(cadena):
    if es_palindromo(cadena.lower()):
        print("Es palindromo.")
    else:
        print("No es palindromo.")
else:
    print("La cadena no puede contener espacios ni tildes.")
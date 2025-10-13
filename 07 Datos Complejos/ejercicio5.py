#  Solicita al usuario una frase e imprime:
#   • Las palabras únicas (usando un set).
#   • Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingrese una frase: ")

palabras = frase.split()
palabras_unicas = set(frase.split())
print(f"Palabras Únicas: {palabras_unicas}")

recuento = {}

for palabra in palabras:
    recuento[palabra] = palabras.count(palabra)

print(f"Recuento: {recuento}")



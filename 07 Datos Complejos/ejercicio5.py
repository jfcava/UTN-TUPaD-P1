#  Solicita al usuario una frase e imprime:
#   • Las palabras únicas (usando un set).
#   • Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingrese una frase: ")

palabras = frase.split() #Se genera una lista con las palabras de la frase
palabras_unicas = set(palabras) #Se transforma la lista en un set eliminando repetidos
print(f"Palabras Únicas: {palabras_unicas}")

recuento = {}

#Se recorre la lista y se carga el diccionario con cantidad de apariciones
for palabra in palabras:
    recuento[palabra] = palabras.count(palabra)

print(f"Recuento: {recuento}")



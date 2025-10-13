# Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
#   • Las capitales sean las claves.
#   • Los países sean los valores.

original = {
    "Argentina" : "Buenos Aires",
    "Chile" : "Santiago",
    "Brasil" : "Brasilia",
    "Colombia" : "Bogotá",
    "Uruguay" : "Montevideo",
    "Venezuela" : "Caracas",
    "Paraguay" : "Asunción"
}

invertido = {}

for pais, capital in original.items():
    invertido[capital] = pais

print(invertido)
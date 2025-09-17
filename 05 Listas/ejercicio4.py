# Dada una lista con valores repetidos:
# datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado.

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
sin_repetir = []

for x in range(len(datos)):
    if datos[x] not in sin_repetir:
        sin_repetir.append(datos[x])

print(sin_repetir)

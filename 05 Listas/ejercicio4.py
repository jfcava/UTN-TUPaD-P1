# Dada una lista con valores repetidos:
# datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado.

# Inicializo variables
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
sin_repetir = []

print("=== LISTA CON ELEMENTOS REPETIDOS ===")
print(datos)

# Recorro lista, si cada elemento del ciclo no esta en la nueva lista, cargo esa lista.
for x in range(len(datos)):
    if datos[x] not in sin_repetir:
        sin_repetir.append(datos[x])

print("\n=== LISTA CON ELEMENTOS SIN REPETIR ===")
print(sin_repetir)

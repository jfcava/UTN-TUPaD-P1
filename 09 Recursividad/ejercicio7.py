# Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la
# pirámide.
#  Ejemplos:
# contar_bloques(1) → 1 (1)
# contar_bloques(2) → 3 (2 + 1)
# contar_bloques(4) → 10 (4 + 3 + 2 + 1)

def contar_bloques(cant_bloques):
    if cant_bloques <= 1:
        return cant_bloques
    else:
        return cant_bloques + contar_bloques(cant_bloques - 1)

cant_bloques = input("Ingrese la cantidad de bloques para la base: ")

if not cant_bloques.isdigit():
    print("Solo se aceptan numeros positivos enteros.")
else:
    cant_bloques = int(cant_bloques)
    print(f"Se necesitan {contar_bloques(cant_bloques)} bloques para construir la piramide.")

# Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# • Inicializarlo con guiones "-" representando casillas vacías.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada.

tateti = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]
print("================")
print("=== Ta-Te-Ti ===")
print("================\n")

for x in tateti:
    print(x)

while True:
    print("Turno jugador 1...")
    fila = int(input("Fila: "))
    columna = int(input("Columna: "))
    if fila <= len(tateti) and columna <= len(tateti[fila]):
        tateti[fila - 1][columna - 1] = "X"
    else:
        print("Posicion erronea")
    
    for x in tateti:
        print(x)
    
    print("Turno jugador 2...")
    fila = int(input("Fila: "))
    columna = int(input("Columna: "))
    if fila <= len(tateti) and columna <= len(tateti[fila]):
        tateti[fila - 1][columna - 1] = "O"
    else:
        print("Posicion erronea")
    
    for x in tateti:
        print(x)
    
    print("Quieren seguir jugando? 1-Si 2-No")
    opc = int(input("Opcion: "))
    if opc == 2:
        print("Juego terminado :(")
        break

# Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# • Inicializarlo con guiones "-" representando casillas vacías.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada.

# Inicializo la lista
tateti = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]

# Imprimo el tateti en pantalla
print("================")
print("=== Ta-Te-Ti ===")
print("================\n")

for x in tateti:
    print(x)

# Inicio ciclo while para que se pueda seguir jugando
while True:
    print("Turno jugador 1...")
    fila = int(input("Fila: ")) # Solicito ingreso de Fila y Columna
    columna = int(input("Columna: "))
    # Verifico que este dentro del rango del tablero y que no este ocupada la casilla
    if 1 <= fila <= len(tateti) and 1 <= columna <= len(tateti[0]):
        if tateti[fila - 1][columna - 1] == "-":
            tateti[fila - 1][columna - 1] = "X"
        else:
            print("Posicion ocupada!")
    else:
        print("Posicion erronea")
    
    # Imprimo tateti en pantalla
    for x in tateti:
        print(x)
    
    # Turno jugador 2
    print("Turno jugador 2...")
    fila = int(input("Fila: "))
    columna = int(input("Columna: "))
    if 1 <= fila <= len(tateti) and 1 <= columna <= len(tateti[0]):
        if tateti[fila - 1][columna - 1] == "-":
            tateti[fila - 1][columna - 1] = "O"
        else:
            print("Posicion ocupada!")
    else:
        print("Posicion erronea")
    
    for x in tateti:
        print(x)
    
    # Pregunto si quiere seguir jugando, sino sale del ciclo
    print("Quieren seguir jugando? 1-Si 2-No")
    opc = int(input("Opcion: "))
    if opc == 2:
        print("Juego terminado :(")
        break

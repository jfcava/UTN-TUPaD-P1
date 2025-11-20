# Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("=== CALCULO DE SERIE DE FIBONACCI ===")
posicion_final = int(input("Indique la posicion final: "))

if posicion_final < 0:
    print("Debe ingresar un número entero positivo.")
else:
    for i in range(posicion_final + 1):
        print(f"Valor en posicion {i}: {fibonacci(i)}")

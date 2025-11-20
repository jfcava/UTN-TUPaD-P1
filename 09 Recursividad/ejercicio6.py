# Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
#  Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)

def suma_digitos(n):
    if n // 10 < 1:
        return n
    else:
        return (n%10) + suma_digitos(n//10)

print("=== SUMA DE DIGITOS ===")
numero = input("Ingrese un numero: ")

if not numero.isdigit():
    print("El numero debe ser entero positivo.")
else:
    numero = int(numero)
    print(f"La suma de todos sus digitos es: {suma_digitos(numero)}")
# Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

def celsius_a_fahrenheit(celsius):
    return celsius * 1.8 + 32

print("=== CELSIUS A FAHRENHEIT ===")
temp = float(input("Ingrese la temperatura en Celsius: "))
print(f"Temperatura en Fahrenheit: {celsius_a_fahrenheit(temp)}")

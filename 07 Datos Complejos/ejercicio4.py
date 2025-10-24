# Escribí un programa que permita almacenar y consultar números telefónicos.
#   • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#   • Luego, pedí un nombre y mostrale el número asociado, si existe.

contactos = {}

print("=== CARGAR TELÉFONOS ===")

# Se carga el diccionario 'contactos' con datos
for i in range(5):
    nombre = input(f"{i + 1}. Nombre: ")
    telefono = int(input("Teléfono: "))
    contactos[nombre] = telefono
    
    print("Contacto agregado.")
    print()
print("Agregaste los 5 contactos exitosamente.")

print("=== BUSCÁ UN CONTACTO ===")
busqueda = input('Nombre a buscar: ')
# Se realiza la busqueda del contacto y se imprime en pantalla
if busqueda in contactos:
    print()
    print(f"Nombre: {busqueda}")
    print(f"Teléfono: {contactos[busqueda]}")
else:
    print("No se encontró el contacto.")

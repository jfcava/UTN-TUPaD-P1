# Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora.

agenda = {
    ("lunes", "10:00") : "Reunion",
    ("martes", "15:00") : "Clase de ingles",
    ("miercoles", "11:00") : "Turno dentista",
    ("jueves", "12:00") : "Almuerzo",
    ("viernes", "09:00") : "Presentacion producto"
}

print("=== BUSCADOR DE AGENDA ===")
dia = input("Ingrese el día: ").lower()
hora = input("Ingrese la hora (hh:mm): ")

busqueda = (dia, hora)

if busqueda in agenda:
    dia, hora = busqueda
    print(f"\nDia: {dia} - Horario: {hora}")
    print(f"Actividad: {agenda[busqueda]}")
else:
    print("No hay ninguna actividad en ese horario.")

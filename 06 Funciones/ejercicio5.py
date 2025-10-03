# Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro 
# y devuelva la cantidad de horas correspondientes. 
# Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    return round((segundos / 60),2)

print("=== CALCULO DE HORAS ===")
seg = input("Cantidad de segundos: ")

while not seg.isdigit():
    print("Solo se aceptan números positivos.")
    seg = input("Cantidad de segundos: ")

print(f"Cantidad de horas: {segundos_a_horas(float(seg))} horas")
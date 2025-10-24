# Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
#   • Mostrá los que aprobaron ambos parciales.
#   • Mostrá los que aprobaron solo uno de los dos.
#   • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial1 = {"Ana", "Lucas", "María", "Sofía", "Tomás"}
parcial2 = {"Bruno", "Camila", "Diego", "Ana", "Valentina", "Lucas", "Mateo", "Tomás"}

#Interseccion - Elementos que estan en ambos sets
print("Aprobaron ambos parciales:", parcial1 & parcial2)

#Diferencia Simetrica - Elementos que estan en un set pero no en ambos
print("Aprobaron solo un parcial:", parcial1 ^ parcial2)

#Union - Todos los elementos sin repetir
print("Lista de estudiantes que aprobaron al menos un parcial:", parcial1 | parcial2)



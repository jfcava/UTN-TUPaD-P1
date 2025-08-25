# EJERCICIO 10

# Utilizando la información aportada en la siguiente tabla sobre las estaciones del año

#   PERIODO DEL AÑO                                 ESTACION EN EL             ESTACION EN EL
#                                                   HEMISFERIO NORTE           HEMISFERIO SUR
# Desde el 21 de diciembre hasta el 20 de           Invierno                   Verano
# marzo (incluidos)

# Desde el 21 de marzo hasta el 20 de junio         Primavera                  Otoño
# (incluidos)

# Desde el 21 de junio hasta el 20 de               Verano                     Invierno
# septiembre (incluidos)

# Desde el 21 de septiembre hasta el 20 de          Otoño                      Primavera
# diciembre (incluidos)

# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

# Obtengo los datos de entrada
print("======= CONOCÉ TU ESTACIÓN DEL AÑO =======")
hemisferio = input("Ingresá en cuál hemisferio te encontrás (N - Norte, S - Sur): ").upper()
mes = int(input("Ingresa el número de mes actual: "))
dia = int(input("Ingresa el número de día actual: "))

# Declaro variable para guardar la estacion
estacion_del_anio = ""

if (mes >= 1 and mes <= 12) and (dia >= 1 and dia <= 31): # Valido que sean fechas correctas
    if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
        estacion_del_anio = "Invierno"
    elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
        estacion_del_anio = "Primavera"
    elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
        estacion_del_anio = "Verano"
    else:
        estacion_del_anio = "Otoño"

    # Comparo el hemisferio y si es el contrario a N, invierto los valores.        
    if hemisferio == "N":
        print(f"Usted se encuentra en {estacion_del_anio}")
    else:
        if estacion_del_anio == "Invierno":
            print("Usted se encuentra en Verano")
        elif estacion_del_anio == "Otoño":
            print("Usted se encuentra en Primavera")
        elif estacion_del_anio == "Primavera":
            print("Usted se encuentra en Otoño")
        else:
            print("Usted se encuentra en Invierno")
            
else:
    print("Ingresaste datos incorrectos")
    

    
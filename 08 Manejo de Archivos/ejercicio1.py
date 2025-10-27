# 1. Crear archivo inicial con productos: Crear un archivo de texto llamado
# productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad

nuevos_productos = [
    "Pantalon,80000,25",
    "Campera,250000,10",
    "Remera,25000,80"
]

with open("productos.txt", "w") as archivo:
    for linea in nuevos_productos:
        archivo.write(f"{linea}\n")

# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
# línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
# formato: Producto: Lapicera | Precio: $120.5 | Cantidad: 30

with open("productos.txt", "r") as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        lista = linea.strip().split(",")
        print(f"Producto: {lista[0]} | Precio: ${lista[1]} | Cantidad: {lista[2]}")


# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
# cantidad) y lo agregue al archivo sin borrar el contenido existente.

respuesta = "Si"

while respuesta.lower() == "si":
    print("\nIngrese un nuevo producto")
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))

    nuevo_producto = f"{nombre},{precio},{cantidad}\n"

    with open("productos.txt", "a") as archivo:
        archivo.write(nuevo_producto)
        print("\nProducto agregado exitosamente.")

    respuesta = input("\nDesea cargar mas productos? Si - No: ")


# 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
# una lista llamada productos, donde cada elemento sea un diccionario con claves:
# nombre, precio, cantidad.

productos = []

with open("productos.txt","r") as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        partes = linea.strip().split(",")
        productos.append({
            "Nombre" : partes[0],
            "Precio" : partes[1],
            "Cantidad" : partes[2] + "\n"
        })

# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
# producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
# no existe, mostrar un mensaje de error.

encontrado = False

busqueda = input("\nIngrese nombre de producto a buscar: ")
for producto in productos:
    if busqueda.lower() in producto["Nombre"].lower():
        encontrado = True
        print("Producto encontrado!\n")
        print(f"Producto: {producto['Nombre']}")
        print(f"Precio: {producto['Precio']}")
        print(f"Cantidad: {producto['Cantidad']}")

if encontrado == False:
    print("El producto no se encontro en la base de datos.")

# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
# productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
# productos actualizados desde la lista.

with open("productos.txt", "w") as archivo:
    for producto in productos:
        nombre = producto["Nombre"]
        precio = producto["Precio"]
        cantidad = producto["Cantidad"]

        nueva_entrada = f"{nombre},{precio},{cantidad}"

        archivo.write(nueva_entrada)

print("Archivo productos.txt actualizado exitosamente.")
    

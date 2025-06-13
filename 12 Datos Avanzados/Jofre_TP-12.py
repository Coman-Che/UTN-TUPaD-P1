# 1) Dado el diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
# 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

# Diccionario inicial
precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450
}

# Nuevas frutas a añadir
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Mostrar el diccionario actualizado
print(precios_frutas)

####################################################################################################

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

# Diccionario inicial
precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450
}

# Añadir nuevas frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Actualizar precios de frutas existentes
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# Mostrar el diccionario final
print(precios_frutas)


####################################################################################################

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.

# Diccionario inicial
precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450
}

# Añadir nuevas frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Actualizar precios de frutas existentes
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# Crear lista con solo los nombres de las frutas
lista_frutas = list(precios_frutas.keys())

# Mostrar la lista de frutas
print(lista_frutas)


####################################################################################################

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.
# Ejemplo:
# contactos = {"Juan":"123456", "Ana":"987654"}
# # Consultar: "Juan" -> muestra "123456"

# Crear diccionario para almacenar los contactos
contactos = {}

# Cargar 5 contactos desde el input del usuario
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i+1}: ").strip().lower()
    numero = input(f"Ingresá el número de teléfono de {nombre.capitalize()}: ").strip()
    contactos[nombre] = numero

# Consultar un contacto
consulta = input("Ingresá el nombre del contacto que querés consultar: ").strip().lower()

# Mostrar el número si el contacto existe
if consulta in contactos:
    print(f"El número de {consulta.capitalize()} es {contactos[consulta]}")
else:
    print(f"No se encontró el contacto '{consulta}'")

####################################################################################################

# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.
# Ejemplo:
# #Entrada -> "hola mundo hola"
# #Salida:
# Palabras_unicas: {"hola","mundo"}
# Recuento: {"hola": 2, "mundo": 1}

# Solicitar una frase al usuario
frase = input("Ingresá una frase: ").strip().lower()

# Separar la frase en palabras
palabras = frase.split()

# Obtener palabras únicas usando un set
palabras_unicas = set(palabras)

# Crear un diccionario con el recuento de cada palabra
recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

# Mostrar los resultados
print("Palabras únicas:", palabras_unicas)
print("Recuento:", recuento)


####################################################################################################

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.
# Ejemplo:
# alumnos = {
#     "Sofía": (10, 9, 8),
#     "Luis": (6, 7, 7) 
# }

# Crear diccionario para almacenar alumnos y sus notas
alumnos = {}

# Cargar los datos de 3 alumnos
for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ").strip()
    
    print(f"Ingresá las 3 notas de {nombre}, separadas por espacios:")
    notas_entrada = input().strip()
    notas = tuple(map(int, notas_entrada.split()))
    
    # Validar que haya exactamente 3 notas
    if len(notas) != 3:
        print("Error: Debés ingresar exactamente 3 notas.")
        exit()
    
    alumnos[nombre] = notas

# Calcular y mostrar el promedio de cada alumno
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es {promedio:.2f}")

####################################################################################################

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

# Ingresar estudiantes que aprobaron el Parcial 1
aprobados_parcial1 = set(input("Ingresá los nombres de los estudiantes que aprobaron el Parcial 1 (separados por espacios): ").split())

# Ingresar estudiantes que aprobaron el Parcial 2
aprobados_parcial2 = set(input("Ingresá los nombres de los estudiantes que aprobaron el Parcial 2 (separados por espacios): ").split())

# Estudiantes que aprobaron ambos parciales
ambos = aprobados_parcial1 & aprobados_parcial2

# Estudiantes que aprobaron solo uno de los dos
solo_uno = aprobados_parcial1 ^ aprobados_parcial2

# Estudiantes que aprobaron al menos un parcial
al_menos_uno = aprobados_parcial1 | aprobados_parcial2

# Mostrar resultados
print("Aprobaron ambos parciales:", ambos)
print("Aprobaron solo uno de los dos:", solo_uno)
print("Aprobaron al menos un parcial:", al_menos_uno)

####################################################################################################

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

# Diccionario inicial vacío
stock_productos = {}

while True:
    print("\nOpciones:")
    print("1 - Consultar stock")
    print("2 - Agregar unidades a un producto existente")
    print("3 - Agregar un nuevo producto")
    print("4 - Salir")

    opcion = input("Elegí una opción (1-4): ").strip()

    if opcion == '1':
        producto = input("Ingresá el nombre del producto a consultar: ").strip()
        if producto in stock_productos:
            print(f"El stock de {producto} es {stock_productos[producto]} unidades.")
        else:
            print(f"El producto '{producto}' no existe en el stock.")

    elif opcion == '2':
        producto = input("Ingresá el nombre del producto para agregar unidades: ").strip()
        if producto in stock_productos:
            try:
                unidades = int(input("Ingresá la cantidad de unidades a agregar: "))
                if unidades < 0:
                    print("No se pueden agregar unidades negativas.")
                else:
                    stock_productos[producto] += unidades
                    print(f"Nuevo stock de {producto}: {stock_productos[producto]} unidades.")
            except ValueError:
                print("Por favor, ingresá un número válido.")
        else:
            print(f"El producto '{producto}' no existe en el stock.")

    elif opcion == '3':
        producto = input("Ingresá el nombre del nuevo producto: ").strip()
        if producto in stock_productos:
            print(f"El producto '{producto}' ya existe.")
        else:
            try:
                unidades = int(input("Ingresá la cantidad inicial de unidades: "))
                if unidades < 0:
                    print("La cantidad no puede ser negativa.")
                else:
                    stock_productos[producto] = unidades
                    print(f"Producto '{producto}' agregado con {unidades} unidades.")
            except ValueError:
                print("Por favor, ingresá un número válido.")

    elif opcion == '4':
        print("Saliendo...")
        break

    else:
        print("Opción no válida, por favor elegí entre 1 y 4.")


####################################################################################################

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Ejemplo:
# agenda={
#     ("lunes", "10:00"): "Reunion",
#     ("martes", "15:00"): "Clase de inglés"
# Permití consultar qué actividad hay en cierto día y hora.

# Crear agenda vacía
agenda = {}

# Cargar algunos eventos (podés modificar o agregar aquí si querés)
# Por ejemplo:
agenda[("lunes", "10:00")] = "Reunión"
agenda[("martes", "15:00")] = "Clase de inglés"

# Consultar evento
dia = input("Ingresá el día: ").strip().lower()
hora = input("Ingresá la hora (formato HH:MM): ").strip()

clave = (dia, hora)

if clave in agenda:
    print(f"El evento programado para {dia} a las {hora} es: {agenda[clave]}")
else:
    print(f"No hay ningún evento programado para {dia} a las {hora}")

####################################################################################################

# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.
# Ejemplo:
# original={"argentina":"buenos aires", "chile": "santiago"}
# invertido={"buenos aires": "argentina", "santiago": "chile"}

# Diccionario original: pedimos que el usuario ingrese países y capitales
original = {}

n = int(input("¿Cuántos países querés ingresar?: "))

for i in range(n):
    pais = input(f"Ingresá el nombre del país {i+1}: ").strip().lower()
    capital = input(f"Ingresá la capital de {pais}: ").strip().lower()
    original[pais] = capital

# Invertir el diccionario
invertido = {capital: pais for pais, capital in original.items()}

# Mostrar el diccionario invertido
print("Diccionario invertido (capital: país):")
print(invertido)

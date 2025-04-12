# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

# Solicitar la edad del usuario
edad = int(input("Por favor, ingresa tu edad: "))

# Verificar si es mayor de edad
if edad > 18:
    print("Es mayor de edad.")

###################################################################################################

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.

# Solicitar la nota al usuario
nota = float(input("Por favor, ingresa tu nota: "))

# Determinar si está aprobado o desaprobado
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

###################################################################################################

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

# Solicitar un número al usuario
numero = int(input("Por favor, ingrese un número: "))

# Verificar si el número es par:
if numero % 2 == 0:
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par.")

###################################################################################################

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

# Solicitar la edad al usuario
edad = int(input("Por favor, ingresa tu edad: "))

# Evaluar en qué categoría entra
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

###################################################################################################

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

# Solicitar una contraseña al usuario
contrasena = input("Por favor, ingrese una contraseña (entre 8 y 14 caracteres): ")

# Evaluar la longitud de la contraseña
if len(contrasena) >= 8 and len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

###################################################################################################

# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
# y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el
# siguiente:
# from statistics import mode, median, mean
# mi_lista = [1,2,5,5,3]
# mean(mi_lista)
# En la documentación oficial se puede encontrar más información sobre este paquete:
# https://docs.python.org/es/3.8/library/statistics.html.
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
# pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
# mediana es mayor que la moda.
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
# la mediana es menor que la moda.
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma:
# import random
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
# forma aleatoria.

import random
from statistics import mean, median, mode

# Crear la lista de 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular los parámetros estadísticos
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

# Mostrar los valores calculados
print(f"Números: {numeros_aleatorios}")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

# Evaluar el sesgo
if media > mediana > moda:
    print("La distribución tiene sesgo positivo (a la derecha).")
elif media < mediana < moda:
    print("La distribución tiene sesgo negativo (a la izquierda).")
elif media == mediana == moda:
    print("La distribución no tiene sesgo.")
else:
    print("No se puede determinar claramente un sesgo con estos datos.")

###################################################################################################

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

# Solicitar una frase o palabra al usuario
texto = input("Ingrese una frase o palabra: ")

# Verificar si termina con una vocal (minúscula o mayúscula)
if texto[-1].lower() in "aeiou":
    texto += "!"  # Agregar signo de exclamación si termina en vocal

# Mostrar el resultado
print("Resultado:", texto)

###################################################################################################

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

# Solicitar el nombre al usuario
nombre = input("Ingrese su nombre: ")

# Mostrar las opciones
print("¿Cómo desea ver su nombre?")
print("1. En mayúsculas")
print("2. En minúsculas")
print("3. Con la primera letra en mayúscula")

# Solicitar la opción
opcion = input("Ingrese el número de la opción (1, 2 o 3): ")

# Aplicar la transformación según la opción
if opcion == "1":
    print("Resultado:", nombre.upper())
elif opcion == "2":
    print("Resultado:", nombre.lower())
elif opcion == "3":
    print("Resultado:", nombre.title())
else:
    print("Opción no válida. Por favor, elija 1, 2 o 3.")

###################################################################################################

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

# Solicitar al usuario la magnitud del terremoto
magnitud = float(input("Ingrese la magnitud del terremoto (escala de Richter): "))

# Clasificar según la escala de Richter
if magnitud < 3:
    print("Muy leve (imperceptible).")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
else:
    print("Extremo (puede causar graves daños a gran escala).")

###################################################################################################

# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
# Periodo del año Estación en el
# hemisferio norte
# Estación en el
# hemisferio sur
# Desde el 21 de diciembre hasta el 20 de
# marzo (incluidos) Invierno Verano
# Desde el 21 de marzo hasta el 20 de junio
# (incluidos) Primavera Otoño
# Desde el 21 de junio hasta el 20 de
# septiembre (incluidos) Verano Invierno
# Desde el 21 de septiembre hasta el 20 de
# diciembre (incluidos) Otoño Primavera
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

# Solicitar la información del usuario
hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").upper()
mes = int(input("¿Qué mes del año es? (1-12): "))
dia = int(input("¿Qué día del mes es? (1-31): "))

# Validar si la información ingresada es válida
if hemisferio not in ['N', 'S']:
    print("Hemisferio no válido. Por favor ingresa 'N' para el hemisferio norte o 'S' para el hemisferio sur.")
else:
    # Verificar la estación según el hemisferio y el mes/día ingresado
    if hemisferio == 'N':  # Hemisferio Norte
        if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
            print("Estación: Invierno")
        elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
            print("Estación: Primavera")
        elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
            print("Estación: Verano")
        else:  # Otoño (restante)
            print("Estación: Otoño")
    
    elif hemisferio == 'S':  # Hemisferio Sur
        if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
            print("Estación: Verano")
        elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
            print("Estación: Otoño")
        elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
            print("Estación: Invierno")
        else:  # Primavera (restante)
            print("Estación: Primavera")
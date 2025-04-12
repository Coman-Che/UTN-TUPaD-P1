#1)Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola Mundo!")


#####################################################################################################################


#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.

nombre = input("Por favor, ingrese su nombre: ")

print (f"Hola {nombre}!")


#####################################################################################################################


#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

nombre = input("Por favor, ingrese su nombre: ")
apellido = input("Por favor, ingrese su apellido: ")
edad = input("Por favor, ingrese su edad: ")
lugar_residencia = input("Por favor, ingrese su lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}")


#####################################################################################################################


#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.

import math
radio = float (input ("Por favor, ingrese el radio de un círculo: "))

area = math.pi*radio**2
perimetro = 2*math.pi*radio

print(f"El área del círculo es {area} y su perímetro es {perimetro}")


#####################################################################################################################


#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.

segundos = int(input("Por favor, ingrese una cantidad de segundos: "))

horas = segundos // 3600
segundos_restantes = segundos % 3600

print (f"Los segundos ingresados equivalen a {horas} horas y {segundos_restantes} segundos")


#####################################################################################################################


#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.

numero = int(input("Por favor, ingrese un número: "))

print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")


#####################################################################################################################


#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numero1 = int(input("Por favor, ingrese un primer número entero (distinto de 0): "))
numero2 = int(input("Por favor, ingrese un segundo número entero (distinto de 0): "))


if numero1 == 0 or numero2 == 0:
    print("Error: Los números no pueden ser 0.")
else:

    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2


    print(f"La suma de {numero1} y {numero2} es: {suma}")
    print(f"La resta de {numero1} y {numero2} es: {resta}")
    print(f"La multiplicación de {numero1} y {numero2} es: {multiplicacion}")
    print(f"La división de {numero1} y {numero2} es: {division}")


#####################################################################################################################


    #8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo:
#𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔/(𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2

peso = float(input("Por favor, ingrese su peso en kilogramos (kg): "))
altura = float(input("Por favor, ingrese su altura en metros (m): "))

imc = peso / (altura ** 2)

print(f"Su índice de masa corporal (IMC) es: {imc}")


#####################################################################################################################


#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
#𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5*𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

celsius = float(input("Por favor, ingrese una temperatura en grados Celsius: "))

fahrenheit = (9/5) * celsius + 32

print(f"La temperatura en Fahrenheit es: {fahrenheit}°F")


#####################################################################################################################


#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.

num1 = float(input("Por favor, ingrese el primer número: "))
num2 = float(input("Por favor, ingrese el segundo número: "))
num3 = float(input("Por favor, ingrese el tercer número: "))

promedio = (num1 + num2 + num3) / 3

print(f"El promedio de los tres números es: {promedio}")
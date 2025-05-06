# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for numero in range(0, 101):
    print(numero)

##################################################################################################

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

# Solicitar un número entero al usuario
numero = int(input("Ingresa un número entero: "))

# Trabajamos con el valor absoluto para contar dígitos (ignora signo negativo)
numero_abs = abs(numero)

# Contador de dígitos
contador = 0

# Caso especial: si el número es 0, tiene 1 dígito
if numero_abs == 0:
    contador = 1
else:
    while numero_abs > 0:
        numero_abs //= 10  # División entera para eliminar el último dígito
        contador += 1

print("El número tiene", contador, "dígito(s).")

##################################################################################################

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

# Solicitar los dos valores al usuario
a = int(input("Ingresa el primer número entero: "))
b = int(input("Ingresa el segundo número entero: "))

# Determinar cuál es el menor y cuál el mayor
inicio = min(a, b)
fin = max(a, b)

# Inicializar la suma y el contador
suma = 0
numero = inicio + 1  # Comenzar justo después del menor

# Sumar todos los números entre inicio y fin (excluidos)
while numero < fin:
    suma += numero
    numero += 1

print("La suma de los números entre", a, "y", b, "es:", suma)

##################################################################################################

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

# Inicializar la suma
suma_total = 0

# Solicitar el primer número
numero = int(input("Ingresa un número entero (0 para terminar): "))

# Mientras el número no sea 0, continúa sumando
while numero != 0:
    suma_total += numero
    numero = int(input("Ingresa un número entero (0 para terminar): "))

# Mostrar el resultado final
print("La suma total es:", suma_total)

##################################################################################################

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

# Generar un número aleatorio entre 0 y 9
numero_secreto = random.randint(0, 9)

# Inicializar el contador de intentos
intentos = 0

# Variable para almacenar la suposición del usuario
adivinanza = -1  # Cualquier valor diferente de numero_secreto

# Bucle hasta que el usuario adivine correctamente
while adivinanza != numero_secreto:
    adivinanza = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1

# Mostrar el resultado
print("¡Correcto! Adivinaste el número en", intentos, "intento(s).")

##################################################################################################

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

# Comienza desde 100, el número par más alto dentro del rango
numero = 100

# Bucle que continúa mientras el número sea mayor o igual que 0
while numero >= 0:
    print(numero)
    numero -= 2  # Resta 2 para ir al siguiente número par menor

##################################################################################################

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

# Solicitar al usuario un número entero positivo
limite = int(input("Ingresa un número entero positivo: "))

# Inicializar la suma y el contador
suma = 0
contador = 0

# Bucle que suma todos los números desde 0 hasta (limite - 1)
while contador < limite:
    suma += contador
    contador += 1

# Mostrar el resultado
print("La suma de los números entre 0 y", limite, "es:", suma)

##################################################################################################

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# Se puedes cambiar este valor para probar con menos números
total_numeros = 100

# Inicializar los contadores
pares = 0
impares = 0
positivos = 0
negativos = 0

# Contador para controlar el bucle
contador = 0

# Bucle para pedir los números
while contador < total_numeros:
    numero = int(input(f"Ingrese el número {contador + 1}: "))

    # Clasificar el número como par o impar
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    # Clasificar el número como positivo o negativo (0 no cuenta en ninguno)
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

    contador += 1

# Mostrar los resultados
print("\nResultados:")
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)

##################################################################################################

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

# Se puede cambiar este valor para probar con menos números
total_numeros = 100

# Inicializar la suma de los números y el contador de entradas
suma = 0
contador = 0

# Bucle para pedir los números
while contador < total_numeros:
    numero = int(input(f"Ingrese el número {contador + 1}: "))
    suma += numero  # Suma el número ingresado
    contador += 1  # Incrementa el contador

# Calcular la media
media = suma / total_numeros

# Mostrar el resultado
print(f"\nLa media de los {total_numeros} números ingresados es: {media}")

##################################################################################################

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

# Solicitar al usuario un número entero
numero = int(input("Ingresa un número entero: "))

# Inicializar una variable para almacenar el número invertido
numero_invertido = 0

# Utilizar un bucle while para invertir el número
while numero > 0:
    # Obtener el último dígito del número
    digito = numero % 10
    # Agregar el dígito al número invertido
    numero_invertido = numero_invertido * 10 + digito
    # Eliminar el último dígito del número original
    numero //= 10

# Mostrar el número invertido
print("El número invertido es:", numero_invertido)

# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario

# Función recursiva para calcular el factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Pedir al usuario un número entero positivo
numero = int(input("Introduce un número entero positivo: "))

# Verificamos que el número sea mayor o igual a 1
if numero < 1:
    print("Por favor, introduce un número mayor o igual a 1.")
else:
    print(f"Factoriales del 1 al {numero}:")
    for i in range(1, numero + 1):
        print(f"{i}! = {factorial(i)}")

##############################################################################################

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.

# Función recursiva para calcular el valor de Fibonacci en la posición n
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Solicitar al usuario una posición
posicion = int(input("Introduce una posición (número entero no negativo): "))

# Verificamos que el número sea válido
if posicion < 0:
    print("Por favor, introduce un número entero no negativo.")
else:
    print(f"Serie de Fibonacci hasta la posición {posicion}:")
    for i in range(posicion + 1):
        print(f"F({i}) = {fibonacci(i)}")

##############################################################################################

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un
# algoritmo general.

# Función recursiva para calcular la potencia
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# Solicitar al usuario la base y el exponente
base = float(input("Introduce la base (número): "))
exponente = int(input("Introduce el exponente (entero no negativo): "))

# Verificación del exponente
if exponente < 0:
    print("Por favor, introduce un exponente entero no negativo.")
else:
    resultado = potencia(base, exponente)
    print(f"{base} elevado a la {exponente} es igual a {resultado}")

##############################################################################################

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.
# Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y
# unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este
# procedimiento:
# 1. Dividir el número por 2.
# 2. Guardar el resto (0 o 1).
# 3. Repetir el proceso con el cociente hasta que llegue a 0.
# 4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.
# Convertir el número 10 a binario:
# 10 ÷ 2 = 5 resto: 0
# 5 ÷ 2 = 2 resto: 1
# 2 ÷ 2 = 1 resto: 0
# 1 ÷ 2 = 0 resto: 1
# Leyendo los restos de abajo hacia arriba: 1 0 1 0 → El resultado binario es "1010".

# Función recursiva para convertir un número decimal a binario
def decimal_a_binario(n):
    if n == 0:
        return ''
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# Solicitar un número al usuario
numero = int(input("Introduce un número entero positivo: "))

if numero < 0:
    print("Por favor, introduce un número entero positivo.")
elif numero == 0:
    print("El número 0 en binario es: 0")
else:
    binario = decimal_a_binario(numero)
    print(f"El número {numero} en binario es: {binario}")

##############################################################################################

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
# lo es.
# Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):
    # Caso base: si la palabra tiene 0 o 1 letras, es un palíndromo
    if len(palabra) <= 1:
        return True
    # Comparar primer y último carácter
    if palabra[0] != palabra[-1]:
        return False
    # Llamada recursiva con la subcadena del medio
    return es_palindromo(palabra[1:-1])

# Prueba del usuario
entrada = input("Introduce una palabra (sin espacios ni tildes): ").lower()

# Mostrar el resultado
if es_palindromo(entrada):
    print(f"'{entrada}' es un palíndromo.")
else:
    print(f"'{entrada}' no es un palíndromo.")

##############################################################################################

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
# Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

# Ejemplo de uso
numero = int(input("Introduce un número entero positivo: "))

if numero < 0:
    print("Por favor, introduce un número entero positivo.")
else:
    resultado = suma_digitos(numero)
    print(f"La suma de los dígitos de {numero} es: {resultado}")

##############################################################################################

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la
# pirámide.
# Ejemplos:
# contar_bloques(1) → 1 (1)
# contar_bloques(2) → 3 (2 + 1)
# contar_bloques(4) → 10 (4 + 3 + 2 + 1)

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

# Solicitar al usuario la cantidad de bloques del nivel más bajo
nivel_inferior = int(input("Introduce la cantidad de bloques en el nivel más bajo: "))

if nivel_inferior < 1:
    print("Por favor, introduce un número entero mayor o igual a 1.")
else:
    total = contar_bloques(nivel_inferior)
    print(f"Se necesitan {total} bloques para construir la pirámide.")

##############################################################################################

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.
# Ejemplos:
# contar_digito(12233421, 2) → 3
# contar_digito(5555, 5) → 4
# contar_digito(123456, 7) → 0

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        coincidencia = 1 if (numero % 10) == digito else 0
        return coincidencia + contar_digito(numero // 10, digito)

# Ejemplo de uso
numero = int(input("Introduce un número entero positivo: "))
digito = int(input("Introduce un dígito entre 0 y 9: "))

# Validación de entradas
if numero < 0 or digito < 0 or digito > 9:
    print("Entrada inválida. Asegúrate de ingresar un número positivo y un dígito entre 0 y 9.")
else:
    resultado = contar_digito(numero, digito)
    print(f"El dígito {digito} aparece {resultado} veces en el número {numero}.")
# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
# range.

multiplos_de_4 = list(range(4, 101, 4))
print(multiplos_de_4)

########################################################################################################

# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
# penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
# indexing con números negativos!

mi_lista = ['comida', 'películas', 'series', 'streamings', 'caminar']
penultimo_elemento = mi_lista[-2]
print("El penúltimo elemento es:", penultimo_elemento)

########################################################################################################

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
# pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
# ejemplo:
# lista_vacia = []

# Crear una lista vacía
lista_vacia = []

# Agregar tres palabras con append
lista_vacia.append("perro")
lista_vacia.append("gato")
lista_vacia.append("raton")

# Imprimir la lista resultante
print("Lista resultante:", lista_vacia)

########################################################################################################

# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
# respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
# en los videos o bien investigar cómo funciona el indexing con números negativos!
# animales = ["perro", "gato", "conejo", "pez"]

animales = ["perro", "gato", "conejo", "pez"]

# Reemplazar el segundo (índice 1) por "loro"
animales[1] = "loro"

# Reemplazar el último (índice -1) por "oso"
animales[-1] = "oso"

# Imprimir la lista resultante
print("Lista modificada:", animales)

########################################################################################################

# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
# numeros = [8, 15, 3, 22, 7]
# numeros.remove(max(numeros))
# print(numeros)

# Rta: Este programa crea una lista llamada "numeros" con los valores [8, 15, 3, 22, 7]. 
# Luego busca el número más grande de la lista usando "max(numeros)"", que en este caso es 22.
# Elimina ese número máximo (22) de la lista con "numeros.remove(...)".
# Luego imprime la lista resultante, sin incluir el número más grande de la lista (22).

########################################################################################################

# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
# pantalla los dos primeros.

# Crear la lista con números del 10 al 30, saltando de 5 en 5
numeros = list(range(10, 31, 5))

# Mostrar los dos primeros elementos
print("Los dos primeros números son:", numeros[0], "y", numeros[1])

########################################################################################################

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
# cualesquiera.
# autos = ["sedan", "polo", "suran", "gol"]

autos = ["sedan", "polo", "suran", "gol"]

# Reemplazar los elementos en las posiciones 1 y 2
autos[1:3] = ["camioneta", "coupe"]

# Imprimir la lista resultante
print("Lista modificada:", autos)

########################################################################################################

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
# directamente. Imprimir la lista resultante por pantalla.

# Crear una lista vacía
dobles = []

# Agregar el doble de 5, 10 y 15
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

# Imprimir la lista resultante
print("Lista de dobles:", dobles)

########################################################################################################

# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
# diferentes clientes:
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
# ["agua"]]
# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla

# Lista inicial
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" a la lista del tercer cliente (índice 2)
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente (índice 1)
compras[1][1] = "tallarines"

# c) Eliminar "pan" de la lista del primer cliente (índice 0)
compras[0].remove("pan")

# d) Imprimir la lista resultante
print("Lista de compras actualizada:", compras)

########################################################################################################

# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.

# Crear la lista anidada
lista_anidada = [
    15,                     # lista_anidada[0]
    True,                  # lista_anidada[1]
    [25.5, 57.9, 30.6],    # lista_anidada[2][0], [2][1], [2][2]
    False                  # lista_anidada[3]
]

# Imprimir la lista resultante
print("Lista anidada:", lista_anidada)
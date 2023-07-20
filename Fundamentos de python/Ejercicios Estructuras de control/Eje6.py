"""

Escribe un programa que encuentre el número más grande en una lista ingresada por el usuario. 
Utiliza la estructura de control for.


"""
numeros = []  # Lista vacía para almacenar los números

# Solicitar al usuario ingresar la cantidad de números que desea ingresar
cantidad = int(input("Ingrese la cantidad de números que desea ingresar: "))

# Utilizar un bucle for para solicitar al usuario ingresar los números y almacenarlos en la lista
for i in range(cantidad):
    numero = int(input("Ingrese el número: "))
    numeros.append(numero)

# Inicializar la variable "mayor" con el primer número de la lista
mayor = numeros[0]

# Utilizar un bucle for para comparar cada número de la lista con el número mayor actual
for numero in numeros:
    if numero > mayor:
        mayor = numero

# Imprimir el número más grande encontrado
print("El número más grande es:", mayor)

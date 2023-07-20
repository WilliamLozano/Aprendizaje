# 2 Ejercicio 

# Escribe un programa que tome una lista de números y calcule la suma de todos los 
# elementos. Por ejemplo, si la lista es [2, 4, 6, 8], la salida debería ser: 20.

Lista = [2, 4, 6, 8, 10]

def calcular_suma(Lista):
    suma = 0 
    for numero in Lista:
        suma += numero
    return suma

print(f"La suma de todos los elementos de la lista es : {calcular_suma(Lista)}") # Con funciones hechas por mi.

print(f"La suma de todos los elementos de la lista es : {sum(Lista)}") # Con funciones predeterminadas de python.

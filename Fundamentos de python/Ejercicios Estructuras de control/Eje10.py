"""

Escribe un programa que calcule el factorial de un número ingresado por el usuario utilizando un bucle while.


"""
numero = int(input("Ingrese un número para calcular su factorial: "))
# Solicitamos al usuario que ingrese un número y lo convertimos a entero usando la función int(). 
# El número ingresado se asigna a la variable 'numero'.

if numero < 0:
    print("El número debe ser no negativo.")
else:
    factorial = 1
    # Inicializamos la variable 'factorial' en 1, ya que el factorial de 0 es 1.

    while numero > 0:
        factorial *= numero
        # Multiplicamos 'factorial' por el valor actual de 'numero'.
        # En cada iteración del bucle, 'factorial' se actualiza con la multiplicación.

        numero -= 1
        # Restamos 1 a 'numero' en cada iteración para avanzar hacia el siguiente número en el factorial.

    print("El factorial es:", factorial)
    # Imprimimos el resultado del factorial.


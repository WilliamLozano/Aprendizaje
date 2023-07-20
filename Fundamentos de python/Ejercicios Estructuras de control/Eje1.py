
"""

Escribe un programa que verifique si un número ingresado por el usuario es positivo, negativo o cero.

"""

while True:

    num = int(input("Ingrese un numero : "))

    if num > 0:
        print(f"El numero {num} es positivo!") 
    elif num < 0 :
        print(f"El numero {num} es negativo  o cero!")
    else:
        print(f"El numero {num} ingresado es erroneo.")


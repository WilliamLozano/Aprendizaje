# Ejercicio 4:
# Escribe un programa que solicite al usuario ingresar un año e indique si es un año bisiesto o no. Un año bisiesto es aquel que es divisible
# por 4, excepto aquellos que son divisibles por 100 pero no por 400.




while True:
    
    num = int(input("Ingrese un numero : "))

    if num % 4 == 0 and (num % 100 != 0 or num % 400 == 0):
        print("Es bisiesto")
    else:
        print("No es bisiesto")



"""

Escribe un programa que resuelva el siguiente problema: dado un número entero positivo ingresado por el usuario, 
verifica si es un número primo.


"""

while True:


    num = int(input("Ingrese un numero : "))

    if num <= 1:
        print("el numero no es primo")
    else:
        es_primo = True

    for i in range(2, num //2 +1):
        if num % i == 0:
            es_primo = False
            break

        if es_primo:
            print("El numero es primo")
        else:
            print("El numero no es primo")
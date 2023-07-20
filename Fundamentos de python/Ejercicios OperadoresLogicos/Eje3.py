# Ejercicio 3:
# Escribe un programa que tome un número entero ingresado por el usuario y verifique si es divisible por 3 y por 5 simultáneamente utilizando
# el 
# operador lógico "and".

while True:

    num = int(input("Ingrese un numero : "))

    if num % 3  == 0 and num % 5 == 0:
        print("Es divisible")
    else:
        print("No es divisible") 
    

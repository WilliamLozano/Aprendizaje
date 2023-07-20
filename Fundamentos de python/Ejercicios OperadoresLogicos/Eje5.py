# Escribe un programa que tome un número entero ingresado por el usuario y verifique si es mayor que 10 y menor que 20 utilizando
# los operadores de  comparación.

while True:

    num = int(input("Ingrese un numero : "))
    
    if num >= 10 and num < 20:
        print(f"El numero {num} es mayor que 10 y menor que 20")
    else:
        print(f"El numero {num}  no cumple los requisitos...")

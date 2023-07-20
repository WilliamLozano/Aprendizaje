# Escribe un programa que tome un número entero ingresado por el usuario y verifique si es negativo utilizando el operador de comparación 
# "<".

while True:

    num1 = int(input("Ingrese un numero : "))
    num2 = int(input("Ingrese un numero : "))

    if num1 < num2:
        print(f"el numero {num1} es menor que el numero {num2}")
    else:
        print(f"el numero {num2} es menor que el numero {num1}")
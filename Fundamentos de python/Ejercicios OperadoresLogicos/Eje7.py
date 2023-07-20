# Escribe un programa que tome dos números ingresados por el usuario y determine si el primero es mayor que el segundo utilizando el 
# operador de comparación ">".

while True:

    num1 = (int(input("Ingrese un numero : ")))
    num2 = (int(input("Ingrese otro numero : ")))

    if num1 > num2:
        print(f"El numero {num1} es mayor que el numero {num2}")
    else: 
        print(f"el numero {num2} es mayor que el numero {num1}")
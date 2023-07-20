# Escribe un programa que tome un número entero ingresado por el usuario y determine si es par o impar utilizando el operador de
# módulo (%).
while True:

    num1 = int(input("Ingrese un numero : "))

    if num1 % 2 == 0:
        print("es par")
    else:
        print("es impar")
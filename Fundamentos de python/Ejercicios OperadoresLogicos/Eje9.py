# Escribe un programa que tome tres números ingresados por el usuario y determine si forman una terna pitagórica
# (cumplen el teorema de Pitágoras) utilizando operadores aritméticos.

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
c = float(input("Ingresa el tercer número: "))

if a**2 + b**2 == c**2:
    print("Los números forman una terna pitagórica.")
else:
    print("Los números no forman una terna pitagórica.")

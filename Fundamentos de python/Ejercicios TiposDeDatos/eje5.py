# Ejercicio 5

# Escribe un programa que tome un número entero y determine si es un número primo. Un número primo es aquel que solo
# es divisible por 1 y por sí mismo. Por ejemplo, si el número es 7, la salida debería ser: "Es un número primo".


def es_primo(numero):
    if numero < 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
        return True
    
Entero = int(input("Ingrese un numero entero : "))

if es_primo(Entero):
    print("Es un numero primo")
else:
    print("No es un numero primo")

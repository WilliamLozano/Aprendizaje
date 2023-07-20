"""

Pedir al usuario que ingrese un número entero positivo y verificar si es un número primo.


"""


numero = int(input("Ingresa un numero positivo : "))

es_primo = True

if numero < 1:
    es_primo = False
else:
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break
if es_primo:
    print(f"el {numero} es un numero primo")
else:
    print(f"el {numero} no es un numero primo")
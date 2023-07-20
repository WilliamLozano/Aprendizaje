"""

Imprimir los números primos del 1 al 100.


"""

for i in range(1,101):
    if i % 2 == 1:
        print(f"el numero {i} es primo")
    elif i % 2 == 0:
        print(f"el numero {i} es par")
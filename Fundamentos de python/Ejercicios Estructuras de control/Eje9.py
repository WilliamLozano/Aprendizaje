"""

Escribe un programa que muestre la tabla de multiplicar de un número ingresado por el usuario, del 1 al 10.



"""

num = int(input("Ingrese un numero : "))

for i in range(num):

    l1  = [num]
    l1 = num * 1
    print(l1)
    l1 = num * 2
    print(l1)
    l1 = num * 3
    print(l1)
    l1 = num * 4
    print(l1)
    l1 = num * 5
    print(l1)
    l1 = num * 6
    print(l1)
    l1 = num * 7
    print(l1)
    l1 = num * 8
    print(l1)
    l1 = num * 9
    print(l1) 
    l1 = num * 10
#     print(l1)

numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))

for i in range(1, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)




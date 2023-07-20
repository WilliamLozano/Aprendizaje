"""

Imprimir la tabla de multiplicar del número ingresado por el usuario, desde el 1 hasta el 10.


"""

x = int(input("Ingrese un numero para sacarle la table de multiplicar: "))

for i in range(1,13):

    resultado = x * i

    print(f" {x} x {i} = {resultado} ")
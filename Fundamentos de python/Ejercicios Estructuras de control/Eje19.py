"""

Imprimir la tabla de multiplicar de un número ingresado por el usuario.


"""

num = int(input("Ingrese un numero : "))

for i in range(1,11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")

    
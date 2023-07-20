"""

Calcular el factorial de un número ingresado por el usuario.


"""

num = int(input("Ingresa un numero : "))

n = 0

if num < 0:
    "No se aceptan numeros negativos"
else:
    for i in range(1, num + 1):
        n *= i
        
print(f"El factorial de {num} es : {n}")



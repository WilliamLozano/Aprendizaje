"""

Imprimir una secuencia de caracteres n veces, donde n es un número ingresado por el usuario.


"""

n = str(input("Ingrese un caracter : "))

for letras in n:
    m = int(input("Cuantas veces quieres que se repita el caracter : "))
    n *= m  
    print(f"El caracter {n} se repitira {m} veces ", end="")


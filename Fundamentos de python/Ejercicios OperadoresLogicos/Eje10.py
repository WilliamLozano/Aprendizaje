# Escribe un programa que calcule el promedio de tres calificaciones ingresadas por el usuario.

while True:
    
    nota1 = float(input("Ingrese su calificacion de Matematicas : "))
    nota2 = float(input("Ingrese su calificacion de Ingles: "))
    nota3 = float(input("Ingrese su calificacion de Fisica: "))

    suma = nota1 + nota2 + nota3

    print(f"El promedio de sus 3 asignaturas es {suma / 3}")
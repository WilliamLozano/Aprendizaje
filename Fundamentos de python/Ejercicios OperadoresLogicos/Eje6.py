# Ejercicio 5:
# Escribe un programa que tome una cadena de texto ingresada por el usuario y verifique si contiene la palabra "Python" 
# utilizando el operador de pertenencia "in"

while True:


        cadena = input("Ingresa una cadena de texto: ")

        if "Python" in cadena:
            print("La cadena contiene la palabra 'Python'.")
        else:
            print("La cadena no contiene la palabra 'Python'.")
"""

Pedir al usuario que ingrese una palabra y contar cuántas vocales (a, e, i, o, u) contiene.


"""

x = str(input("Ingrese una palabra : "))
suma = 0

for letras in x:
    if letras == "a" or letras == "e" or letras == "i" or letras == "o" or letras == "u":  
        print(f"La palabra {x} tiene la vocal {letras} ")


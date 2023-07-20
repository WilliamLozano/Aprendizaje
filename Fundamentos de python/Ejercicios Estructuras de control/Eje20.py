"""

Contar la cantidad de vocales en una palabra ingresada por el usuario.

"""

f = str(input("Ingrese una palabra : "))
cantidad_vocales = 0

for letra in f:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        cantidad_vocales += 1

print(f"La cantidad de vocales en la palabra {f} es: {cantidad_vocales}")


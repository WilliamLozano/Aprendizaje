# 3 Ejercicio 

# Escribe un programa que tome una cadena de texto y cuente cuántas veces aparece una letra específica en esa cadena. 
# Por ejemplo, si la cadena es "Hola mundo" y la letra es "o", la salida debería ser: 2.


def contador_cadena(Cadena, letra):
    contador = 0 
    for caracter in Cadena:
        if caracter == letra:
            contador += 1
    return contador

Cadena = "Hola Mundo!"
Letra = "o"

print(f"La letra {Letra} aparece {contador_cadena(Cadena, Letra)} veces en la cadena ")


"""

Imprimir los caracteres de una cadena en orden inverso.

"""

# 1 forma

def reverse(cadena):
    for i in range((len(cadena)) -1, -1, -1):
        print(cadena[i], end = "")


p = "William"

reverse(p)

# 2 forma

p = "pedro"

for i in range(len(p) -1, -1, -1):
    print(p[i], end="")



"""

Imprimir los números pares del 1 al 50.


"""

# 1 forma

for i in range (1,51):
    if i % 2 == 0:
        print(f"Es par -> {i}")


# 2 forma

for i in range (2, 51, 2):
    print(f"Es par > {i} ")

    
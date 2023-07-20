"""

Calcular la suma de los elementos de una lista.


"""

# 1 forma

suma = 1

for i in [1,2,3,4,5,6,7,8,9,10]:
    suma += i

print(f"La suma de todos los elementos de la lista es {suma}")

# 2 forma

l1 = [12,12,12,12,12]

suma = 0

for i in l1:
    suma += i

print(f"La suma de todo lo que hay en {l1} es: {suma} ")



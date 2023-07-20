"""

Escribe un programa que encuentre la suma de todos los números pares del 1 al 100 utilizando un bucle for.

"""
# suma = 0

# for num in range(1, 101):
#     if num % 2 == 0:
#         "es par"
#         suma += num

# print(f"la suma de todos los pares de los numeros 1 al 100 es {suma}")

suma = 0

for num in range(1, 101):
    if num % 2 == 0:
        suma += num

print("La suma de los números pares del 1 al 100 es:", suma)
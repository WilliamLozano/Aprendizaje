"""

Calcular e imprimir los primeros 20 términos de la secuencia de Fibonacci. La secuencia comienza con 0 y 1, 
y cada término posterior es la suma de los dos términos anteriores (0, 1, 1, 2, 3, 5, ...).

"""

suma = 0

a,b = 0, 1

for i in range(20):
    print(a, end= " ")
    a, b = b, a + b


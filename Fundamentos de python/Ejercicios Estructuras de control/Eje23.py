"""

Calcular la suma de los primeros 50 números naturales.


"""

suma = 0

for i in range(1, 51):
    suma += i
    
print(f"La suma de los {i} primeros naturales es {suma}")
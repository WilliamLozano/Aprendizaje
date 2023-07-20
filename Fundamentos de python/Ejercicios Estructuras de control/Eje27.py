"""

Calcular la suma de los primeros 100 números primos.

"""
# suma = 0

# for i in range(1,101):
#     if i % 2 == 0:
#         suma += i

# print(f"La suma de todos los numeros primos es {suma} ")



# Calcular la suma de los primeros 100 números primos
contador_primos = 0
suma_primos = 0

for num in range(2, 200):  # Iniciamos el rango desde 2, ya que 1 no es primo
    es_primo = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        suma_primos += num
        contador_primos += 1
    if contador_primos == 100:
        break

# Mostrar el resultado
print("La suma de los primeros 100 números primos es:", suma_primos)

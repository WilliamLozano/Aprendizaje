# Ejercicio 4

# Escribe un programa que tome una lista de nombres y los ordene alfabéticamente. Luego, muestra la lista ordenada.
# Por ejemplo,si la lista es ["Juan", "Ana", "Carlos"], la salida debería ser: ["Ana", "Carlos", "Juan"].

def tomador_nombres(lista):
    lista.sort()
    return lista

nombres = ["Pedro", "Juan", "William"]

print(f"los nombres estan ordenados alfabeticamente : {tomador_nombres(nombres)}")
# Estructura de control if-else:
# La estructura de control if-else se utiliza para tomar decisiones en función de una condición. 
# Permite ejecutar un bloque de código si la condición se evalúa como verdadera y otro bloque de código si 
# la condición se evalúa como falsa.

condicion = 0

if condicion:
    pass # Bloque de código si la condición es verdadera
else:
    pass # Bloque de código si la condición es falsa


# La condición puede ser cualquier expresión booleana. Si la condición es verdadera, se ejecuta el bloque de código 
# indentado después de la declaración "if". Si la condición es falsa, se ejecuta el bloque de código indentado después 
# de la declaración "else".

#------------------------------------------------------------------------------------------------------------------------

# Estructura de control if-elif-else:
# La estructura de control if-elif-else se utiliza cuando hay múltiples condiciones a evaluar. 
# "elif" es una abreviatura de "else if". Se evalúan las condiciones en orden y se ejecuta el bloque de 
# código correspondiente a la primera condición verdadera encontrada.

condicion1 = 0
condicion2 = 0

if condicion1:
    pass# Bloque de código si la condicion1 es verdadera
elif condicion2:
    pass# Bloque de código si la condicion2 es verdadera
else:
    pass# Bloque de código si ninguna condición es verdadera


"""Si alguna de las condiciones es verdadera, se ejecuta el bloque de código correspondiente y el programa sale 
de la estructura. Si todas las condiciones son falsas, se ejecuta el bloque de código después de la declaración "else"
"""

#------------------------------------------------------------------------------------------------------------------------

"""Estructura de control while:
La estructura de control while se utiliza para repetir un bloque de código mientras una condición sea verdadera. El bloque 
de código se ejecuta repetidamente hasta que la condición se evalúe como falsa.
"""

while condicion:
    pass # Bloque de código a repetir mientras la condicion sea verdadera


"""
Antes de cada repetición, se verifica la condición. Si es verdadera, se ejecuta el bloque de código y luego se vuelve a 
verificar la condición. Si la condición es falsa, se sale del bucle y se continúa con la ejecución del código siguiente.
"""

#------------------------------------------------------------------------------------------------------------------------

"""
Estructura de control for:
La estructura de control for se utiliza para iterar sobre una secuencia o colección de elementos (como una lista, tupla o 
cadena) o para repetir un bloque de código una cantidad específica de veces.
"""

secuencia = 0

for elemento in secuencia:
    pass # Bloque de código a ejecutar para cada elemento en la secuencia

"""
El bucle for toma cada elemento de la secuencia uno por uno y ejecuta el bloque de código asociado. Después de procesar 
todos los elementos, el bucle se completa y el programa continúa con la ejecución del código siguiente.
Estas estructuras de control son fundamentales en la programación y te permiten controlar el flujo de ejecución 
de tu programa. Puedes anidar estructuras de control dentro de otras para crear lógica más compleja. 
¡Espero que esta explicación te sea útil!
"""
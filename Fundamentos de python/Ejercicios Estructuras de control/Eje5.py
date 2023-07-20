"""

Escribe un programa que encuentre la suma de todos los dígitos de un número entero positivo ingresado por el usuario.


"""

numero = int(input("Ingresa un número entero positivo: "))

# Verificamos que el número sea positivo
if numero < 0:
    print("El número debe ser positivo.")
else:
    suma_digitos = 0
    # Convertimos el número en una cadena para poder acceder a cada dígito
    numero_str = str(numero)
    for digito in numero_str:
        suma_digitos += int(digito)

    print("La suma de los dígitos de", numero, "es:", suma_digitos)

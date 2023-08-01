def solicitar_datos_personales(nombre_archivo):
    try:
        with open(nombre_archivo, 'w') as archivo:
            print("Ingrese sus datos personales:")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            edad = input("Edad: ")
            email = input("Email: ")

            # Escribir los datos en el archivo
            archivo.write(f"Nombre: {nombre}\n")
            archivo.write(f"Apellido: {apellido}\n")
            archivo.write(f"Edad: {edad}\n")
            archivo.write(f"Email: {email}\n")

        print(f"Los datos personales se han guardado en el archivo '{nombre_archivo}'.")
    except Exception as e:
        print(f"Error: {e}")

# Ejemplo de uso:
nombre_archivo = "datos_personales.txt"
solicitar_datos_personales(nombre_archivo)

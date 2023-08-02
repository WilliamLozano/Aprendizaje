"""

Supongamos que queremos guardar datos en un nuevo archivo CSV llamado nuevos_datos.csv.


"""

import csv

def escribir_en_archivo_csv(nombre_archivo):
    datos = [
        ["Pedro", "Gómez", 35, "pedro.gomez@example.com"],
        ["María", "López", 28, "maria.lopez@example.com"]
    ]

    try:
        with open(nombre_archivo, 'w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerow(["nombre", "apellido", "edad", "email"])  # Escribir encabezados
            escritor_csv.writerows(datos)  # Escribir los datos
        print(f"Se han escrito los datos en el archivo '{nombre_archivo}'.")
    except Exception as e:
        print(f"Error: {e}")

# Ejemplo de uso:
nombre_archivo = "nuevos_datos.csv"
escribir_en_archivo_csv(nombre_archivo)


"""

En este ejemplo, utilizamos el módulo csv para escribir datos en el archivo nuevos_datos.csv. El método csv.writer() 
se utiliza para escribir en el archivo. Primero escribimos una fila con los encabezados y luego escribimos las filas
de datos utilizando writerows().


"""
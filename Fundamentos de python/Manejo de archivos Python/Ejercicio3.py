



import csv


# Supongamos que tenemos un archivo CSV llamado datos.csv con la siguiente estructura:



# nombre,apellido,edad,email
# John,Doe,30,john.doe@example.com
# Jane,Smith,25,jane.smith@example.com



def leer_archivo_csv(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', newline='') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            encabezados = next(lector_csv)  # Leer la primera fila como encabezados

            for fila in lector_csv:
                print(f"Nombre: {fila[0]}, Apellido: {fila[1]}, Edad: {fila[2]}, Email: {fila[3]}")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")
    except Exception as e:
        print(f"Error: {e}")


# En este ejemplo, utilizamos el módulo csv para leer el archivo datos.csv. El método csv.reader() lee el 
# archivo línea por línea y cada línea se convierte en una lista. Usamos next() para leer la primera línea
# como encabezados y luego recorremos el resto de las filas para imprimir los datos.



# Ejemplo de uso:
nombre_archivo = "datos.csv"
leer_archivo_csv(nombre_archivo)

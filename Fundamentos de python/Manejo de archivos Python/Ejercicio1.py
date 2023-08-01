"""
1. Crea un archivo nuevo con un nombre que se pasa como parámetro a la función. Valide si el archivo ya existe, 
en tal caso no lo debe re-crear. Además debe decir cuantas lineas tiene el archivo existente
"""
def Contador_Lineas_Archivo(nombre_archivo):
    try:
        archivo_existente = open(nombre_archivo, 'r')
        lineas = archivo_existente.readlines()
        num_lineas = len(lineas)
        print(f"El archivo '{nombre_archivo}' ya existe y tiene {num_lineas} líneas.")
        archivo_existente.close()
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")
    except Exception as e:
        print(f"Error: {e}")

def crear_archivo(nombre_archivo):
    try:
        nuevo_archivo = open(nombre_archivo, 'x')
        print(f"Se ha creado el archivo '{nombre_archivo}'.")
        nuevo_archivo.close()
    except FileExistsError:
        print(f"El archivo '{nombre_archivo}' ya existe.")
    except Exception as e:
        print(f"Error: {e}")

nombre_archivo = "Hola.txt"
Contador_Lineas_Archivo(nombre_archivo)
crear_archivo(nombre_archivo)
Contador_Lineas_Archivo(nombre_archivo)
    
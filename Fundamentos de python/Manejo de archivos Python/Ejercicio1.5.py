def crear_archivo_y_contar_lineas(nombre_archivo):
    try:
        # Intentamos abrir el archivo en modo lectura para contar las líneas
        with open(nombre_archivo, 'r') as archivo_existente:
            # Contamos las líneas del archivo
            lineas = archivo_existente.readlines()
            num_lineas = len(lineas)
            print(f"El archivo '{nombre_archivo}' ya existe y tiene {num_lineas} líneas.")
    except FileNotFoundError:
        # Si el archivo no existe, lo creamos
        with open(nombre_archivo, 'w') as nuevo_archivo:
            print(f"Se ha creado el archivo '{nombre_archivo}'.")
    except Exception as e:
        print(f"Error: {e}")

# Ejemplo de uso:
nombre_archivo = "mi_archivo.txt"
crear_archivo_y_contar_lineas(nombre_archivo)

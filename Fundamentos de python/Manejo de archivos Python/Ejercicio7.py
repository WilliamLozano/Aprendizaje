"""


    #Escriba un programa que diga cuantas letras tiene cada linea del coro del himno de soacha escriba la respuesta en otro archivo.


"""

def contLineas(nuevo_archivo):
    try:
        archivo_existente = open("C:\\Users\\SENA\\Desktop\\Carpeta\\Aprendizaje\\Fundamentos de python\\Manejo de archivos Python\\File.txt", "r", encoding=  "utf-8")
        lineas = archivo_existente.readlines()
        num_lineas = len(lineas)
        print(f"El archivo {nuevo_archivo} ya  existe y tiene {num_lineas} lineas")
        archivo_existente.close()
    except Exception as e:
        print(f"Error : {e}")


def Crear_Archivo(nuevo_archivo):
    try:
        nuevo_archivo = open(nuevo_archivo, "x", encoding= "utf-8")
        print(f"el archivo {nuevo_archivo} se ha creado ")
        nuevo_archivo.close()

    except Exception:
        print("")

nombre_archivo = "pito.txt"
contLineas(nombre_archivo)
Crear_Archivo(nombre_archivo)
contLineas(nombre_archivo)
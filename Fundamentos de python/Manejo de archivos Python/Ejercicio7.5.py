def contador_letras(linea):
    linea_sin_nada= linea.replace(" ", "").replace("\n", "").replace(",", "").replace(".", "")  
    return len(linea_sin_nada)


archivo_entrada = "File.txt"

archivo_salida = str(input("Ingrese el nombre de el archivo : "))

archivo_entrada_obj = open(archivo_entrada, "r")
lineas = archivo_entrada_obj.readlines()
archivo_entrada_obj.close()

cont_letras = [contador_letras(linea) for linea in lineas]

arch
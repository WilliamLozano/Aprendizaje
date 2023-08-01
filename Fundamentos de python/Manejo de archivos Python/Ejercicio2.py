"2. Solicitar datos personales para guardarlos en un archivo. Se pasa como parámetro el nombre del archivo "
"donde quiere guardar los datos personales. Se ingresan por teclado"

def Datos_Personales(nombre_archivo):
    try:
        archivo_existente = open(nombre_archivo, "w")
        print("Ingrese sus datos personales.")
        nombre = input("Ingrese su nombre : ")
        apellido = input("Ingrese su apellido : ")
        telefono = input("Ingrese su telefono : ")
        correo = input("Ingrese su correo : ")
        
        archivo_existente.write(f"Nombre : {nombre} \n")
        archivo_existente.write(f"Apellido : {apellido} \n")
        archivo_existente.write(f"Telefono : {telefono} \n" )
        archivo_existente.write(f"Correo : {correo} \n")

        archivo_existente.close()
        print(f"Se ha creado el archivo y se han guardado sus datos personales : '{nombre_archivo}'.")
        archivo_existente.close()
    except FileExistsError:
        print(f"El archivo {nombre_archivo} ya existe")
    

nombre_archivo = "Datos.txt"
Datos_Personales(nombre_archivo)
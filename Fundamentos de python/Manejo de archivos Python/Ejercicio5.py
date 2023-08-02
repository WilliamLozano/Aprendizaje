

s = "Aprendizaje/Fundamentos de python/Manejo de archivos Python/File.txt"

stream=open(s, "r", encoding="utf-8")
    
linea=stream.readline()

contador = 1
try:
    while linea != "":
        print(f"{contador} {linea}")
        linea=stream.readline()
        contador+=1
except IOError  as e:
    print(e,"ERROR")
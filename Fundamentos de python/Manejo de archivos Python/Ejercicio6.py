try:
    s = "Aprendizaje/Fundamentos de python/Manejo de archivos Python/File.txt"

    stream=open(s, "r", encoding="utf-8")
        
    linea=stream.readlines()


    for linea in stream.readlines():
        print(linea)


except IOError as e :
    print(f"Error {e}")




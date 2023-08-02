class Icfes:
    def __init__(self, Documento, Genero, Correo, Telefono ):
        self.__Documento = Documento
        self.__Genero = Genero
        self.__Correo = Correo
        self.__Telefono = Telefono

    
    def verDatos(self):
        return f"{self.__Documento} {self.__Genero} {self.__Correo} {self.__Telefono}"
    
    def getDocumento(self):
        return self.__Documento
    
    def getGenero(self):
        return self.__Genero
    
    def getCorreo(self):
        return self.__Correo
    
    def getTelefono(self):
        return self.__Telefono
    
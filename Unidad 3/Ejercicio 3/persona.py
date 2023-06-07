class persona:
    __nombre = ''
    __direccion = ''
    __dni = ''
    __inscripcion = object
    def __init__ (self,nom,direccion,dni,inscripcion):
        self.__nombre = nom
        self.__direccion = direccion
        self.__dni = dni
        self.__inscripcion = inscripcion
    def getnombre(self):
        return self.__nombre
    def getdireccion(self):
        return self.__direccion
    def getdni(self):
        return self.__dni
    def getinscripcion(self):
        return self.__inscripcion
    
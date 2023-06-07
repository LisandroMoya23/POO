class carrera:
    __codigoFacu = ''
    __codigoCarrera = ''
    __nombre = ''
    __duracion = ''
    __titulo = ''
    __nivel = ''
    def __init__(self,codigoF,codigoC,nombre,duracion,titulo,nivel):
        self.__codigoFacu = codigoF
        self.__codigoCarrera = codigoC
        self.__nombre = nombre
        self.__duracion = duracion
        self.__titulo = titulo
        self.__nivel = nivel
    def getcodigoFacu(self):
        return self.__codigoFacu
    def getcodigoCarrera(self):
        return self.__codigoCarrera
    def getnombre(self):
        return self.__nombre
    def getnivel(self):
        return self.__nivel
    def getduracion(self):
        return self.__duracion
    def gettitulo(self):
        return self.__titulo
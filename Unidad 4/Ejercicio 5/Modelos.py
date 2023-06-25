class Pelicula:
    __lenguaje: str
    __titulo: str
    __resumen: str
    __fecha: str
    def __init__(self,lenguaje,titulo,resumen,fecha):
        self.__fecha = fecha
        self.__lenguaje = lenguaje
        self.__titulo = titulo
        self.__resumen = resumen
    def getLen(self):
        return self.__lenguaje
    def getTit(self):
        return self.__titulo
    def getResu(self):
        return self.__resumen
    def getFecha(self):
        return self.__fecha
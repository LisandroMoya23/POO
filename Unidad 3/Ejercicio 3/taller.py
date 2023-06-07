class taller:
    __idTaller = int
    __nombre = ''
    __vacantes = int
    __montoInscripcion = float
    __personas = list
    __inscripcion = object
    def __init__(self,id,nom,vacantes,monto):
        self.__idTaller = id
        self.__nombre = nom
        self.__vacantes = vacantes
        self.__montoInscripcion = monto
        self.__personas = []
    def getidtaller(self):
        return self.__idTaller
    def getnombre(self):
        return self.__nombre
    def getvacantes(self):
        return self.__vacantes
    def getmonto(self):
        return self.__montoInscripcion
    def agregarPersona(self,unaPersona):
        self.__personas.append(unaPersona)
    def restarVacante(self):
        self.__vacantes-=1
    

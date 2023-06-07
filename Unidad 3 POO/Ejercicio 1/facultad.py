from carrera import carrera
class facultad:
    __codigo = 0
    __nombre = ''
    __direccion = ''
    __localidad = ''
    __telefono = ''
    __carreras: list
    __provincia = 'San Juan'
    def __init__(self,codigo,nombre,direccion,localidad,telefono):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__direccion = direccion
        self.__localidad = localidad
        self.__telefono = telefono
        self.__carreras = []
    @classmethod
    def getprovincia(cls):
        return cls.__provincia
    def getcodigo(self):
        return self.__codigo
    def getnombre(self):
        return self.__nombre
    def getdireccion(self):
        return self.__direccion
    def getlocalidad(self):
        return self.__localidad
    def gettelefono(self):
        return self.__telefono
    def getcarreras(self):
        return self.__carreras
    def agregarCarrera(self,fila):
        codF = fila[0]
        codC = fila[1]
        nom = fila[2]
        titulo = fila[3]
        duracion = fila[4]
        nivel = fila[5]
        unaCarrera = carrera(codF,codC,nom,duracion,titulo,nivel)
        self.__carreras.append(unaCarrera)
    def __del__ (self):
        print("Borrando facultad...")
        del self.__carreras
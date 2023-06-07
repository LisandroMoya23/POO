import csv
from facultad import facultad
from carrera import carrera
class ManejaFacultades:
    __facultades = []
    def __init__(self):
        self.__facultades = []
    def cargaFacultad(self,unaFacultad):
        self.__facultades.append(unaFacultad)
    def test(self):
        archivo = open('C:\\Users\\lisan\\OneDrive\\2° Año\\Programación Orientada a Objetos\\Unidad 3\\Ejercicio 1\\Facultades.csv',encoding='utf8')
        reader = csv.reader(archivo,delimiter=',')
        unaFacultad = None
        for fila in reader:
            if (len(fila) == 5):
                codigo = fila[0]
                nombre = fila[1]
                direccion = fila[2]
                localidad = fila[3]
                telefono = fila[4]
                unaFacultad = facultad(codigo,nombre,direccion,localidad,telefono)
                self.cargaFacultad(unaFacultad)
            else:
                unaFacultad.agregarCarrera(fila)
    def muestraDatos(self):
        for i in range(len(self.__facultades)):
            print("Facultad: ",self.__facultades[i].getnombre())
            carrera = self.__facultades[i].getcarreras()
            for j in range(len(carrera)):
                print("Carrera: ",carrera[j].getnombre())
        return
    def buscaCodigo(self,cod):
        i = 0
        b = False
        retorno = None
        while not b and i < len(self.__facultades):
            if(cod == self.__facultades[i].getcodigo()):
                b = True
                retorno = i
            else:
                i+1
        return retorno
    def muestra1(self,cod):
        b = self.buscaCodigo(cod)
        if (b == None):
            print("El codigo de facultad es incorrecto.")
        else:
            print("Nombre de facultad: ",self.__facultades[b].getnombre())
            print("-- Lista de carreras --")
            carreras = self.__facultades[b].getcarreras()
            for i in range(len(carreras)):
                print("Nombre: ",carreras[i].getnombre())
                print("Duracion: ",carreras[i].getduracion())
        return
    def buscaNom(self,nom):
        i = 0
        j = 0
        b = False
        retorno = None
        while not b and i < len(self.__facultades):
            carreras = self.__facultades[i].getcarreras()
            while not b and j < len(carreras):
                if(carreras[j].getnombre() == nom):
                    b = True
                    retorno = [None,None]
                    retorno[0] = i
                    retorno[1] = j
                j+=1
            i+=1
        return retorno
    def muestra2(self,nom):
        b = self.buscaNom(nom)
        if (b == None):
            print("El nombre de la carrera es incorrecto.")
        else:
            carreras = self.__facultades[b[1]].getcarreras()
            print("Codigo de carrera: {},{}".format(carreras[b[1]].getcodigoFacu(),carreras[b[1]].getcodigoCarrera()))
            print("Nombre de facultad: {}".format(self.__facultades[b[0]].getnombre()))
            print("Localidad: {}".format(self.__facultades[b[0]].getlocalidad()))
    

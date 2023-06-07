from taller import taller
import csv
class ManejadorPersonas:
    __listaPersonas= list
    def __init__(self):
        self.__listaPersonas = []
    def agregarPersona(self,unaPersona):
        self.__listaPersonas.append(unaPersona)
    def test(self):
        archivo = open('C:\\Users\\lisan\\OneDrive\\2° Año\Programación Orientada a Objetos\\Unidad 3\\Ejercicio 3\\talleres.csv', encoding="utf8")
        reader = csv.reader(archivo,delimiter=',')
        for fila in reader:
            unaPersona = (fila[0],fila[1],fila[2],fila[3])
            self.agregarPersona(unaPersona)
            archivo.close()
    
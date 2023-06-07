from sabores import sabor
import csv

class ManejadorSabores:
    __listaSabores = list
    def __init__(self):
        self.__listaSabores = []
    def agregarSabor(self,unSabor):
        self.__listaSabores.append(unSabor)
    def test(self):
        archivo = open('C:\\Users\\lisan\\OneDrive\\2° Año\\Programación Orientada a Objetos\\Unidad 3\\Ejercicio 2\\sabores.csv')
        reader = csv.reader(archivo,delimiter=";")
        for fila in reader:
            unSabor = sabor(fila[0],fila[1],fila[2])
            self.agregarSabor(unSabor)
        archivo.close()
    def getlista(self):
        return self.__listaSabores
    def compara(self,sabor):
        b = None
        i = 0
        while i in range(len(self.__listaSabores)):
            if(sabor == self.__listaSabores[i].getnom()):
                i = len(self.__listaSabores)
                b = True
            else:
                b = False
                i+=1
        return b
    def ordenar(self):
        self.__listaSabores.sort()
        return self.__listaSabores
    def buscaid(self,num):
        retorno = None
        i=0
        while i < len(self.__listaSabores):
            if(num == self.__listaSabores[i].getid()):
                retorno = self.__listaSabores[i].getnom()
                i = len(self.__listaSabores)
            i+=1
        return retorno
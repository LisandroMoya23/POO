from ViajeroFrecuente6 import ViajeroFrecuente
import csv
class manejadorViajero:
    def __init__(self):
        self.__listaViajero= []
    def agregarViajero(self,unViajero):
        self.__listaViajero.append(unViajero)
    def testViajero(self):
        archivo = open('Ejercicio 6\Datos6.csv')
        reader = csv.reader(archivo,delimiter=',')
        for fila in reader:
            num = fila[0]
            dni = fila[1]
            nom = fila[2]
            apellido = fila[3]
            millas = int(fila[4])
            unViajero = ViajeroFrecuente(num,dni,nom,apellido,millas)
            self.agregarViajero(unViajero)
        archivo.close()
    def buscaViajero(self,num):
        i=0
        Retorno = None
        b = False
        while not b and i < len(self.__listaViajero):
            if self.__listaViajero[i].getNumViajero()==num:
                b =True
                Retorno=i
            else:
                i+=1
        return Retorno
    def getMillas(self,n):
        return(self.__listaViajero[n].getTotalMillas())
    def acumularMillas(self,nuevas_millas,n):
        return self.__listaViajero[n] + nuevas_millas
    def canjearMillas(self,cant,n):
        return self.__listaViajero[n] - cant
    def compararMillas(self,cant,n):
        if(self.__listaViajero[n] == cant):
            print("Las millas ingresadas son iguales.")
        else:
            print("Las millas ingresadas no son iguales.")
    def comparaViajeros(self):
        i=0
        maximo = max(self.__listaViajero)
        for i in range(len(self.__listaViajero)):
            if self.__listaViajero[i].getTotalMillas() == maximo.getTotalMillas():
                print("El viajero",self.__listaViajero[i].getNumViajero(),"tiene el maximo de millas.")
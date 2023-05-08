import csv
from Email import Email
class manejadorEmail:
    def __init__(self):
        self.__listaEmail = []
    def agregarEmail(self,unEmail):
        self.__listaEmail.append(unEmail)
    def testEmail(self):
        archivo = open('Ejercicio 1\Datos.csv')
        reader = csv.reader(archivo,delimiter=',')
        for fila in reader:
            id = fila[0]
            dom = fila[1]
            tipoDom = fila[2]
            contraseña = fila[3]
            unEmail = Email(id,dom,tipoDom,contraseña)
            self.agregarEmail(unEmail)
        archivo.close()
    def controlDom(self,dominio,canti):
        i = 0
        for i in range(len(self.__listaEmail)):
            if(self.__listaEmail[i].getDominio() == dominio):
                canti = canti + 1
        return(canti)
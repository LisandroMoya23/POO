from plan import PlanAhorro
import csv
class ManejadorPlan:
    def __init__(self):
        self.__lista = []
    def agregarPlan(self,unPlan):
        self.__lista.append(unPlan)
    def testPlan(self):
        archivo = open('Ejercicio 5\planes.csv')
        reader = csv.reader(archivo,delimiter=';')
        for fila in reader:
            cod = int(fila[0])
            modelo = fila[1]
            version = fila[2]
            importe = float(fila[3])
            unPlan = PlanAhorro(cod,modelo,version,importe)
            self.agregarPlan(unPlan)
        archivo.close
        return
    def modificaValor(self):
        i = 0
        for i in range(len(self.__lista)):
            print(self.__lista[i])
            importe = float(input('Ingrese nuevo valor: '))
            self.__lista[i].actualizaValor(importe)
        return
    def obtenerCuota(self,i):
        cuotas = self.__lista[i].getCuotas()
        valor = self.__lista[i].getValor()
        return ((valor/cuotas)+valor * 0.10)
    def mostrarPlanes(self,importe):
        i = 0
        for i in range(len(self.__lista)):
            if(importe > self.obtenerCuota(i)):
                print(self.__lista[i])
        return
    def obtenerCuotaLicita(self,i):
        cuota = self.obtenerCuota(i)
        cuotasLicitas = PlanAhorro.getCantCuotas() 
        return (cuota * cuotasLicitas)
    def mostrarMontos(self):
        i = 0
        for i in range(len(self.__lista)):
            print("Vehiculo:", self.__lista[i].getModelo())
            print("Monto: $", self.obtenerCuotaLicita(i))
        return
    def cambiarCuotas(self,codigo,cant):
        i = 0
        b = None
        while not b and i in range(len(self.__lista)):
            if(codigo == self.__lista[i].getCod()):
                self.__lista[i].modificaCantCuotas(cant)
                b = True
                print("Se modificaron las cuotas.")
            i+=1
        return
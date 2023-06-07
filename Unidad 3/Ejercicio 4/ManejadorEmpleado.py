from empleado import empleado,planta,externo,contratado
import numpy as np
import csv

class ManejadorEmpleado:
    __dim = int
    __empleados = object
    __actual = int 
    def __init__(self,dim):
        self.__empleados = np.empty(dim,dtype=empleado)
        self.__dim = dim
        self.__actual = 0
    def agregarEmpleado(self,unEmpleado):
        self.__empleados[self.__actual]=unEmpleado
        self.__actual+=1
    def incrementaHoras(self,dni,cant):
        i=0
        while i < self.__actual:
            if isinstance(self.__empleados[i],contratado):
                if(dni == self.__empleados[i].getdni()):
                    self.__empleados[i].incrementaHoras(cant)
                    i=self.__actual
                    print("Las horas fueron incrementadas.")
            i+=1
    def montoTareas(self,tarea):
        i=0
        while i in range(self.__actual):
            if isinstance(self.__empleados[i],externo):
                if(tarea == self.__empleados[i].gettarea()):
                    print("Costo de la tarea: ",self.__empleados[i].getcosto())
            i+=1
    def sueldo(self,empleado):
        if isinstance(self.__empleados,contratado):
                sueldo = self.__empleados.getsueldo()
        if isinstance(self.__empleados,planta):
                sueldo = self.__empleados.getsueldo()
        if isinstance(self.__empleados,externo):
                sueldo = self.__empleados.getsueldo()
        return sueldo
    def ayuda(self):
        print("-- Lista de empleados --")
        for i in range(self.__actual):
            sueldo =  self.sueldo(self.__empleados[i])
            if(sueldo < 150000):
                print("Nombre: ",self.__empleados[i].getnom())
                print("Direccion: ",self.__empleados[i].getdireccion())
                print("DNI: ",self.__empleados[i].getdni())
    def listarsueldos(self):
        print("-- Lista de empleados --")
        for i in range(self.__actual):
            print("Nombre: ",self.__empleados[i].getnom())
            print("Telefono: ",self.__empleados[i].gettelefono())
            print("Sueldo: ${}".format(self.sueldo(self.__empleados[i])))


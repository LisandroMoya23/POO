from Alumnos import Alumno
import numpy as np
import csv
class ManejadorAlumno:
    __cantidad=0
    __dimension=0
    __incremento=5
    def __init__(self,dimension,incremento=8):
        self.__listaalum=np.empty(dimension,dtype=Alumno)
        self.__cantidad=0
        self.__dimension=dimension
        self.__incremento=incremento
        
    def carga_alumnos(self):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__listaalum = np.resize(self.__listaalum,self.__dimension)
        archivo=open("C:\\Users\\lisan\\OneDrive\\2° Año\\Programación Orientada a Objetos\\Unidad 2\\Ejercicio Integrador\\alumnos.csv")
        reader=csv.reader(archivo,delimiter=';')
        i=0
        for fila in reader:
            if i!=0:
                alumnoaux=Alumno(fila[0],fila[1],fila[2],fila[3],fila[4])
                self.__listaalum[self.__cantidad]=alumnoaux
                self.__cantidad+=1
            i+=1
    
    def buscar_alum(self,dni):
        i=0
        while i<self.__cantidad and dni!=self.__listaalum[i].get_dni():
            i+=1
        if i!=self.__cantidad:
            print ("{}       {}".format(self.__listaalum[i].get_dni(),self.__listaalum[i].get_nomap().ljust(17)),end="           ")
        return self.__listaalum[i].get_anio()
            
    def ordenar_lista(self):
        alumnos_ordenados=sorted(self.__listaalum)
        for alumno in alumnos_ordenados:
            alumno.mostrar_datos()
from materiasAprobadas import materiaA
import csv
class ManejadorMateria:
    def __init__(self):
        self.__listamat=[]
        
    def carga_materias(self):
        archivo=open("C:\\Users\\lisan\\OneDrive\\2° Año\\Programación Orientada a Objetos\\Unidad 2\\Ejercicio Integrador\\materiasAprobadas.csv")
        reader=csv.reader(archivo,delimiter=';')
        i=0
        for fila in reader:
            if i!=0:
                alumnoaux=materiaA(fila[0],fila[1].upper(),fila[2],int(fila[3]),fila[4])
                self.__listamat.append(alumnoaux)
            i+=1
            
    def mostrarprom_alumno(self):
        dni=input("Ingrese el dni del alumno ")
        lista_indices=[]
        i=0
        for fila in self.__listamat:
            if fila.get_dni()==dni:
                lista_indices.append(i)
            i+=1 
        if len(lista_indices)==0:
            print ("No se encontró el Alumno buscado")
        else:
            prom=[0,0]
            for cant in range (len(lista_indices)):
                prom[0]+=self.__listamat[lista_indices[cant]].get_nota()                
                if self.__listamat[lista_indices[cant]].get_cond()=='E':
                    if self.__listamat[lista_indices[cant]].get_nota()>=4:
                        prom[1]+=self.__listamat[lista_indices[cant]].get_nota()
                if self.__listamat[lista_indices[cant]].get_cond()=='P':
                    if self.__listamat[lista_indices[cant]].get_nota()>=7:
                        prom[1]+=self.__listamat[lista_indices[cant]].get_nota()
                if self.__listamat[lista_indices[cant]].get_cond()=='X':
                    if self.__listamat[lista_indices[cant]].get_nota()>=6:
                        prom[1]+=self.__listamat[lista_indices[cant]].get_nota()
            print ("El promedio del alumno con aplazos es "+str(prom[0]/len(lista_indices)))
            print ("El promedio del alumno sin aplazos es "+str(prom[1]/len(lista_indices)))
            
    def mostrar_aprobados(self,alumnos):
        materia=input("Ingrese la materia a buscar: ")
        print ("DNI            Apellido y Nombre           Fecha           Nota        Año que cursa")
        for fila in self.__listamat:
            if materia.upper()==fila.get_nomate():
                if fila.get_cond()=='P':
                    if fila.get_nota()>=7:
                        p=alumnos.buscar_alum(fila.get_dni())
                        print("{}      {}           {}".format(fila.get_fecha(),str(fila.get_nota()),p))
                        
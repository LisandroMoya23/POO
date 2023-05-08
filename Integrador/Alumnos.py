class Alumno:
    def __init__(self,dni,ape,nom,carrera,anio):
        self.__dni=dni
        self.__ap=ape
        self.__nom=nom
        self.__carrera=carrera
        self.__aniocar=anio

    def get_dni(self):
        return self.__dni
    
    def get_nomap(self):
        return self.__ap+" "+self.__nom
    
    def get_anio(self):
        return self.__aniocar
    
    def __lt__(self,otro):
        return (self.__aniocar, (self.__ap + self.__nom)) < (otro.get_anio(), (otro.get_nomap()))
    
    def mostrar_datos(self):
        print ("{}, {} {}, {}, {}".format(self.__dni,self.__ap,self.__nom,self.__carrera,self.__aniocar))
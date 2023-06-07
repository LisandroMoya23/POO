class empleado:
    __DNI = ''
    __nombre = ''
    __direccion = ''
    __telefono = ''
    def __init__(self,dni,nom,dir,tele):
        self.__DNI = dni
        self.__nombre = nom
        self.__direccion = dir
        self.__telefono = tele
    def getdni(self):
        return self.__DNI
    def getnom(self):
        return self.__nombre
    def getdireccion(self):
        return self.__direccion
    def gettelefono(self):
        return self.__telefono
    
class planta(empleado):
    __sueldo = float
    __antiguedad = int
    def __init__(self,dni,nom,dir,tele,sueldo,antiguedad):
        super().__init__(empleado)
        self.__sueldo = sueldo
        self.__antiguedad = antiguedad
    def getdni(self):
        return super().getdni()
    def getnom(self):
        return super().getnom()
    def getdireccion(self):
        return super().getdireccion()
    def gettelefono(self):
        return super().gettelefono()
    def getsueldo(self):
        return self.__sueldo + self.__antiguedad * self.__sueldo * 1/100

class contratado(empleado):
    __fechaInicio = ''
    __fechaFinalizacion = ''
    __cantHoras = int
    __valorHora = 1500
    def __init__(self,dni,nom,dir,tele,fechaIni,fechaFin,cantH,valorH):
        super().__init__(empleado)
        self.__fechaInicio = fechaIni
        self.__fechaFinalizacion = fechaFin
        self.__cantHoras = int(cantH)
        self.__valorHora = float(valorH)
    def getdni(self):
        return super().getdni()
    def getnom(self):
        return super().getnom()
    def getdireccion(self):
        return super().getdireccion()
    def gettelefono(self):
        return super().gettelefono()
    def incrementaHoras(self,cant):
        self.__cantHoras+=cant
    def getsueldo(self):
        return self.__cantHoras * self.__valorHora

class externo(empleado):
    __tarea = ''
    __fechaInicio = ''
    __fechaFinalizacion = ''
    __montoViatico = ''
    __costoObra = ''
    __montoSeguro = ''
    def __init__(self,dni,nom,dir,tele,tarea,fechaIni,fechaFin,monto,costo,seguro):
        super().__init__(empleado)
        self.__tarea = tarea
        self.__fechaInicio = fechaIni
        self.__fechaFinalizacion = fechaFin
        self.__montoViatico = float(monto)
        self.__costoObra = float(costo)
        self.__montoSeguro = float(seguro)
    def getdni(self):
        return super().getdni()
    def getnom(self):
        return super().getnom()
    def getdireccion(self):
        return super().getdireccion()
    def gettelefono(self):
        return super().gettelefono()
    def gettarea(self):
        return self.__tarea
    def getcosto(self):
        return self.__costoObra
    def getsueldo(self):
        return self.__costoObra - self.__montoViatico - self.__montoSeguro
       
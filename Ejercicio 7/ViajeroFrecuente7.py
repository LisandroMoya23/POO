class ViajeroFrecuente:
    __num_viajero = ''
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millas_acum = None
    def __init__(self,num,dni,nom,apellido,millas):
        self.__num_viajero = num
        self.__dni = dni
        self.__nombre = nom
        self.__apellido = apellido
        self.__millas_acum = millas
    def __gt__ (self,otroViajero):
        if(self.__millas_acum > otroViajero.getTotalMillas()):
            milla_mayor = self.__millas_acum
        else:
            milla_mayor = otroViajero.getTotalMillas()
        return (milla_mayor)
    def __add__(self,millas):
        return self.__millas_acum + millas
    def __sub__(self,millas):
        return self.__millas_acum - millas
    def __eq__(self,millas):
        return self.__millas_acum == millas
    def getNumViajero(self):
        return(self.__num_viajero)
    def getTotalMillas(self):
        return(int(self.__millas_acum))
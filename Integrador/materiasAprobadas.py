class materiaA:
    def __init__(self,dni,nommat,fecha,nota,aprob):
        self.__dni=dni
        self.__nommate=nommat
        self.__fecha=fecha
        self.__nota=nota
        self.__cond=aprob

    def get_dni(self):
        return self.__dni
    
    def get_nota(self):
        return self.__nota
    
    def get_cond(self):
        return self.__cond
    
    def get_nomate(self):
        return self.__nommate
    
    def get_fecha(self):
        return self.__fecha
    
    def mostrar(self):
        print (self.__dni)
        print (self.__nommate)
        print (self.__fecha)
        print (self.__nota)
        print (self.__cond)
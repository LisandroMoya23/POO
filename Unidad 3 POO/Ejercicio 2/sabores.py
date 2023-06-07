class sabor:
    __idSabor = int
    __ingredientes = ''
    __nombreSabor= ''
    def __init__(self,idSabor,ingredientes,nombreSabor):
        self.__idSabor = int(idSabor)
        self.__ingredientes = ingredientes
        self.__nombreSabor = nombreSabor
    def getnom(self):
        return self.__nombreSabor
    def getid(self):
        return self.__idSabor
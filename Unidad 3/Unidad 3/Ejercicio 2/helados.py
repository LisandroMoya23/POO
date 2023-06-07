class helado:
    __gramos = float
    __precio = float
    __sabores = list
    def __init__(self,gramos,precio,listaS):
        self.__gramos = float(gramos)
        self.__precio = float(precio)
        self.__sabores = listaS
    def muestradatos(self):
        print("Gramos: {}".format(self.__gramos))
        print("Precio: {}".format(self.__precio))
        for i in range(len(self.__sabores)):
            print("{} - {}".format(i+1,self.__sabores[i]))
    def getgramos(self):
        return self.__gramos
    def getprecio(self):
        return self.__precio
    def getsabores(self):
        return self.__sabores
    def añadirSabor(self,lista):
        self.__sabores = lista
    def muestrasabores(self):
        for i in range(len(self.__sabores)):
            print("{}".format(self.__sabores[i]))
from helados import helado
class ManejadorHelados:
    __listaHelados = list
    def __init__(self):
        self.__listaHelados = []
    def agregarHelado(self,gramos,precio,listaS):
        unHelado = helado(gramos,precio,listaS)
        self.__listaHelados.append(unHelado)
    def pedidos(self,listaSabores):
        i=0
        sabor = None
        sabores = []
        while sabor != '0' and i < 4:
            sabor = input('Ingrese sabor del helado, puede ingresar hasta {} sabores y finalizar con 0:'.format(i))
            b = listaSabores.compara(sabor)
            if(b == True):
                sabores.append(sabor)
                i+=1
            elif sabor == False:
                print("Sabor incorrecto.")
        gramos = float(input('Ingrese gramos del helado: '))
        precio = float(input('Ingrese precio del helado: '))
        self.agregarHelado(gramos,precio,sabores)
    def mostrar(self):
        for i in range(len(self.__listaHelados)):
            self.__listaHelados[i].muestradatos()
    def buscasabor(self,sabores,num):
        sabor = sabores.buscaid(num)
        if(sabor != None):
            kg = 0
            for i in range(len(self.__listaHelados)):
                lista = self.__listaHelados[i].getsabores()
                j = 0
                while j < (len(lista)):
                    if(sabor == lista[j]):
                        kg+= self.__listaHelados[i].getgramos() / len(lista)
                        j = len(lista)
                    j+=1 
            print("La cantidad de gramos vendidos del sabor {} es: {}gr".format(sabor,kg))
        else:
            print("El sabor ingresado no existe")
    def muestratipo(self,tipo):
        for i in range(self.__listaHelados):
            if(self.__listaHelados[i].getgramos() == tipo):
                self.__listaHelados[i].muestrasabores()
    def recaudado(self):
        a =0
        b = 0
        c = 0
        d = 0
        e = 0
        for i in range(len(self.__listaHelados)):
            if(self.__listaHelados[i].getgramos() == 100):
                a+= self.__listaHelados[i].getprecio()
            elif(self.__listaHelados[i].getgramos() == 150):
                b+= self.__listaHelados[i].getprecio()
            elif(self.__listaHelados[i].getgramos() == 250):
                c+= self.__listaHelados[i].getprecio()
            elif(self.__listaHelados[i].getgramos() == 500):
                d+= self.__listaHelados[i].getprecio()
            elif(self.__listaHelados[i].getgramos() == 1000):
                e+= self.__listaHelados[i].getprecio()
        print("Recaudado por helado:")
        print("100gr: ",a)
        print("150gr: ",b)
        print("250gr: ",c)
        print("500gr: ",d)
        print("1000gr: ",e)


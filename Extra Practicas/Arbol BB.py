class Nodo:
    def __init__(self,x):
        self.dato = x
        self.izquierda = None
        self.derecha = None

    def getDato(self):
        return self.dato
    def getDer(self):
        return self.derecha
    def getIzq(self):
        return self.izquierda
    def setDato(self,d):
        self.dato = d
    def setDer(self,n):
        self.derecha = n
    def setIzq(self,n):
        self.izquierda = n
    
class ABB:
    cabeza = None
    def __init__(self):
        self.cabeza = None

    def vacia(self):
        return self.cabeza == None

    def insertar(self,dato):
        nodo = Nodo(dato)
        if self.vacia():
            self.cabeza = nodo
            return
        
        aux = self.cabeza
        while aux != None and aux.getDato() != dato:
            ant = aux
            if aux.getDato() < dato:
                aux = aux.getDer()
            else:
                aux = aux.getIzq()
        if aux != None:
            print("El dato ya ha sido ingresado")
        else:
            if ant.getDato() < dato:
                ant.setDer(nodo)
            else:
                ant.setIzq(nodo)

    def grado(self,nodo):
        cant=0
        if nodo.getDer() != None:
            cant+=1
        if nodo.getIzq() != None:
            cant+=1
        return cant

    def suprimir(self,clave):
        if self.vacia():
            print("El arbol esta vacio")
            return
        aux = self.cabeza
        while aux != None and aux.getDato() != clave:
            ant = aux
            if aux.getDato() < clave:
                aux = aux.getIzq()
            else:
                aux = aux.getDer()
        if aux != None:
            if self.grado(aux) == 0:
                if ant.getDato > aux.getDato():
                    ant.setIzq(None)
                else:
                    ant.setDer(None)
                del aux 
            elif self.grado(aux) == 1:
                if ant.getIzq() == None:
                   aux2 = aux.getDer()
                   aux.setDato(aux2.getDato())
                   aux.setDer(None)
                   del aux2
                else:
                    aux2= aux.getIzq()
                    aux.setDato(aux2.getDato())
                    aux.setIzq(None)
                    del aux2
            else:
                aux2 = aux.getIzq()
                while aux2.getDer != None:
                    ant = aux2
                    aux2 = aux2.getDer()
                if aux2 == aux.getIzq():
                    aux.setIzq(None)
                else:
                    aux.setDato(aux2.getDato)
                    aux.setDer(None)
        else:
            print("El elemento a suprimir no se encontro.")

    def buscar(self,dato):
        if self.vacia():
            print("Arbol vacio")
            return
        aux = self.cabeza
        while aux != None and aux.getDato() != dato:
            if aux.getDato() < dato:
                aux = aux.getDer()
            else:
                aux = aux.getIzq()
        if aux != None:
            print("El dato fue encontrado.")
        else:
            print("El dato no fue encontrado.")
    
    def imprimir_sucesores(self,dato):
        if self.vacia():
            print("Arbol vacio")
            return
        aux = self.cabeza
        while aux != None and aux.getDato() != dato:
            if aux.getDato() < dato:
                aux = aux.getDer()
            else:
                aux = aux.getIzq()
        if aux != None:
            self.ImprimirArbol(aux)
        else:
            print("El dato no fue encontrado.")
    
    def ImprimirArbol(self,aux, prefijo="", es_ultimo=True):
        if aux != None:
            print(prefijo, "|__", aux.getDato())
            prefijo += "    " if es_ultimo else "|   "
            self.ImprimirArbol(aux.getIzq(), prefijo, False)
            self.ImprimirArbol(aux.getDer(), prefijo, True)
    
    def hoja(self,dato):
        if self.vacia():
            print("Arbol vacio")
            return
        aux = self.cabeza
        while aux != None and aux.getDato() != dato:
            if aux.getDato() < dato:
                aux = aux.getDer()
            else:
                aux = aux.getIzq()
        if aux == None:
            print("No se encontro.")
        else:
            if aux.getDer() != None or aux.getIzq() != None:
                return False
            else:
                return True
    
    def getNivel(self,clave):
        aux = self.cabeza
        nivel = self.nivelNodo(aux,clave)
        if nivel != None:
            print("Nivel del nodo:",nivel)
        else:
            print("El nodo no se encontro.")

    def nivelNodo(self, nodo, valor, nivel_actual=1):
        if nodo is None:
            return None
        elif valor == nodo.getDato():
            return nivel_actual
        elif valor < nodo.getDato():
            return self.nivelNodo(nodo.getIzq(), valor, nivel_actual + 1)
        else:
            return self.nivelNodo(nodo.getDer(), valor, nivel_actual + 1)
    
    def Contar_Nodos(self):
        nodos = self.ContarNodos(self.cabeza)
        print ("Numero de nodos del Arbol:",nodos)

    def ContarNodos(self,aux):
        if aux == None:
            return 0
        else:
            return 1+self.ContarNodos(aux.getIzq())+self.ContarNodos(aux.getDer())
    
    def alturaArbol(self, nodo):
        if nodo is None:
            return 0
        else:
            altura_izquierda = self.alturaArbol(nodo.getIzq())
            altura_derecha = self.alturaArbol(nodo.getDer())
            return max(altura_izquierda, altura_derecha) + 1

    def obtenerAltura(self):
        return self.alturaArbol(self.cabeza)
    
    def caminos(self,x,z):
        if self.vacia():
            print("Arbol vacio")
            return
        aux = self.cabeza
        while aux != None and aux.getDato() != x:
            if aux.getDato() < x:
                aux = aux.getDer()
            else:
                aux = aux.getIzq()
        if aux != None:
            camino = []
            while aux != None and aux.getDato() != z:
                if aux.getDato() < z:
                    camino.append(aux)
                    aux = aux.getDer()
                else:
                    camino.append(aux)
                    aux = aux.getIzq()
            if aux != None:
                print("Camino:")
                for i in range(camino):
                    print("",camino[i])
            else:
                print("no se encontro a {z}")
        else:
            print("no se encontro a {x}")

    def hijo(self,hijo,padre):
        if padre.getDer() == hijo or padre.getIzq() == hijo:
            return True
        else:
            return False
    
    def padre(self,padre,hijo):
        if padre.getDer() == hijo or padre.getIzq() == hijo:
            return True
        else:
            return False
    def In_Orden(self):
        self.InOrden(self.cabeza)

    def InOrden(self, aux):
        if aux is not None:
            self.InOrden(aux.getIzq())
            print(aux.getDato(), end=" ")
            self.InOrden(aux.getDer())

    def Pre_Orden(self):
        self.PreOrden(self.cabeza)

    def PreOrden(self, aux):
        if aux is not None:
            print(aux.getDato(), end=" ")
            self.PreOrden(aux.getIzq())
            self.PreOrden(aux.getDer())

    def Post_Orden(self):
        self.PostOrden(self.cabeza)

    def PostOrden(self, aux):
        if aux is not None:
            self.PostOrden(aux.getIzq())
            self.PostOrden(aux.getDer())
            print(aux.getDato(), end=" ")
        
            

if __name__ == '__main__':
    Arbol = ABB()
    Arbol.insertar(10)
    Arbol.insertar(20)
    Arbol.insertar(5)
    Arbol.In_Orden()
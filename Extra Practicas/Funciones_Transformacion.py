import numpy as np

class tablaHash:
    __dimension: int
    __tabla: np.ndarray
    __contador: int

#Funciones de Transformacion

    def metodoDivision(self, valor):
        return valor % self.__dimension

    def metodoExtraccionClaves(self, valor): #Explicacion: extrae el ultimo digito de cada numero como clave para la tabla hash
        valor = valor % 100 #Ejemplo: 123 -> 123 % 100 = 23
        return valor % self.__dimension
    
    def metodoPlegado(self, valor): #El consiste en sumar sub_mitades de un numero y luego sacar el modulo de la dimension 
        acumulador = 0

        while valor != 0:
            acumulador += valor % 10
            valor //= 10

        #ejemplo 123 -> 1+2+3 = 6 -> 6 % 149 = 6
        #ejemplo en caso % o // 100 : 123 -> 1+23 = 24 -> 24 % 149 = 24
        return acumulador % self.__dimension

    def metodoCuadradosMedios(self, valor): #Consiste en que te de los valores centrales del digito como clave 
        #print (int(str(valor**2)[1:-1]))
        return int(str(valor**2)[1:-1]) % self.__dimension #Ejemplo: 123 -> 123^2 = 15129 -> 5129 -> 512 % 149 = 65 

    def metodoClavesAlfanumericas(self, valor):
        acumulador = 0

        for i in range(0, len(str(valor))):
            acumulador += ord(str(valor)[i])

        return acumulador % self.__dimension
        
        #ord() -> devuelve el valor unicode de un caracter
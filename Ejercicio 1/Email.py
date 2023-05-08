class Email:
    __idCuenta = ''
    __tipo = ''
    __dominio = ''
    __contraseña = ''
    def __init__(self,id,dom,tipo,contraseña):
        self.__idCuenta = id
        self.__tipo = tipo
        self.__dominio = dom
        self.__contraseña = contraseña
    def retornamail(self):
        return(self.__idCuenta+'@'+self.__dominio+'.'+self.__tipo)
    def getDominio(self):
        return (self.__dominio)
    def ModificaContraseña(self):
        contra = input('Ingrese su contraseña actual: ')
        if(contra == self.__contraseña):
            self.__contraseña = input('Ingrese su nueva contraseña: ')
            print("Contraseña modificada.")
        else:
            print("Contraseña incorrecta.")
        return
    def crearCuenta(self,correo1):
        x = correo1.split('@')
        y = x[1].split('.')
        id = x[0]
        dom = y[0]
        tipo = y[1]
        contraseña = "1234"
        mail2 = Email(id,dom,tipo,contraseña)
        return(mail2)
    def mostrarDatos(self):
        print("Mail: ",self.__idCuenta+'@'+self.__dominio+'.'+self.__tipo)
        print("Contraseña: ",self.__contraseña)
        return
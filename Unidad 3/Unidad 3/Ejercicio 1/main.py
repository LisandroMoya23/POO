from ManejaFacultades import ManejaFacultades

if __name__ == '__main__':
    lista = ManejaFacultades()
    lista.test()
    opc = None
    while (opc != '0'):
        opc = input('''--Menu--
            1) Mostrar informacion de una facultad.
            2) Mostrar informacion de carrera.
            3) Muestra datos.
            0) Terminar con el programa.
            ''')
        if opc == '1':
            cod = (input('Ingrese codigo de carrera: '))
            lista.muestra1(cod)
        elif opc == '2':
            nom = input('Ingrese nombre: ')
            lista.muestra2(nom)
        elif opc == '3':
            lista.muestraDatos()
        elif opc == '0':
            print("Hasta luego :D.")
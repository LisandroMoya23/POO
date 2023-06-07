from ManejadorHelados import ManejadorHelados
from ManejadorSabores import ManejadorSabores

if __name__ == '__main__':
    helados = ManejadorHelados()
    sabores = ManejadorSabores()
    sabores.test()
    opc = None
    while (opc != '0'):
        opc = input('''--Menu--
            1) Registrar helado vendido.
            2) Mostrar top 5 helados.
            3) Mostrar cantidad de gramos vendidos de un helado.
            4) Mostrar sabores vendidos de un tipo de helado.
            5) Mostrar ganancia por cada tipo de helado.
            0) Terminar con el programa.
            ''')
        if opc == '1':
            helados.pedidos(sabores)
            helados.mostrar()
        elif opc =='2':
            helados.top5(sabores)
        elif opc =='3':
            num = int(input("Ingrese numero de sabor: "))
            helados.buscasabor(sabores,num)
        elif opc =='4':
            tipo = float(input('Ingrese tipo de helado: '))
            helados.muestratipo()

from ManejadorEmpleado import ManejadorEmpleado

if __name__ == '__main__':
    dim = int(input('Ingrese dimension del arreglo: '))
    arreglo = ManejadorEmpleado(dim)
    while (opc != '0'):
        opc = input('''--Menu--
            1) Registrar horas.
            2) Total de tareas.
            3) Ayuda Económica.
            4) Calcular sueldo.
            0) Terminar con el programa.
            ''')
        if opc == '1':
            dni = input('Ingrese DNI del empleado:')
            cant = input('Ingrese cantidad de horas del empleado: ')
            arreglo.incrementaHoras(dni,cant)
        if opc =='2':
            tarea = input("Ingrese la tarea: ")
            arreglo.montoTareas(tarea)
        if opc == '3':
            arreglo.ayuda()
        if opc=='4':
            arreglo.listarsueldos()
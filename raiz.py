# raiz

import AsignarSueldos, ClasificarSueldos, VerEstadisticas, ReporteDsueldos

trabajadores = ['Juan Pérez','María García','Carlos López','Ana Martínez','Pedro Rodríguez','Laura Hernández','Miguel Sánchez','Isabel Gómez','Francisco Díaz','Elena Fernández']
diccionariosTrabajadores = []
totalsueldos = 0

opc = '0'
while opc != '5':
    print("###### MENU ######")
    print("1.- Asignar sueldos aleatorios.")
    print("2.- Clasificar sueldos.")
    print("3.- Ver estadísticas.")
    print("4.- Reporte de sueldos.")
    print("5.- Salir.")
    opc = input("Ingrese su opción: ")

    if opc == '1':
        diccionariosTrabajadores = AsignarSueldos.asignarSueldos(trabajadores,diccionariosTrabajadores)
        print('Sueldos asignados.')
        #print(diccionariosTrabajadores)

    elif opc == '2':
        print("\nClasificación de sueldos:")
        totalsueldos, listaTrabajadores = ClasificarSueldos.clasificarSueldos(diccionariosTrabajadores)

    elif opc == '3':
        print("Estadísticas:")
        VerEstadisticas.verEstadisticas(diccionariosTrabajadores, totalsueldos)

    elif opc == '4':
        listaTrabajadores = ReporteDsueldos.reporteDsueldos(diccionariosTrabajadores)

print("Finalizando programa.\nDesarrollado por Leonardo Salgado.\nRUT 16.941.228-6")
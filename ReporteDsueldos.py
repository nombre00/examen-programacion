# reporte de sueldos

import csv


def reporteDsueldos(listaDiccionarios):

    # calculando descuentos de sueldo y sueldo líquido
    for trabajador in listaDiccionarios:
        trabajador['descuentoSalud'] = (trabajador['sueldo'] * 0.07)//1
        trabajador['descuentoAFP'] = (trabajador['sueldo'] * 0.12)//1
        trabajador['sueldoLíquido'] = trabajador['sueldo'] - trabajador['descuentoSalud'] - trabajador['descuentoAFP']

    # imprimiendo
    print("Nombre:       Sueldo Base:    Descuento Salud:   Descuento AFP:   Sueldo Líquido:")
    for trabajador in listaDiccionarios:
        print(f"{trabajador['nombre']}    {trabajador['sueldo']}        {trabajador['descuentoSalud']}           {trabajador['descuentoAFP']}        {trabajador['sueldoLíquido']}")  

    # creando el .csv
    with open('ReporteSueldos.csv','w') as archivo:
        try:
            llaves = listaDiccionarios[0]
        except IndexError:
            llaves = 'nombre', 'sueldo', 'categoríaSueldo', 'descuentoSalud', 'descuentoAFP', 'sueldoLíquido'
        escritor_dict = csv.DictWriter(archivo,fieldnames= llaves)
        escritor_dict.writeheader()
        for trabajador in listaDiccionarios:
            escritor_dict.writerow(trabajador)
    
    """ # imprimiendo el archivo creado
    with open('ReporteSueldos.csv','r') as archivo:
        lector_dict = csv.DictReader(archivo)
        print("             Nombre:  Sueldo: Categoría sueldo:  Descuento Salud:  Descuento AFP:  Sueldo Líquido:")
        for linea in lector_dict:
            print(linea.values()) """
    
    espera = input("Presione ENTER para continuar.")
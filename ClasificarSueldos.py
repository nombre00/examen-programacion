# clasificar sueldos

def clasificarSueldos(listaDisccionarios):
    sueldosBajos = 0
    sueldosMedios = 0
    sueldosAltos = 0
    totalSueldos = 0
    for trabajador in listaDisccionarios:
        if trabajador['sueldo'] < 800000:
            trabajador['categoríaSueldo'] = 'sueldoBajo'
            sueldosBajos += 1
            totalSueldos += trabajador['sueldo']
        elif trabajador['sueldo'] < 2000000:
            trabajador['categoríaSueldo'] = 'sueldoMedio'
            sueldosMedios += 1
            totalSueldos += trabajador['sueldo']
        else:
            trabajador['categoríaSueldo'] = 'sueldoAlto'
            sueldosAltos += 1
            totalSueldos += trabajador['sueldo']
    
    print(f'\nSueldos menores a $800.000 TOTAL: {sueldosBajos}')
    print("Nombre empleado.                     Sueldo.")
    for trabajador in listaDisccionarios:
        if trabajador['categoríaSueldo'] == 'sueldoBajo':
            print(f"{trabajador['nombre']}                      {trabajador['sueldo']}")
    
    print(f'\nSueldos entre $800.000 y $2.000.000 TOTAL: {sueldosMedios}')
    print("Nombre empleado.                     Sueldo.")
    for trabajador in listaDisccionarios:
        if trabajador['categoríaSueldo'] == 'sueldoMedio':
            print(f"{trabajador['nombre']}                      {trabajador['sueldo']}")
    
    print(f'\nSueldos superiores a $2.000.000 TOTAL: {sueldosAltos}')
    print("Nombre empleado.                     Sueldo.")
    for trabajador in listaDisccionarios:
        if trabajador['categoríaSueldo'] == 'sueldoAlto':
            print(f"{trabajador['nombre']}                      {trabajador['sueldo']}")
    
    print(f"\nTotal sueldos: {totalSueldos}")

    espera = input("Presione ENTER para continuar.")

    return totalSueldos, listaDisccionarios
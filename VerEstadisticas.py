# ver estadisticas
import statistics

def verEstadisticas(listaDiccionarios, totalSueldos):
    # sacando el sueldo más alto
    SueldoAlto = 0
    for trabajador in listaDiccionarios:
        if trabajador['sueldo'] > SueldoAlto:
            SueldoAlto = trabajador['sueldo']
    
    #sacando el sueldo más bajo
    SueldoBajo = 3000000
    for trabajador in listaDiccionarios:
        if trabajador['sueldo'] < SueldoBajo:
            SueldoBajo = trabajador['sueldo']
    
    # sacando el promedio de los sueldos
    promedioSueldos = totalSueldos / 10

    # sacando la media geométrica de los sueldos
    listaSueldos = []
    for trabajador in listaDiccionarios:
        listaSueldos.append(trabajador['sueldo'])
    MediaGeométrica = statistics.geometric_mean(listaSueldos)


    # imprimiendo
    print(f"\nSueldo más alto: {SueldoAlto}")
    print(f"Sueldo más bajo: {SueldoBajo}")
    print(f"Promedio de sueldos: {promedioSueldos}")
    print(f"Media geométrica: {MediaGeométrica}")

    espera = input("Presione ENTER para continuar.")
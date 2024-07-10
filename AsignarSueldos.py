# asignar sueldos aleatorios

import random


def asignarSueldos(lista, listaDiccionarios):
    
    for trabajador in lista:
        Trabajador = {}
        sueldo = random.randint(300000, 2500000)
        Trabajador['nombre'] = trabajador
        Trabajador['sueldo'] = sueldo
        listaDiccionarios.append(Trabajador)
    return listaDiccionarios
from math import ceil


def numero_antenas(area, antenas_viejas, tipo):
    if antenas_viejas < 0:
        return "error en los datos"
    if tipo == 'a':
        cobertura = 800
    elif tipo == 'b':
        cobertura = 52900
    elif tipo == 'c':
        cobertura = 7500
    elif tipo == 'd':
        cobertura = 35600
    elif tipo == 'e':
        cobertura = 49800
    else:
        return "error en los datos"
    area_cubierta = antenas_viejas * 3000
    area_por_cubrir = area - area_cubierta
    no_antenas = ceil(area_por_cubrir/cobertura)
    return no_antenas




# tests = [(2584345.04, 17, 'a'), (2918.29, 2, 'e'), (345076.14, 7, 'a'), (182856.1, -1, 'c'), (182856.1, -1, 'z')]
#
# for tupla in tests:
#     print(numero_antenas(*tupla))

while True:
    area = float(input('Inserte el area de la zona: '))
    antenas_viejas = int(input('Inserte el numero de antenas viejas: '))
    tipo = input('Inserte el tipo de antena nueva (en minúsculas): ')

    print(numero_antenas(area, antenas_viejas, tipo))

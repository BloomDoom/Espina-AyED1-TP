'''La siguiente función permite averiguar el día de la semana para una fecha determi-
nada. La fecha se suministra en forma de tres parámetros enteros y la función de-
vuelve 0 para domingo, 1 para lunes, 2 para martes, etc. Escribir un programa para
imprimir por pantalla el calendario de un mes completo, correspondiente a un mes
y año cualquiera basándose en la función suministrada. Considerar que la semana
comienza en domingo.'''

import tp01_ej02_fecha_valida as fv

def diadelasemana(dia,mes,año): #Le falta DOCSTRING y Typehints, insalubre profe!!
    if mes < 3:
        mes = mes + 10
        año = año - 1
    else:
        mes = mes - 2
    siglo = año // 100
    año2 = año % 100
    diasem = (((26*mes-2)//10)+dia+año2+(año2//4)+(siglo//4)-(2*siglo))%7
    if diasem < 0:
        diasem = diasem + 7
    return diasem

def main():
    '''Programa principal'''

    print('='*50)
    print('Bienvenido a tu calendario.')
    print('='*50)

    mes = 0
    while mes < 1 or mes > 12:
        mes = int(input('Ingrese el mes a visualizar (del 1 al 12): '))

    anio = 0
    while anio < 1900 or anio > 2100:
        anio = int(input('Ingrese el año a visualizar (del 1900 al 2100): '))
    
    calendar = []
    for dia in range(1, 32):
        fecha = dia, mes, anio
        if fv.validar_fecha(fecha):
            calendar.append(fecha)

    dias_semana = []
    for i in range(len(calendar)):
        dias_semana.append(diadelasemana(*calendar[i]))

    calendario = list(zip(calendar, dias_semana))

    print('=====CALENDARIO=====')
    for dias in calendario:
        nombre_dia = {0: 'Domingo', 1: 'Lunes', 2: 'Martes', 3: 'Miercoles', 4: 'Jueves', 5: 'Viernes', 6: 'Sabado'}
        print(f'El dia {dias[0][0]} cae {nombre_dia[dias[1]]}')
    print('=====CALENDARIO=====')


if __name__ == '__main__':
    main()
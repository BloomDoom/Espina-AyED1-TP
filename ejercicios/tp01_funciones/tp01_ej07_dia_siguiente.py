'''Escribir una función diasiguiente(dia, mes año) que reciba como parámetro una
fecha cualquiera expresada por tres enteros y calcule y devuelva otros tres enteros
correspondientes el día siguiente al dado. Utilizando esta función sin modificaciones
ni agregados, desarrollar programas que permitan:
a. Sumar N días a una fecha.
b. Calcular la cantidad de días existentes entre dos fechas cualesquiera.'''

import tp01_ej02_fecha_valida as fv

def diasiguiente(fecha: tuple[int, int, int]) -> tuple[int, int, int]:
    '''
    Contrato:
        Esta funcion recibe una fecha valida cualquiera y devuelve la fecha siguiente.
    Precondiciones:
        Recibe un tupla donde sus elementos deben ser enteros en orden dia - mes - año. La fecha debe ser válida.
    Postcondiciones:
        Devuelve una tupla con 3 enteros correspondiente a la fecha siguiente en orden dia - mes - año
    '''

    dia, mes, anio = fecha

    bisiesto = fv.es_bisiesto(anio)

    match mes:
        case 2:
            if bisiesto:
                if dia < 29:
                    return dia + 1, mes, anio
                return 1, 3, anio
            else:
                if dia < 28:
                    return dia + 1, mes, anio
                return 1, 3, anio
        case 12:
            if dia < 31:
                return dia + 1, mes, anio
            return 1, 1, anio + 1
        case 4 | 6 | 9 | 11:
            if dia < 30:
                return dia + 1, mes, anio
            return 1, mes + 1, anio
        case _:
            if dia < 31:
                return dia + 1, mes, anio
            return 1, mes + 1, anio

def sumar_dias(fecha: tuple[int, int, int], n: int) -> tuple[int, int, int]:
    '''
    Contrato:
        Esta funcion recibe una fecha valida cualquiera y los dias a sumarle, devuelve la fecha posterior en n dias.
    Precondiciones:
        Recibe 2 parametros; una tupla de enteros que deben estar en orden dia - mes - año, y, un entero 0 o mayor. La fecha debe ser válida.
    Postcondiciones:
        Devuelve una tupla con 3 enteros correspondiente a la fecha objetivo en orden dia - mes - año.
    '''

    assert n >= 0, 'Los dias a sumar debe ser 0 o mayor.'
    assert fv.validar_fecha(fecha), 'La fecha debe ser válida'

    for _ in range(n):
        fecha = diasiguiente(fecha)
    return fecha

def calcular_dias_entre_fechas(fecha1: tuple[int, int, int], fecha2: tuple[int, int, int]) -> int:
    '''
    Contrato:
        Esta función recibe dos fechas válidas, devuelve la cantidad de días entre ambas.
    Precondiciones:
        Recibe 2 parámetros; 2 tuplas de enteros que deben estar en orden dia - mes - año. La fecha del primer parámetro no puede ser mayor que la fecha del segundo parámetro. La fechas deben ser válidas.
    Postcondiciones:
        Devuelve un entero correspondiente a los dias entre ambas fechas.
    '''

    assert fv.validar_fecha(fecha1) and fv.validar_fecha(fecha2), 'Las fechas deben ser válidas'
    assert fecha1[::-1] <= fecha2[::-1], 'La primer fecha debe ser menor o igual que la segunda fecha recibida como parámetro'

    contador = 0

    while fecha1 != fecha2:
        fecha1 = diasiguiente(fecha1)
        contador += 1
    return contador

def menu() -> None:
    '''Menu de opciones'''
    print('='*50)
    print('MENU')
    print('='*50)
    print('1. Sumar días a una fecha')
    print('2. Saber cuantos días hay entre 2 fechas')
    print('0. Salir')

def ingresar_fecha() -> tuple[int, int, int]:
    '''
    Contrato:
        Pide al usuario que ingrese una fecha en orden dia - mes - año.
    Precondiciones:
        Esta función NO recibe parámetros.
    Postcondiciones:
        Devuelve una tupla de 3 enteros, correspondientes a dia - mes - año
    '''
    dia = int(input('Ingrese el dia: '))
    mes = int(input('Ingrese el mes: '))
    anio = int(input('Ingrese el año: '))
    return dia, mes, anio


def main() -> None:
    '''Programa principal'''

    op = ''
    while op != '0':
        menu()
        op = input('Ingrese opción: ')
        

        if op == '1':
            fecha = ingresar_fecha()

            while not fv.validar_fecha(fecha):
                print('Ingrese una fecha válida.')
                fecha = ingresar_fecha()

            n = int(input('Ingrese los dias a sumar: '))
            n_fecha = sumar_dias(fecha, n)
            print(f'La fecha obtenida es {n_fecha[0]}/{n_fecha[1]}/{n_fecha[2]}')

        elif op == '2':
            fecha1 = ingresar_fecha()
            fecha2 = ingresar_fecha()
            
            while not fv.validar_fecha(fecha1):
                print('Ingrese una fecha válida.')
                fecha1 = ingresar_fecha()

            while not fv.validar_fecha(fecha2):
                print('Ingrese una fecha válida.')
                fecha2 = ingresar_fecha()

            n = calcular_dias_entre_fechas(fecha1, fecha2)
            print(f'Hay {n} día/s entre las fechas dadas.')
    print('Saliendo del programa ...')
            
if __name__ == "__main__":
    main()
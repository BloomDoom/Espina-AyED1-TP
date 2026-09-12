'''Escribir una función diasiguiente(dia, mes año) que reciba como parámetro una
fecha cualquiera expresada por tres enteros y calcule y devuelva otros tres enteros
correspondientes el día siguiente al dado. Utilizando esta función sin modificaciones
ni agregados, desarrollar programas que permitan:
a. Sumar N días a una fecha.
b. Calcular la cantidad de días existentes entre dos fechas cualesquiera.'''

import tp01_ej02_fecha_valida as fv

def diasiguiente(dia: int, mes: int, anio: int) -> tuple[int, int, int]:
    '''
    Contrato:
        Esta funcion recibe una fecha valida cualquiera y devuelve la fecha siguiente.
    Precondiciones:
        Parametros deben ser enteros en orden dia - mes - año. La fecha debe ser válida.
    Postcondiciones:
        Devuelve una tupla con 3 enteros correspondiente a la fecha siguiente en orden dia - mes - año
    '''
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
    assert fv.validar_fecha(*fecha), 'La fecha debe ser válida'

    for _ in range(n):
        fecha = diasiguiente(*fecha)
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

    assert fv.validar_fecha(*fecha1) and fv.validar_fecha(*fecha2), 'Las fechas deben ser válidas'
    assert fecha1[::-1] <= fecha2[::-1], 'La primer fecha debe ser menor o igual que la segunda fecha recibida como parámetro'

    contador = 0

    while fecha1 != fecha2:
        fecha1 = diasiguiente(*fecha1)
        contador += 1
    return contador

def main() -> None:
    '''Programa principal'''


if __name__ == "__main__":
    main()
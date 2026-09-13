'''Desarrollar una función que reciba tres números enteros positivos correspondientes
al día, mes, año de una fecha y verifique si corresponden a una fecha válida. Debe
tenerse en cuenta la cantidad de días de cada mes, incluyendo los años bisiestos.
Devolver True o False según la fecha sea correcta o no. Realizar también un
programa para verificar el comportamiento de la función.'''

def validar_fecha(fecha: tuple[int, int, int]) -> bool:
    '''Contrato: Recibe 3 int correspondientes a dia, mes y anio. Verifica que sean una fecha valida.
        Precondiciones: Primer argumento 'dia' entre 1 y 31, segundo argumento 'mes' entre 1 y 12 y tercer argumento 'anio' entre -10_000 y 10_000.
        Postcondiciones: True si la fecha es valida, False si no lo es.'''
    dias = [n for n in range(1, 32)]
    meses = [n for n in range(1, 13)]
    anios = [n for n in range(-10_000, 10_001)]

    dia, mes, anio = fecha

    if dia not in dias or mes not in meses or anio not in anios:
        return False

    bisiesto = es_bisiesto(anio)

    if dia < 29 or (dia < 30 and bisiesto):
        return True
    if dia == 30 and mes in [4, 6, 9, 11]:
        return True
    if dia == 31 and mes in [1, 3, 5, 7, 8, 10, 12]:
        return True

    return False

def es_bisiesto(anio: int) -> bool:
    ''' 
        Contrato: Verifica si el anio es bisiesto o no.
        Precondiciones: Que el numero sea un anio real.
        Postcondiciones: True si es anio bisiesto, False si no lo es.
    '''
    return anio % 400 == 0 or (anio % 4 == 0 and anio % 100 != 0)
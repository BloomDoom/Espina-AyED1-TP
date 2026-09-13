'''Desarrollar una función que reciba tres números enteros positivos correspondientes
al día, mes, año de una fecha y verifique si corresponden a una fecha válida. Debe
tenerse en cuenta la cantidad de días de cada mes, incluyendo los años bisiestos.
Devolver True o False según la fecha sea correcta o no. Realizar también un
programa para verificar el comportamiento de la función.'''

def validar_fecha(fecha: tuple[int, int, int]) -> bool:
    '''
    Contrato:
        Recibe 3 int correspondientes a dia, mes y año. Verifica que sean una fecha válida.
    Precondiciones:
        Primer argumento 'dia' entre 1 y 31, segundo argumento 'mes' entre 1 y 12 y tercer argumento 'anio' entre -10_000 y 10_000.
    Postcondiciones:
        True si la fecha es válida, False si no lo es.
    '''
    dias = [n for n in range(1, 32)]
    meses = [n for n in range(1, 13)]
    anios = [n for n in range(0, 2222)]

    dia, mes, anio = fecha

    if dia not in dias or mes not in meses or anio not in anios:
        return False

    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ultimo_dia = dias_por_mes[mes - 1]

    if mes == 2 and es_bisiesto(anio):
        ultimo_dia = 29

    return dia <= ultimo_dia

def es_bisiesto(anio: int) -> bool:
    ''' 
    Contrato:
        Verifica si el año es bisiesto o no.
    Precondiciones:
        Que el numero sea un año real.
    Postcondiciones:
        True si es año bisiesto, False si no lo es.
    '''
    return anio % 400 == 0 or (anio % 4 == 0 and anio % 100 != 0)
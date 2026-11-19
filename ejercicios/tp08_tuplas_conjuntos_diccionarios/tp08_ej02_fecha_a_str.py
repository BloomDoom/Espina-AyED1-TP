"""
Escribir una función que reciba como parámetro una tupla conteniendo una fecha
(día,mes,año) y devuelva una cadena de caracteres con la misma fecha expresada
en formato extendido. La función debe contemplarse que el año se ingrese en dos
dígitos, los que serán interpretados según un año de corte definido dentro del
programa. Cualquier año mayor que éste se considerará del siglo pasado. Por
ejemplo, si el año de corte fuera 30, la función devuelve "12 de Octubre de 2030"
para (12,10,30). Pero si la tupla fuera (25, 12, 31) devolverá "25 de Diciembre de
1931". Si el año se ingresa en cuatro dígitos el año de corte no será tenido en
cuenta. Escribir también un programa para ingresar los datos, invocar a la función y
mostrar el resultado.
"""
import datetime as dt



def ingresar_fecha() -> tuple[int, int, int]:
    """
    Contrato:
        - Permite que el usuario ingrese una fecha por teclado.

    Precondiciones:
        - No recibe parámetros.

    Postcondiciones:
        - Devuelve una tupla en orden dia, mes, año.
    """
    while True:
        while True:
            try:
                dia = int(input('Ingrese el dia: '))
                if 0 < dia < 32:
                    break
            except ValueError:
                print('Ingrese un dia válido en dígitos.')

        while True:
            try:
                mes = int(input('Ingrese el mes: '))
                if 0 < mes < 13:
                    break
            except ValueError:
                print('Ingrese un mes válido en dígitos.')

        while True:
            try:
                anio = int(input('Ingrese el año: '))
                if 0 < anio < 9999:
                    break
            except ValueError:
                print('Ingrese un año válido en dígitos.')

        try:
            dt.date(anio, mes, dia)
            return dia, mes, anio
        
        except ValueError:
            print('No es una fecha válida, intente nuevamente.')


def fecha_a_texto(fecha: tuple[int,int,int]) -> str:
    """
    Contrato:
        - Recibe una fecha en formato tupla: dia, mes año.
        - La procesa y crea un str.
        - Ejemplo: (12, 12, 2012) -> 12 de Diciembre de 2012
        - Contempla recibir años de 4 y 2 dígitos.
        - Si el año es de 2 dígitos, el corte se hace en el año 30.
        - Ejemplo: (12, 12, 30) -> 12 de Diciembre de 2030
        - Ejemplo: (12, 12, 31) -> 12 de Diciembre de 1931

    Precondiciones:
        - La fecha debe ser válida.

    Postcondiciones:
        - Devuelve en formato texto una fecha.
    """

    meses = (
        'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',
        'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
    )
    corte = 30

    dia, mes, anio = fecha

    if 9 < anio < 100:
        if anio > corte:
            return f'{dia} de {meses[mes-1]} de 19{anio}.'
        return f'{dia} de {meses[mes-1]} de 20{anio}.'
    return f'{dia} de {meses[mes-1]} de {anio}.'


def main() -> None:
    """
    Programa para ingresar los datos, invocar a la función y
    mostrar el resultado.
    """
    fecha = ingresar_fecha()
    fecha_str = fecha_a_texto(fecha)
    print(fecha_str)


if __name__ == '__main__':
    main()
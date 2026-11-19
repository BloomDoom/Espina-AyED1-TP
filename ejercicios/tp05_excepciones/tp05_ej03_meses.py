"""
Desarrollar una función que devuelva una cadena de caracteres con el
nombre del mes cuyo número se recibe como parámetro. Los nombres de los
meses deberán obtenerse de una lista de cadenas de caracteres
inicializada dentro de la función.
Devolver una cadena vacía si el número de mes es inválido. La detección
de meses inválidos deberá realizarse a través de excepciones.
"""


def nombre_mes(n: int) -> str:
    """
    Contrato:
        - Dado un número, devuelve el nombre del mes correspondiente.

    Precondiciones:
        - Un entero; número de mes.

    Postcondiciones:
        - Un string con nombre del mes.
        - Un string vacío si el número de mes es inválido.
    """

    meses = [
        'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio',
        'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'
        ]

    try:
        if n < 1:
            raise IndexError
        return meses[n - 1]

    except IndexError:
        return ''


def main() -> None:
    """Programa principal."""

    while True:
        try:
            n = int(input('Ingrese el número del mes: '))
            break

        except ValueError:
            print('1000: Error en la carga de dato, intente con un número.')

    mes = nombre_mes(n)

    if not mes:
        print('El número ingresado no corresponde a un mes válido.')
    else:
        print(f'El número ingresado corresponde al mes: {mes}')


if __name__ == '__main__':
    main()
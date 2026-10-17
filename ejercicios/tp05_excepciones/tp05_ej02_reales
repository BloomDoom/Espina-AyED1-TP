"""
Realizar una función que reciba como parámetros dos cadenas de
caracteres conteniendo números reales, sume ambos valores y devuelva el
resultado como un número real. Devolver -1 si alguna de las cadenas no
contiene un número válido, utilizando manejo de excepciones para
detectar el error.
"""


def sumar_reales_desde_cadena(s1: str, s2: str) -> float:
    """
    Contrato:
        - Dadas dos cadenas, las convierte a reales y
          devuelve la suma de ambos.

    Precondiciones:
        - Str; cadena conteniendo un número real.
        - Str; cadena conteniendo un número real.

    Postcondiciones:
        - Un flotante; suma de los números convertidos de las cadenas.
        - -1 en caso de que alguna cadena no contenga un número válido.
    """

    cadenas: tuple[str, str] = (s1, s2)
    reales: list[float] = []

    for cadena in cadenas:
        try:
            reales.append(float(cadena))
        except ValueError:
            return -1

    return sum(reales)


def main() -> None:
    """Programa principal."""

    n = sumar_reales_desde_cadena('21.50', '19')

    if n == -1:
        print('Un texto no se pudo convertir a número.')
    else:
        print(f'La suma de los reales convertidos de los textos es: {n}')


if __name__ == '__main__':
    main()
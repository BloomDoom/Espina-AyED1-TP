"""
La raíz cuadrada de un número puede obtenerse mediante la función sqrt() del
módulo math. Escribir un programa que utilice esta función para calcular la raíz
cuadrada de un número cualquiera ingresado a través del teclado. El programa
debe utilizar manejo de excepciones para evitar errores si se ingresa un número
negativo.
"""

from math import sqrt



def raiz(n: float) -> float:
    """
    Contrato:
        - Dado un número n, se calcula su raíz cuadrada y se devuelve.

    Precondiciones:
        - El número n no puede ser negativo.

    Postcondiciones:
        - Se retorna un float.
    """

    if n < 0:
        raise ValueError('El número a calcular no puede ser negativo.')
    
    return sqrt(n)


def main() -> None:
    """Programa principal."""
    while True:
        try:
            n = float(input('Ingrese un número: '))
            break
        except ValueError:
            print('Intente utilizando dígitos.')

    try:
        salida = raiz(n)

    except ValueError as e:
        print(e)

    else:
        print(f'La raíz cuadrada de {n} es: {round(salida, 2)}')

    finally:
        print('Gracias por venir, vuelva prontos!')



if __name__ == '__main__':
    main()
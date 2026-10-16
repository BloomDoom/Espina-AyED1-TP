"""
Desarrollar una función para ingresar a través del teclado un número natural. La
función rechazará cualquier ingreso inválido de datos utilizando excepciones y
mostrará la razón exacta del error. Controlar que se ingrese un número, que ese
número sea entero y que sea mayor que 0, mostrando un mensaje con la razón
exacta del error en caso necesario. Devolver el valor ingresado cuando éste sea
correcto. Escribir también un programa que permita probar el correcto funciona-
miento de la misma.
"""

def ingresar_natural() -> int:
    """
    Contrato:
        - Permite únicamente ingresar un número natural por teclado.

    Precondiciones:
        - No recibe parámetros.

    Postcondiciones:
        - Un entero; número de orden natural.
    """

    while True:
        try:
            n = int(input('Ingrese un número natural: '))
            if n > 0:
                return n
            print('Ingrese un número entero mayor a 0.')

        except ValueError:
            print('1000: Error de tipo de dato. Ingrese un número.')

def main() -> None:
    """Programa principal."""
    
    n = ingresar_natural()

    print(f'El número ingresado es: {n}')


if __name__ == '__main__':
    main()
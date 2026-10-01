'''
Escribir una función que reciba como parámetro un número entero entre 0 y 3999 y
lo convierta en un número romano, devolviéndolo en una cadena de caracteres. ¿En
qué cambiaría la función si el rango de valores fuese diferente?
'''


def entero_a_romano(n: int) -> str:
    """
    Contrato:
        - Recibe un entero entre 0 y 3999, y lo devuelve en números romanos.

    Precondiciones:
        - Un entero entre 0 y 3999 inclusive

    Postcondiciones:
        - Una cadena; número romano equivalente al entero recibido.
    """
    s: str = ''
    numeros_romanos = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    letras_romanas = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'LX', 'X', 'IX', 'V', 'IV', 'I']
    i = 0
    
    while n > 0:
        for _ in range(n // numeros_romanos[i]):
            s += letras_romanas[i]
            n -= numeros_romanos[i]
        i += 1

    return s


def main() -> None:
    """Programa principal."""
    print('='*50)
    print('Bienvenidos a la conversión romana!')
    
    while True:
        try:
            n = int(input('\nIngrese un número: '))
            if 0 <= n <= 3999:
                break
            print('El número debe estar entre 0 y 3999.')
        except ValueError:
            print('Error en la carga de datos.')

    print(f'\nEl número {n}, los romanos lo escribian así: {entero_a_romano(n)}')
    print('='*50)


if __name__ == '__main__':
    main()
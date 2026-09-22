'''
Las siguientes matrices responden distintos patrones de relleno. Desarrollar funcio-
nes que generen cada una de ellas sin intervención humana y escribir un programa
que las invoque e imprima por pantalla. El tamaño de las matrices debe estable-
cerse como N x N, donde N se ingresa a través del teclado.

a:  1 0 0 0     b:  0 0 0 27   c:   4 0 0 0
    0 3 0 0         0 0 9 0         3 3 0 0
    0 0 5 0         0 3 0 0         2 2 2 0
    0 0 0 7         1 0 0 0         1 1 1 1

d:  8 8 8 8     e:  0 1 0 2     f:  0 0 0 1
    4 4 4 4         3 0 4 0         0 0 3 2
    2 2 2 2         0 5 0 6         0 6 5 4
    1 1 1 1         7 0 8 0         10 9 8 7

g:  1 2 3 4     h:  1 2 4 7     i:  1 2 6 7
    12 13 14 5      3 5 8 11        3 5 8 13
    11 16 15 6      6 9 12 14       4 9 12 14
    10 9 8 7        10 13 15 16     10 11 15 16
'''
def e(m: list[list[int]]) -> None:
    """
    Contrato:
        - Agrega valores enteros según patrón.
    
    Precondiciones:
        - Una matriz de enteros.
    
    Postcondiciones:
        - Modifica la matriz recibida.
        - No retorna nada.
    """
    long = len(m)
    contador = 1

    for i in range(long):
        for j in range(long):
            if (i + j) % 2:
                contador += 1


def matriz_de_ceros() -> list[list[int]]:
    """Crea una matriz N x N con valores '0' en cada celda."""
    while True:
        try:
            n = int(input('Ingrese el tamaño de la matriz: '))
            if n > 0:
                return [[0] * n for _ in range(n)]
            else:
                print('Ingrese un número válido.')
        except ValueError:
            print('Error en la carga de datos, debe ingresar un número entero.')


def a(m: list[list[int]]) -> None:
    """
    Contrato:
        - Agrega valores enteros en la diagonal principal de una matriz.
    
    Precondiciones:
        - Una matriz de enteros.

    Postcondiciones:
        - Modifica la matriz recibida.
        - No retorna nada.
    """

    impares = [n for n in range(len(m)*2) if n%2]
    j = 0

    for i in range(len(m)):
        m[i][i] = impares[j]
        j += 1


def b(m: list[list[int]]) -> None:
    """
    Contrato:
        - Agrega valores enteros en la diagonal secundaria de una matriz.
    
    Precondiciones:
        - Una matriz de enteros.

    Postcondiciones:
        - Modifica la matriz recibida.
        - No retorna nada.
    """
    n = len(m)

    for i in range(n):
        m[i][n-1-i] = 3 ** (n-1-i)


def c(m: list[list[int]]) -> None:
    """
    Contrato:
        - Agrega valores enteros hasta su número de fila inclusive en una matriz dada.
    
    Precondiciones:
        - Una matriz de enteros.
    
    Postcondiciones:
        - Modifica la matriz recibida.
        - No retorna nada.
    """

    n = len(m)

    for i in range(n):
        for j in range(i+1):
            m[i][j] = n - i


def d(m: list[list[int]]) -> None:
    """
    Contrato:
        - Agrega valores enteros según patrón.
    
    Precondiciones:
        - Una matriz de enteros.
    
    Postcondiciones:
        - Modifica la matriz recibida.
        - No retorna nada.
    """
    n = (len(m) - 1) ** 2

    for i in range(n):
        for j in range(n):
            m[i][j] = 2 ** (n-1-i)


def main() -> None:
    print('Pendiente a terminar.')


if __name__ == '__main__':
    main()
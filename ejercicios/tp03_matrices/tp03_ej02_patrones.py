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
def i(m: list[list[int]]) -> None:
    """
    Contrato:
        - Agrega valores enteros según patrón (Rellena por diagonales haciendo zigzag).
    
    Precondiciones:
        - Una matriz de enteros.
    
    Postcondiciones:
        - Modifica la matriz recibida.
        - No retorna nada.
    """
    n = len(m)
    contador = 1
    cant_diag = n*2 - 1
    bajando = True
    
    for diag in range(cant_diag):
        bajando = not bajando
        for i in range(n):
            j = diag - i
            if 0 <= j < n:
                if bajando:
                    m[i][j] = contador
                    contador += 1
                else:
                    m[j][i] = contador
                    contador += 1



def h(m: list[list[int]]) -> None:
    """
    Contrato:
        - Agrega valores enteros según patrón (Rellena por diagonales).
    
    Precondiciones:
        - Una matriz de enteros.
    
    Postcondiciones:
        - Modifica la matriz recibida.
        - No retorna nada.
    """
    n = len(m)
    contador = 1
    cant_diag = n*2 - 1

    for diag in range(cant_diag):
        for i in range(n):
            j = diag - i
            if 0 <= j < n:
                m[i][j] = contador
                contador += 1


def g(m: list[list[int]]) -> None:
    """
    Contrato:
        - Agrega valores enteros según patrón (MATRIZ ESPIRALADA).
    
    Precondiciones:
        - Una matriz de enteros.
    
    Postcondiciones:
        - Modifica la matriz recibida.
        - No retorna nada.
    """
    contador = 1
    n = len(m)
    espirales = n//2 + 1
    reset = n*4 - 4
    ultimo = reset
    arriba = 0
    abajo = n - 1
    izq = 0
    der = n - 1
    

    for veces in range(espirales):
        for i in range(veces, n + veces):
            for j in range(veces, n + veces):
                if i == arriba:
                    m[i][j] = contador
                    contador += 1
                elif i == abajo:
                    m[i][-(j + 1)] = contador
                    contador += 1
                else:
                    if j == izq:
                        m[i][j] = ultimo
                        ultimo -= 1
                    elif j == der:
                        m[i][j] = contador
                        contador += 1
        arriba += 1
        abajo -= 1
        izq += 1
        der -= 1
        n -= 2
        contador = reset + 1
        reset += n*4 - 4
        ultimo = reset



def f(m: list[list[int]]) -> None:
    """
    Contrato:
        - Agrega valores enteros según patrón.
    
    Precondiciones:
        - Una matriz de enteros.
    
    Postcondiciones:
        - Modifica la matriz recibida.
        - No retorna nada.
    """
    contador = 1
    for i in range(len(m)):
        for j in range(i + 1):
            if j <= i:
                m[i][-(j + 1)] = contador
                contador += 1


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
                m[i][j] = contador
                contador += 1


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
    n = len(m)

    for i in range(n):
        for j in range(n):
            m[i][j] = 2 ** (n-1-i)


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


def mostrar(m: list[list[int]]) -> None:
    '''
    Contrato:
        - Recibe una matriz y la imprime fila por fila

    Precondiciones:
        - Una lista de listas.

    Precondiciones:
        - Imprime por pantalla las filas de la matriz.
    '''
    for r in m:
        print(r)



def main() -> None:
    """Programa principal."""
    print('='*50)
    print('Bienvenido a mi programa.')
    print()
    print('En esta sección vamos a jugar con los patrones de las matrices.')
    print()
    m = matriz_de_ceros()
    print('Patrones a ver:')
    print('\na:  1 0 0 0     b:  0 0 0 27   c:   4 0 0 0\n'
            '    0 3 0 0         0 0 9 0         3 3 0 0\n'
            '    0 0 5 0         0 3 0 0         2 2 2 0\n'
            '    0 0 0 7         1 0 0 0         1 1 1 1\n'
        '\n'
        'd:  8 8 8 8     e:  0 1 0 2     f:  0 0 0 1\n'
        '    4 4 4 4         3 0 4 0         0 0 3 2\n'
        '    2 2 2 2         0 5 0 6         0 6 5 4\n'
        '    1 1 1 1         7 0 8 0         10 9 8 7\n'
        '\n'
        'g:  1 2 3 4     h:  1 2 4 7     i:  1 2 6 7\n'
        '    12 13 14 5      3 5 8 11        3 5 8 13\n'
        '    11 16 15 6      6 9 12 14       4 9 12 14\n'
        '    10 9 8 7        10 13 15 16     10 11 15 16')

    seguir = True
    while seguir:
        print()
        patron = input('Ingrese el patrón a ver (enter para salir): ')
        print()
        
        if patron == '':
            break
        
        if patron in 'abcdefghi':
            if patron == 'a':
                a(m)
                mostrar(m)
            elif patron == 'b':
                b(m)
                mostrar(m)
            elif patron == 'c':
                c(m)
                mostrar(m)
            elif patron == 'd':
                d(m)
                mostrar(m)
            elif patron == 'e':
                e(m)
                mostrar(m)
            elif patron == 'f':
                f(m)
                mostrar(m)
            elif patron == 'g':
                g(m)
                mostrar(m)
            elif patron == 'h':
                h(m)
                mostrar(m)
            elif patron == 'i':
                i(m)
                mostrar(m)
        else:
            print('Opción incorrecta.')
            

    print('Saliendo. . . . . . . . . . . . . . . .')
    print('='*50)


if __name__ == '__main__':
    main()
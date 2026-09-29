'''
Una fábrica de bicicletas guarda en una matriz la cantidad de unidades producidas
en cada una de sus plantas durante una semana. De este modo, cada columna re-
presenta el día de la semana y cada fila a una de sus fábricas. Ejemplo:
            (Lunes)     (Martes)    (Miércoles)  (Jueves)    (Viernes)   (Sábado)
                0           1           2           3           4           5
(Fábrica 1)     23          150         20          120         25          150
(Fábrica 2)     40          75          80          0           80          35
( . . . )   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .
(Fábrica n)     80          80          80          80          80          80

Se solicita:

a. Crear una matriz con datos generados al azar para N fábricas durante una
semana, considerando que la capacidad máxima de fabricación es de 150
unidades por día y puede suceder que en ciertos días no se fabrique nin-
guna.

b. Mostrar la cantidad total de bicicletas fabricadas por cada fábrica.

c. Cuál es la fábrica que más produjo en un solo día (detallar día y fábrica).

d. Cuál es el día más productivo, considerando todas las fábricas combinadas.

e. Crear una lista por comprensión que contenga la menor cantidad fabricada
por cada fábrica.
'''
from random import randint as ri


def randomizar(n: int) -> list[list[int]]:
    """
    Contrato:
        - Crea una matriz de enteros donde el valor de cada celda ronda entre 0 y 150 inclusive.

    Precondiciones:
        - Un entero; determina la cantidad de filas de la matriz.

    Postcondiciones:
        - Una matriz con 'n' filas y 6 columnas (idx 0 = lunes /.../ idx 5 = sabado)
    """

    return [[ri(0, 150) for j in range(6)] for i in range(n)]


def cant_fabrica(m: list[list[int]], r: int) -> int:
    """
    Contrato:
        - Cuenta los valores de una fila 'r' y los devuelve.
    
    Precondiciones:
        - Una matriz de enteros.
        - Un entero donde r < len(m)

    Postcondiciones:
        - Un entero; suma de los valores de una fila 'r' de 'm'.
    """
    return sum(m[r])


def mayor_valor(m: list[list[int]]) -> tuple[int, int]:
    """
    Contrato:
        - Recibe una matriz de enteros y busca el mayor valor para devolver su ubicación.
        - En caso de empate de mayor valor, devuelve el primero e ignora empates.

    Precondiciones:
        - Matriz de enteros.
        - La matriz no puede estar vacía.
    
    Postcondiciones:
        - Una tupla de enteros; primer elemento es la fila y el segundo la columna.
        - Si la matriz esta vacía, tira IndexError.
    """

    maximo = m[0][0]
    row = 0
    col = 0
    for r in range(len(m)):
        for c in range(len(m[r])):
            if m[r][c] > maximo:
                maximo = m[r][c]
                row = r
                col = c
    return row, col


def produccion_total_dia(m: list[list[int]], col: int) -> int:
    """
    Contrato:
        - Suma los valores de una columna 'col' de la matriz recibida.

    Precondiciones:
        - Una matriz de enteros.
        - Un entero; columna válida de la matriz.

    Postcondiciones:
        - Un entero; suma de los valores de la columna 'col'.
    """
    return sum(r[col] for r in m)


def menor_cantidad_fabrica(m: list[list[int]]) -> list[int]:
    """
    Contrato:
        - Busca y devuelve la primer menor cantidad por fábrica.

    Precondiciones:
        - Una matriz de enteros.

    Postcondiciones:
        - Una lista de enteros; los primer menor valor de cada lista 'm[r]'.
    """
    return [min(r) for r in m]


def menu() -> None:
    """Menu de opciones."""
    print('='*50)
    print('1. Mostrar la cantidad total de bicicletas fabricadas por cada fábrica.')
    print('2. Mostrar fábrica que más produjo en un solo día.')
    print('3. Saber que dia es el más productivo considerando todas las fábricas.')
    print('4. Saber la menor cantidad producida por cada fábrica.')
    print('0. Salir.')
    print('='*50)


def main() -> None:
    """Programa principal."""
    print('/'*50)
    print('Bienvenido a tu programa de gestión de bicicletas.')
    while True:
        try:
            n = int(input('\nIngrese la cantidad de fábricas: '))
            if n > 0:
                break
            print('La cantidad de fábricas debe ser mayor a 0.')
        except ValueError:
            print('Error en la carga de datos numéricos.')

    m = randomizar(n)
    dias = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado']

    op = ''
    while op != '0':
        menu()
        op = input('Ingrese opción: ')
        if op == '1':
            for r in range(len(m)):
                total = cant_fabrica(m, r)
                print(f'\nLa cantidad total de la fábrica número {r+1} es de {total}.')

        elif op == '2':
            fabrica, dia = mayor_valor(m)
            print(f'\nLa fábrica que más produjo en un solo día es la número {fabrica + 1}, el día {dias[dia]}.')

        elif op == '3':
            max_total = produccion_total_dia(m, 0)
            idx = 0
            for c in range(len(m[0])):
                total = produccion_total_dia(m, c)
                if total > max_total:
                    max_total = total
                    idx = c
            print(f'\nEl día mas productivo es {dias[idx]}, con una producción total de {max_total}.')

        elif op == '4':
            lista_menores = menor_cantidad_fabrica(m)
            for i in range(len(lista_menores)):
                print(f'\nLa fábrica número {i+1} tiene como menor producción {lista_menores[i]}.')

        else:
            print('Ingrese una opción válida.')

    print('\nSaliendo del programa. . . . . .')
    print('/'*50)


if __name__ == '__main__':
    main()
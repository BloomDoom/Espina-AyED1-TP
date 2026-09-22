'''
Desarrollar un programa que permita realizar reservas en una sala de cine de N
filas con M butacas por cada fila. Desarrollar las siguientes funciones y utilizarlas
en un mismo programa:
mostrar_butacas: Mostrará por pantalla el estado de cada una de las butacas
del cine. Esta función deberá ser invocada antes de que se realice la reserva, y
se volverá a invocar luego de la misma con los estados actualizados.
reservar: Deberá recibir una matriz y la butaca seleccionada, y actualizará la
sala en caso de estar disponible dicha butaca. La función devolverá True/False
si logró o no reservar la butaca.
cargar_sala: Recibirá una matriz como parámetro y la cargará con valores
aleatorios para simular una sala con butacas ya reservadas.
butacas_libres: Recibirá como parámetro la matriz y retornará cuántas buta-
cas desocupadas hay en la sala.
butacas_contiguas: Buscará la secuencia más larga de butacas libres conti-
guas en una misma fila y devolverá las coordenadas de inicio de la misma.
'''

from random import randint as ri


def butacas_contiguas(m: list[list[bool]]) -> tuple[tuple[int, int], int]:
    """
    Contrato:
        - Explora la matriz buscando la mayor cantidad de butacas libres, al encontrarla, devuelve su coordenada inicial y la cantidad.

    Precondiciones:
        - Una matriz de booleanos.

    Postcondiciones:
        - Una tupla donde el primer elemento es una tupla de 2 enteros; coordenadas de matriz en orden fila, columna.
        - Segundo elemento un entero; cantidad de butacas libres contiguas.
    """
    contiguas = 0
    idx: list[int] = []
    max_contiguas = 0
    inicio = ()
    for r in range(len(m)):
        for c in range(len(m[r])):
            if m[r][c]:
                contiguas = 0
                idx.clear()
            else:
                contiguas += 1
                idx.append(c)

                if contiguas > max_contiguas:
                    max_contiguas = contiguas
                    inicio = r, idx[0]

    return (inicio, max_contiguas)


def butacas_libres(m: list[list[bool]]) -> int:
    """
    Contrato:
        - Cuenta cuantas butacas libres hay en la matriz, retorna un entero con ese valor.

    Precondiciones:
        - Recibe una matriz de booleanos.

    Postcondiciones:
        - Retorna un entero; un contador de datos 'False' en la matriz.
    """

    out = 0
    for r in m:
        out += r.count(False)
    return out


def cargar_sala(m: list[list[bool]]) -> None:
    """
    Contrato:
        - Carga la matriz recibida con datos booleanos aleatorios

    Precondiciones:
        - Recibe una matriz de booleanos.
    
    Postcondiciones:
        - Modifica la matriz con datos booleanos aleatorios.
    """
    
    for r in m:
        for i in range(len(r)):
            r[i] = bool(ri(0, 1))


def reservar(m: list[list[bool]], t: tuple[int, int]) -> bool:
    """
    Contrato:
        - Reserva una butaca en el cine. Si el dato de la matriz es False, lo cambia a True y devuelve True.

    Precondiciones:
        - Recibe una matriz de booleanos.
        - Recibe una tupla con la posición de la butaca; t(row, col).

    Postcondiciones:
        - Devuelve True si efectuó el cambio.
        - Devuelve False si la butaca ya estaba reservada.
    """
    row, col = t

    if m[row][col]:
        return False
    m[row][col] = True
    return True


def _ingresar_dimension() -> int:
    """
    Contrato:
        - Permite ingresar un entero igual o mayor a 0 ingresado por el usuario

    Precondiciones:
        - No recibe parámetros.

    Postcondiciones:
        - Devuelve un entero positivo o 0.
    """
    while True:
        try:
            n = int(input('Ingrese la dimensión requerida: '))
            if n >= 0:
                return n
            print('El valor ingresado debe ser igual o mayor a 0.')
        except ValueError:
            print('Error al cargar dato.')


def mostrar_butacas(m: list[list[bool]]) -> None: 
    """Imprime la matriz en pantalla"""
    for r in m:
        print(' '.join('X' if c else 'O' for c in r))


def menu() -> None:
    """Menu de opciones"""
    print('='*50)
    print('1. Ver butacas libres.')
    print('2. Reservar butacas.')
    print('3. Ver la mayor cantidad de butacas libres contiguas.')
    print('4. Mostrar sala.')
    print('0. Salir.')


def main() -> None:
    """Programa principal."""
    print('='*50)
    print('Bienvenido a tu programa de gestion de sala de cine.')
    print('A continuación, ingrese la cantidad de filas de butacas:')
    row = _ingresar_dimension()
    print('Ahora, ingrese la cantidad de butacas que tiene en las filas.')
    col = _ingresar_dimension()
    m = [[c for c in range(col)] for r in range(row)]
    cargar_sala(m)
    print('Su sala de cine: ')
    mostrar_butacas(m)

    while True:
        menu()
        try:
            op = input('Ingrese opción válida: ')
        except ValueError:
            print('Error al cargar dato')

        if op == '1':
            libres = butacas_libres(m)
            print(f'Hay {libres} butacas libres en la sala.')

        elif op == '2':
            print('Ingrese la fila de la butaca a reservar: ')
            r = _ingresar_dimension()

            while not 1 < r < len(m):
                r = _ingresar_dimension()

            print('Ingrese la columna de la butaca a reservar: ')
            c = _ingresar_dimension()

            while not 1 < c < len(m[r]):
                c = _ingresar_dimension()

            reservado = reservar(m, (r - 1, c - 1))
            if reservado:
                print('Se ha reservado la butaca con éxito.')
            else:
                print('La butaca no está libre.')

        elif op == '3':
            t1, cant = butacas_contiguas(m)
            row, col = t1
            print(f'La cantidad máxima de butacas libres contiguas es de {cant}.')
            print(f'Y su posición en la sala es; Fila: {row+1}, Columna {col+1}')

        elif op == '4':
            mostrar_butacas(m)

        elif op == '0':
            print('Saliendo del programa. . .')
            break

        else:
            print('Opción incorrecta.')


if __name__ == '__main__':
    main()
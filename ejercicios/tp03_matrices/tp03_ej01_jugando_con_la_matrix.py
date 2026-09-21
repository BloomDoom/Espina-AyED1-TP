'''
Desarrollar cada una de las siguientes funciones y escribir un programa que permi-
ta verificar su funcionamiento, imprimiendo la matriz luego de invocar a cada fun-
ción:
a. Cargar números enteros en una matriz de N x N, ingresando los datos desde
teclado.
b. Ordenar en forma ascendente cada una de las filas de la matriz.
c. Intercambiar dos filas, cuyos números se reciben como parámetro.
d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
e. Trasponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji)
f. Calcular el promedio de los elementos de una fila, cuyo número se recibe como
parámetro.
g. Calcular el porcentaje de elementos con valor impar en una columna, cuyo nú-
mero se recibe como parámetro.
h. Determinar si la matriz es simétrica con respecto a su diagonal principal.
i. Determinar si la matriz es simétrica con respecto a su diagonal secundaria.
j. Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo
una lista con los números de las mismas.
NOTA: El valor de N debe leerse por teclado. Las funciones deben servir cualquiera
sea el valor ingresado.
'''

def crear_matriz_cuadrada() -> list[list[int]]:
    """
    Crea una matriz N x N y la devuelve, N se ingresa por teclado.
    
    Precondiciones:
        - No recibe parámetros.
        - El usuario debe saber que es una matriz :D

    Postcondiciones:
        - Devuelve una matriz (lista de listas) de tamaño N ingresado por el usuario.
    """

    while True:
        try:
            n = int(input('Ingrese ancho y largo de la matriz: '))
            if n > 0:
                return [[] for _ in range(n)]
            print('La matriz tiene que tener dimensiones mayores a 0.')
        except ValueError:
            print('Error en la carga de datos.')


def _pedir_entero() -> int:
    """Se le solicita al usuario que ingrese un número entero."""

    while True:
        try:
            return int(input('Ingrese un número entero: '))

        except ValueError:
            print('Error en la carga de datos.')


def cargar_matriz_cuadrada(m: list[list[int]]) -> None:
    """
    Contrato:
        - Permite ingresar números enteros a una matriz recibida.

    Precondiciones:
        - Una lista de listas de enteros.

    Postcondiciones:
        - Agrega valores enteros a una matriz cuadrada vacía.
    """

    print('Empecemos a llenar la matriz.')
    print('Empezaremos por la primera fila y terminaremos con la última.')

    for r in m:
        for _ in range(len(m)):
            r.append(_pedir_entero())


def orden_ascendente(m: list[list[int]]) -> None:
    """
    Contrato:
        - Ordena cada fila de la matriz de manera ascendente.

    Precondiciones:
        - Una lista de listas de enteros.

    Postcondiciones:
        - Modifica el orden de los elementos de las listas internas de la lista.
    """

    for r in m:
        r.sort()


def intercambiar_filas(m: list[list[int]], r1: int, r2: int) -> None:
    """
    Contrato:
        - Permite intercambiar 2 filas entre sí.
    
    Precondiciones:
        - Recibe la matriz a trabajar.
        - Recibe 2 números enteros que deben ser índices de filas válidas de la matriz; 0 <= r < len(m).
    
    Postcondiciones:
        - Intercambia posiciones de las filas recibidas como parámetro.
        - No retorna nada.
    """
    m[r1], m[r2] = m[r2], m[r1]


def intercambiar_columnas(m: list[list[int]], c1: int, c2: int) -> None:
    """
    Contrato:
        - Permite intercambiar 2 columnas entre sí.
    
    Precondiciones:
        - Recibe la matriz a trabajar.
        - Recibe 2 números enteros donde 0 <= c1 <= len(m[r]) lo mismo para c2.
    
    Postcondiciones:
        - Intercambia los valores entre las columnas recibidas como parámetro.
        - No retorna nada.
    """

    for r in m:
        r[c1], r[c2] = r[c2], r[c1]


def transponer_matriz(m: list[list[int]]) -> None:
    """
    Contrato:
        - Dada una matriz recibida, se traspone sobre si misma.

    Precondiciones:
        - La matriz debe ser cuadrada.

    Postcondiciones:
        - La matriz recibida se modifica, se traspone sobre si misma.
    """

    for i in range(len(m)):
        for j in range(i + 1, len(m[i])):
            m[i][j], m[j][i] = m[j][i], m[i][j]


def calcular_promedio_fila(m: list[list[int]], r: int) -> float:
    """
    Contrato:
        - Calcula el promedio de los elementos de una fila, cuyo número se recibe como parámetro.

    Precondiciones:
        - Recibe la matriz a trabajar
        - Recibe un entero haciendo referencia a la fila de la matriz a trabajar; 0 <= r < len(m).

    Postcondiciones:
        - Devuelve un flotante; promedio de los enteros de la fila recibida.
    """
    if len(m[r]) == 0:
        raise ZeroDivisionError('No se puede calcular el promedio de una fila vacía.')

    return sum(m[r]) / len(m[r])


def calcular_porcentaje_impares(m: list[list[int]], c: int) -> float:
    """
    Contrato:
        - Calcular el porcentaje de elementos con valor impar en una columna, cuyo número se recibe como parámetro.

    Precondiciones:
        - Recibe una matriz de enteros.
        - Recibe una columna válida para todas las filas dentro de la matriz.

    Postcondiciones:
        - Retorna un flotante; porcentaje de impares dentro de una columna 'c'.
    """
    impares = [r for r in m if r[c] % 2]

    return (len(impares) * 100) / len(m)


def simetrica_principal(m: list[list[int]]) -> bool:
    """
    Contrato:
        - Determina si una matriz es simétrica respecto a su diagonal principal.

    Precondiciones:
        - Recibe una matriz de enteros.

    Postcondiciones:
        - Devuelve True si es simétrica.
        - Devuelve False si no lo es.
    """
    for r in range(len(m)):
        for c in range(len(m[r])):
            if m[r][c] != m[c][r]:
                return False
    return True


def simetrica_secundaria(m: list[list[int]]) -> bool:
    """
    Contrato:
        - Determina si una matriz es simétrica respecto a su diagonal secundaria.

    Precondiciones:
        - Recibe una matriz de enteros.

    Postcondiciones:
        - Devuelve True si es simétrica.
        - Devuelve False si no lo es.
    """
    n = len(m)

    for r in range(n):
        for c in range(n - 1 - r):
            if m[r][c] != m[n - 1 - c][n - 1 - r]:
                return False
    return True


def _es_capicua(m: list[list[int]], c: int) -> bool:
    """
    Contrato:
        - Determina si una columna de una matriz dada es capicúa.

    Precondiciones:
        - Recibe una matriz de enteros.
        - Una entero; referencia a una columna de la matriz.

    Postcondiciones:
        - Devuelve True si la columna de la matriz es capicúa.
        - Devuelve False si existe un contraejemplo.
    """
    col = [r[c] for r in m]

    return col == col[::-1]


def columnas_capicuas(m: list[list[int]]) -> list[int]:
    """
    Contrato:
        - Devuelve los índices de las columnas capicúas de una matriz.

    Precondiciones:
        - Una matriz de enteros.
        - Todas las filas deben tener el mismo largo; len(m[0]) debe ser representativo.

    Postcondiciones:
        - Una lista de enteros; cada entero es el índice de una columna capicúa en la matriz dada
    """
    return [c for c in range(len(m[0])) if _es_capicua(m, c)]


def menu() -> None:
    "Menú de opciones."
    print('='*50)
    print('1. Ordenar en forma ascendente cada una de las filas de la matriz.')
    print('2. Intercambias 2 filas.')
    print('3. Intercambias 2 columnas.')
    print('4. Trasponer la matriz sobre sí misma.')
    print('5. Calcular el promedio de los elementos de una fila.')
    print('6. Calcular el porcentaje de elementos con valor impar en una columna.')
    print('7. Saber si la matriz es simétrica respecto a su diagonal principal.')
    print('8. Saber si la matriz es simétrica respecto a su diagonal secundaria.')
    print('9. Saber que columnas son palíndromos.')
    print('0. Salir.')
    print('='*50)


def main() -> None:
    """Programa principal."""
    print('Veremos todas las funciones creadas.')
    print('Primero creamos una matriz cuadrada.')
    m = crear_matriz_cuadrada()
    print(m)
    print('Luego le cargamos datos.')
    cargar_matriz_cuadrada(m)
    print(m)
    print('Ahora se viene el menú de opciones. . .')
    
    while True:
        menu()
        op = input('Ingrese una opción válida: ')

        if op == '1':
            orden_ascendente(m)

        elif op == '2':
            print('Ingrese el índice de las filas a intercambiar: ')
            intercambiar_filas(m, _pedir_entero(), _pedir_entero())

        elif op == '3':
            print('Ingrese el índice de las columnas a intercambiar: ')
            intercambiar_columnas(m, _pedir_entero(), _pedir_entero())

        elif op == '4':
            transponer_matriz(m)

        elif op == '5':
            print('Ingrese la fila a calcular: ')
            print(calcular_promedio_fila(m, _pedir_entero()))

        elif op == '6':
            print('Ingrese la columna a calcular: ')
            print(calcular_porcentaje_impares(m, _pedir_entero()))

        elif op == '7':
            print(simetrica_principal(m))

        elif op == '8':
            print(simetrica_secundaria(m))

        elif op == '9':
            print('Las columnas palíndromas son: ')
            print(columnas_capicuas(m))

        elif op == '0':
            print('Saliendo del programa . . .')
            break

        print(m)


if __name__ == '__main__':
    main()
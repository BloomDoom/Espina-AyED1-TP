'''
Escribir funciones para:
a. Generar una lista de N números aleatorios del 1 al 100. El valor de N se ingresa
a través del teclado.
b. Recibir una lista como parámetro y devolver True si la misma contiene algún
elemento repetido. La función no debe modificar la lista.
c. Recibir una lista como parámetro y devolver una nueva lista con los elementos
únicos de la lista original, sin importar el orden.
Combinar estas tres funciones en un mismo programa.
'''

from random import randint as ri


def generar_lista(n: int) -> list[int]:
    """
    Crea una lista aleatoria de n elementos enteros y la retorna.
    
    Precondiciones:
        - Un número entero que sera la longitud de la lista a generar.
        - 'n' no puede ser negativo.

    Postcondiciones:
        - Retorna una lista que contiene números aleatorios del 1 al 100.
    """

    return [ri(1, 100) for x in range (n)]


def elemento_repetido(lista: list[int]) -> bool:
    """
    Recibe una lista y determina si algún elemento dentro de la misma se encuentra repetido.

    Precondiciones:
        - La lista tiene que ser de enteros.

    Postcondiciones:
        - True si existe un elemento repetido.
        - False si no existen elementos repetidos.
    """
    return any(lista.count(x) > 1 for x in lista)


def elementos_unicos(lista: list[int]) -> list[int]:    ### Enunciado: "... sin importar el orden." sugestiona el uso de sets. ☺
    """
    Recibe una lista y devuelve una lista con elementos únicos (sin repetir).

    Precondiciones:
        - La lista debe estar vacia o tener números enteros.

    Postcondiciones:
        - Retorna otra lista donde estan los elementos de la lista recibida sin repetición.
        - No modifica la lista original.
        - No se garantiza el mismo orden a la lista original.
    """

    return list(set(lista))


def main() -> None:
    """Programa principal."""

    print('='*50)
    print('Bienvenido a este maravilloso programa.')
    print('='*50)
    print()
    print('A continuación, vamos a jugar con listas en Python.')
    print('Le voy a pedir que ingrese un número siendo este la cantidad de elementos enteros de una lista.')
    print()
    n = int(input('Ingrese un número positivo: '))
    lista = generar_lista(n)
    print()

    op = ''
    while op != '0':
        print('='*50)
        print('MENU')
        print('='*50)
        print()
        print('1. Ver si la lista tiene elementos repetidos.')
        print('2. Eliminar repetidos en la lista.')
        print('0. Salir.')
        print()
        op = input('Ingrese opción: ')

        if op == '1':
            if elemento_repetido(lista):
                print('La lista tiene elementos repetidos‼')
                print(lista)
                print()
            else:
                print('La lista no tiene elemntos repetidos.')
                print(lista)
                print()

        elif op == '2':
            seteo = elementos_unicos(lista)
            print('La lista sin repetidos se vería así:')
            print(seteo)
            print()

        elif op == '0':
            break

        print('¿Quiere seguir jugando?')
        print('1. Si.')
        print('0. No.')
        seguir = int(input('Ingrese opción: '))

        if not seguir:
            op = '0'

    print('Saliendo del programa ...')

if __name__ == '__main__':
    main()
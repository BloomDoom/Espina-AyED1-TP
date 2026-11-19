"""
Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas
son recibidas en dos tuplas, por ejemplo: (3, 4) y (5, 4). La función devuelve True
o False. Escribir también un programa para verificar su comportamiento. Considerar
el uso de conjuntos para resolver este ejercicio.
"""

from random import choice as ch



def _crear_domino() -> set[tuple[int, int]]:
    """
    Contrato:
        - Crea un juego de dominó.

    Precondiciones:
        - Saber jugar al dominó.

    Postcondiciones:
        - Un juego completo de dominó.
        - Cada ficha es una tupla con 2 enteros.
        - El juego entero es una tupla de tuplas.
    """

    return set((n,m) for n in range(7) for m in range(n, 7))

def si_encajan(ficha1: tuple[int, int], ficha2: tuple[int, int]) -> bool:
    """Determina si 2 fichas de encajan entre sí."""
    
    return bool(set(ficha1) & set(ficha2))


def main() -> None:
    """
    Programa principal.
    Dado un juego de domino, se calcula si 2 fichas encajan.
    """
    juego_domino = _crear_domino()
    
    ficha1 = ch(tuple(juego_domino))
    ficha2 = ch(tuple(juego_domino))
    print('Las fichas elegidas son:')
    print(ficha1)
    print(ficha2)
    if si_encajan(ficha1, ficha2):
        print('Las fichas encajan!')
    else:
        print('Lo lamento, las fichas no encajan.')


if __name__ =='__main__':
    main()
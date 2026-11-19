"""
Escribir una función buscarclave() que reciba como parámetros un diccionario y un
valor, y devuelva una lista de claves que apunten ("mapeen") a ese valor en el dic-
cionario. Comprobar el comportamiento de la función mediante un programa apro-
piado.
"""
from random import randint as ri



def buscar_clave(dicc: dict, valor) -> list:
    """
    Contrato:
        - Dado un dict, se alistan las claves que apunten al valor recibido.

    Precondiciones:
        - El valor tiene que ser coherente con el dict.

    Postcondiciones:
        - Una lista con las claves que coindicieron con el valor recibido.
    """

    salida: list = []

    for clave in dicc.keys():
        if dicc[clave] == valor:
            salida.append(clave)
    return salida


def main() -> None:
    """Programa principal."""
    print('Crearemos un diccionario con 10 claves y 10 valores entre 1 y 10.')
    dicc = {n:ri(100, 110) for n in range(1, 11)}
    print('Diccionario:')
    print(dicc)
    print()
    print('El valor a buscar es:')
    valor = dicc[ri(1, 10)]
    print(valor)
    lista = buscar_clave(dicc, valor)
    print()
    print('Las claves que coindicen con el valor son:')
    print(lista)
    print('¡Adios!')


if __name__ == '__main__':
    main()
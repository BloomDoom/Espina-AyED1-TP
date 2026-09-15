'''
Escribir una función que reciba una lista de números enteros como parámetro y la
normalice, es decir que todos sus elementos deben sumar 1.0, respetando las pro-
porciones relativas que cada elemento tiene en la lista original. Desarrollar también
un programa que permita verificar el comportamiento de la función. Por ejemplo,
normalizar([1, 1, 2]) debe devolver [0.25, 0.25, 0.50].
'''

def normalizar_lista_enteros(lista: list[int]) -> list[float]:
    """
    Normaliza la lista de enteros recibida manteniendo sus proporciones.

    Precondiciones:
        - La lista debe ser numérica.

    Postcondiciones:
        - Se modifica la lista original.
    """

    total = sum(lista)

    for i, elem in enumerate(lista):
        proporcion = elem / total
        lista[i] = proporcion

    return lista

def main() -> None:
    """Programa principal."""
    print(normalizar_lista_enteros([1, 1, 2, 4]))

if __name__ == '__main__':
    main()
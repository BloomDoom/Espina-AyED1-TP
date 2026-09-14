'''
Eliminar de una lista de números enteros aquellos valores que se encuentren en
una segunda lista. Imprimir la lista original, la lista de valores a eliminar y la lista
resultante. La función debe modificar la lista original sin crear una copia modificada.
'''

def eliminar_enteros_en_lista(lista1: list[int], lista2: list[int]) -> None:

    eliminar = [x for x in lista1 if x in lista2]

    print('La lista original:')
    print(lista1)
    print()
    print('Los valores a remover:')
    print(eliminar)
    print()

    for i, elem in enumerate(eliminar):
        lista1.remove(elem)

    print('Lista resultante:')
    print(lista1)


def main() -> None:
    """"Funcion principal."""
    print('='*50)
    print('Bienvenido.')

    lista1 = [x*2 for x in range(10)]
    lista2 = [x*3 for x in range(10)]

    eliminar_enteros_en_lista(lista1, lista2)

    print('Fin.')
    print('='*50)

if __name__ == '__main__':
    main()
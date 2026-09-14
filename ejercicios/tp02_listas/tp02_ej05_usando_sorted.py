'''
Escribir una función que reciba una lista como parámetro y devuelva True si la lista
está ordenada en forma ascendente o False en caso contrario. Por ejemplo,
ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar
además un programa para verificar el comportamiento de la función.
'''

def es_ordenada(lista: list) -> bool:
    """
    Determina si una lista de elementos homogeneos está ordenada.

    Precondiciones:
        - Se recibe una lista.
        - La lista debe ser de elementos comparables entre sí.

    Postcondiciones:
        - True si está ordenada de manera ascendente.
        - False si no lo está.
    """

    return lista == sorted(lista)

def main() -> None:
    """Función pricipal."""

    lista_str = ['a', 'A', 'B', 'b', 'Jeje', 'Tutankamon', 'xD']
    lista2_str = ['Az', 'a', 'az', 'b1', 'zebra']
    lista_num = [x for x in range(10)]
    lista2_num = [x - 51 for x in range(12, 120, 5)]

    print(f'Es la lista {lista_str} ordenada?')
    print(es_ordenada(lista_str))
    print()

    
    print(f'Es la lista {lista2_str} ordenada?')
    print(es_ordenada(lista2_str))
    print()
    
    print(f'Es la lista {lista_num} ordenada?')
    print(es_ordenada(lista_num))
    print()
    
    print(f'Es la lista {lista2_num} ordenada?')
    print(es_ordenada(lista2_num))
    print()


if __name__ == '__main__':
    main()
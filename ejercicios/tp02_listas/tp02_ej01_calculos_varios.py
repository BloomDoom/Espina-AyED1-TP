'''
Desarrollar cada una de las siguientes funciones y escribir un programa que per-
mita verificar su funcionamiento imprimiendo la lista luego de invocar a cada fun-
ción:
a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elemen-
tos también será un número al azar de dos dígitos.
b. Calcular y devolver el producto de todos los elementos de la lista anterior.
c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar
se ingresa desde el teclado y la función lo recibe como parámetro. No utilizar
listas auxiliares.
d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas
auxiliares. Un ejemplo de lista capicúa es [50, 17, 91, 17, 50].
'''

from random import randint as ri


def cargar_rand_list() -> list[int]:
    '''
    Crea y carga una lista de enteros de cantidad aleatoria que a su vez sus elementos son enteros aleatorios.

    Contrato:
        - Carga una lista con números de 4 dígitos.
        - La lista tiene longitud de entre 10 y 99 elementos inclusive.
    
    Precondiciones:
        - Esta función no recibe parámetros.

    Postcondiciones:
        - Una lista de entre 10 y 99 elementos, donde sus elementos son enteros de 4 dígitos.
    '''

    return [ri(1000, 9999) for _ in range(ri(10, 99))]


def producto_lista(lista: list[int]) -> int:
    '''
    Multiplica todos los elementos de una lista de enteros

    Contrato:
        - Agarra elemento i y lo multiplica por elemento i + 1 hasta llegar a N siendo N el último elemento.

    Precondiciones:
        - Debe recibir una lista de enteros.

    Postcondiciones:
        - Un entero siendo este el producto del total de los elementos de la lista.
    '''
    salida = 1
    for elem in lista:
        salida *= elem

    return salida


def eliminar_valor_en_lista(lista: list[int], valor: int) -> None:
    '''
    Elimina un valor de una lista las veces que aparezca.

    Contrato:
        - Elimina valores de una lista modificando la misma.
    
    Precondiciones:
        - Recibe una lista de enteros y un entero referencia al valor a eliminar de la lista.

    Postcondiciones:
        - Elimina todas las apariciones del valor en la lista.
    '''

    while valor in lista:
        lista.remove(valor)

    return


def es_capicua(lista: list[int]) -> bool:
    '''
    Determina si una lista de números enteros es capicúa. O en otra palabras, analiza su capicutividad. ### ☺
    
    Contrato:
        - Una lista es capicúa cuando se lee de igual manera en ambos sentidos (es simétrica).
        - Una lista vacia se considera capicúa.

    Precondiciones:
        - Recibe una lista de enteros a evaluar.

    Postcondiciones:
        - True si la lista es simétrica.
        - False si la lista no es simétrica.
    '''
    for i in range(len(lista)//2):
        if lista[i] != lista[-(i + 1)]:
            return False
    return True


def main() -> None:
    """Programa principal. """

    print('='*50)
    print('Bienvenido a tu programa de cálculos vários.')
    lista = cargar_rand_list()
    print()
    print(lista)
    print()
    print('Ahora el producto de toda la lista es:')
    producto = producto_lista(lista)
    print(producto)
    print()
    n = int(input('Ingrese un número a eliminar de la lista: '))
    eliminar_valor_en_lista(lista, n)
    print()
    print('La lista quedó: ')
    print(lista)
    print()
    print('Ahora vamos a ver si la lista es capicúa.')
    capicua = es_capicua(lista)

    if capicua:
        print('La lista es capicúa‼')
    else:
        print('La lista no es capicúa ..')
    print(lista)
    print('='*50)

if __name__ == '__main__':
    main()
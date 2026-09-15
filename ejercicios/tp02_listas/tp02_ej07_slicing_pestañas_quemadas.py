'''
Intercalar los elementos de una lista entre los elementos de otra. La intercalación
deberá realizarse exclusivamente mediante la técnica de rebanadas y no se creará
una lista nueva sino que se modificará la primera. Por ejemplo, si lista1 = [8, 1, 3]
y lista2 = [5, 9, 7], lista1 deberá quedar como [8, 5, 1, 9, 3, 7]. Las listas pueden
tener distintas longitudes.
'''

def intercalar_elementos(lista1: list, lista2: list) -> None:
    """
    Intercala elementos de 2 listas utilizando slicing

    Precondiciones:
        - Recibe 2 listas.

    Postcondiciones:
        - Modifica la primer lista recibida.
    """
    print('='*100)
    print('En esta seccion vamos a documentar el proceso profe, me queme las pestañas resolviéndolo.. ☺')
    print()
    print('Primero calculo la menor longitud de las 2 listas: ')
    n  = min(len(lista1), len(lista2))  ###Busco el minimo para poder usar slicing con step y que no rompa.
    print(n)
    print()

    print('Luego inserto n elementos en n posición para agrandar la lista y que pueda caber la rebanda de la segunda lista que se va a intercalar: ')
    lista1[n:n] = [n] * n               ### Inserto en n posicion n cantidad de elementos sirviendo estos de contenedor de los elementos a insertar.
    print(lista1)
    print()

    print('Luego reubico los primeros N elementos de la propia lista en posiciones pares: ')
    lista1[:n*2:2] = lista1[:n]         ### Reacomodo los primeros n elementos de la propia lista en posiciones pares.
    print()

    print('Ahora inserto los elementos intercalables de la segunda lista:')
    lista1[1:n*2:2] = lista2[:n]        ### Acomodo los primeros n elementos de la segunda lista en posiciones impares.
    print(lista1)
    print()

    print('Y por último, agrego al final de la lista los elementos sobrantes de la segunda lista si los hubiera: ')
    lista1[len(lista1):] = lista2[n:]   ### Agrego al final de la lista los elementos restantes de la segunda lista. Si no existen elementos, no se agrega nada.
    print(lista1)
    print('='*100)

    
def main() -> None:
    """Programa principal."""

    lista1 = [1, 3, 5, 7, 9, 10]
    lista2 = [2, 4, 6, 8,]

    print('='*100)
    print('Listas a intercalar: ')
    print(lista1)
    print(lista2)

    intercalar_elementos(lista1, lista2)


if __name__ == '__main__':
    main()
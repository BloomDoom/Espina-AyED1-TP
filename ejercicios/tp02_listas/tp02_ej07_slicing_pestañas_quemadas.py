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

    print(lista1)
    print(lista2)

    len1 = len(lista1)     
    lista1[len1:] = [0 for x in lista2]     ### Primero agrando la lista para que tenga todos los slots necesarios.
    lista1[::2] = lista1[:len1]             ### Segundo reubico los elementos de la lista en índices pares.
    lista1[1::2] = lista2                   ### Tercero ubico los elementos de la lista a insertar en índices impares.


    print(lista1)


intercalar_elementos([1,3,5,7,9], [2,4,6,8,10])
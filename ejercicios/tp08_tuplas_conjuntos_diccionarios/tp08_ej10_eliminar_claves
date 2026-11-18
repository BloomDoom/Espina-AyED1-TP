"""
Desarrollar una función eliminarclaves() que reciba como parámetros un diccionario
y una lista de claves. La función debe eliminar del diccionario todas las claves
contenidas en la lista, devolviendo el diccionario modificado y un número entero
que represente la cantidad de claves eliminadas. Desarrollar también un programa
para verificar su comportamiento.
"""

def eliminar_claves(dicc: dict[int, int], claves: list[int]) -> tuple[dict[int, int], int]:
    """
    Contrato:
        - Dado un diccionario y una lista de claves, elimina del diccionario 
        las claves contenidas en la lista

    Precondiciones:
        - El diccionario y las claves deben coincidir en tipo para que funcione.

    Postcondiciones:
        - Devuelve el mismo diccionario modificado.
    """
    contador = 0
    for clave in claves:
        if clave in dicc:
            del dicc[clave]
            contador += 1

    return dicc, contador


def main() -> None:
    """Programa principal."""

    dicc = {m:4*m for m in range(1, 13)}
    claves = [n for n in range(0, 30, 3)]
    
    print('Diccionario en cuestión:')
    print(dicc)
    print('Claves a eliminar:')
    print(claves)
    
    dicc, veces = eliminar_claves(dicc, claves)

    print('Resultado:')
    print(dicc)
    print(f"Se borraron {veces} claves.")


if __name__ == '__main__':
    main()
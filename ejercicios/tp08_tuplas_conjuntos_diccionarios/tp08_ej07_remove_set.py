"""
Definir un conjunto con números enteros entre 0 y 9. Luego solicitar valores al
usuario y eliminarlos del conjunto mediante el método remove, mostrando el con-
tenido del conjunto luego de cada eliminación. Finalizar el proceso al ingresar -1.
Utilizar manejo de excepciones para evitar errores al intentar quitar elementos
inexistentes.
"""
def eliminar_valor(conjunto: set[int]) -> int:
    """Verifica si un valor es eliminable de un conjunto."""
    while True:
        try:
            n = int(input('Ingresa el número a eliminar (-1 para salir): '))
            if n == -1:
                return -1
            if n not in conjunto:
                print(f'El número {n} no se encuentra en el conjunto.')
                continue
            break
        except ValueError:
            print('ERROR: Intenta con un dígito.')
    return n


def main() -> None:
    """Programa principal."""
    conjunto = set(n for n in range(10))
    print('Tengo un conjunto con números del 0 al 9.')
    print(conjunto)
    while True:
        print('Elije cual queres eliminar.')
        if not conjunto:
            print()
            print('Nos hemos quedados sin números :(')
            break
        valor = eliminar_valor(conjunto)
        if valor == -1:
            break
        conjunto.remove(valor)
        print(conjunto)
    print('Cerrando el programa. . .')


if __name__ == '__main__':
    main()
'''
Resolver el siguiente problema, utilizando funciones:
Se desea llevar un registro de los socios que visitan un club cada día. Para ello, se
ingresa el número de socio de cinco dígitos hasta ingresar un cero como fin de car-
ga. Se solicita:
a. Informar para cada socio, cuántas veces ingresó al club. Cada socio debe
aparecer una sola vez en el informe.
b. Solicitar un número de socio que se dio de baja del club y eliminar todos sus
ingresos. Mostrar los registros de entrada al club antes y después de
eliminarlo. Informar cuántos ingresos se eliminaron.
'''

def ingresar_socio() -> int:
    """
    Permite ingresar el número de socio de 5 dígitos

    Precondiciones:
        - No recibe parámetros.

    Postcondiciones:
        - Retorna un número entero, referencia a número de socio (5 dígitos).
        - Retorna 0 al finalizar la carga.
    """
    while True:
        try:
            socio = int(input('Ingrese el número de socio (0 para finalizar): '))
            if 9999 < socio < 100_000 or not socio: #Truthiness para 0
                return socio
            print('El número de socio debe ser de 5 dígitos.')
            
        except ValueError:
            print('Error al cargar dato numérico.')


def _entradas_socio(socio: int, lista_socios: list[int]) -> int:
    """
    Cuenta las veces que aparece un socio en una lista de socios y lo devuelve.

    Precondiciones:
        - Un entero de 5 dígitos.
        - Una lista de enteros de 5 dígitos.

    Postcondiciones:
        - Un entero
    """

    return lista_socios.count(socio)


def baja_socio(socio:int, lista_socios: list[int]) -> int:
    """
    Elimina al socio de la lista de socios todas las veces que aparezca.

    Precondiciones:
        - 'socio' tiene que ser un entero de 5 dígitos.
        - 'lista_socios' tiene que ser una lista de enteros de 5 dígitos.

    Postcondiciones:
        - Si 'socio' existe en 'lista_socios': modifica 'lista_socios' eliminando todas las apariciones de 'socio'.
        - Devuelve la cantidad de veces que 'socio' fue eliminado. 
    """

    veces = 0
    while socio in lista_socios:
        lista_socios.remove(socio)
        veces += 1

    return veces


def menu() -> None:
    """Menu principal"""
    
    print()
    print('='*50)
    print('1. Cargar socio')
    print('2. Baja de socio.')
    print('3. Veces que cada socio entro al club.')
    print('0. Salir')
    print('='*50)
    print()


def main() -> None:
    """Programa principal."""

    print('='*50)

    print('\nBienvenido a tu programa de gestión de socios.')

    listado_socios = []
    op = ''

    while op != '0':
        menu()
        op = input('Ingrese opción: ')

        match op:
            case '1':
                while True:
                    socio = ingresar_socio()
                    if not socio:
                        break
                    listado_socios.append(socio)

            case '2':
                socio = int(input('\nIngrese el número de socio: '))
                print(listado_socios)
                veces = baja_socio(socio, listado_socios)
                print(listado_socios)
                print(f'El socio fue eliminado {veces} veces.')


            case '3':
                for socio in set(listado_socios):
                    veces = _entradas_socio(socio, listado_socios)
                    if veces != 1:
                        print(f'El socio número {socio} vino {veces} veces.')
                    else:
                        print(f'El socio número {socio} vino {veces} vez.')



            case '0':
                print('\nSaliendo del programa ... ')


if __name__ == '__main__':
    main()
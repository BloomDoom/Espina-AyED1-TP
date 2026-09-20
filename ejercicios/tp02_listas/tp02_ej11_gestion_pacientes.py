'''
Resolver el siguiente problema, diseñando las funciones a utilizar:
Una clínica necesita un programa para atender a sus pacientes. Cada paciente que
ingresa se anuncia en la recepción indicando su número de afiliado (número entero
de 4 dígitos) y además indica si viene por una urgencia (ingresando un 0) o con
turno (ingresando un 1). Para finalizar se ingresa -1 como número de afiliado.
Luego se solicita:
a. Mostrar un listado de los pacientes atendidos por urgencia y un listado de
los pacientes atendidos por turno en el orden que llegaron a la clínica.
b. Realizar la búsqueda de un número de afiliado e informar cuántas veces fue
atendido por turno y cuántas por urgencia. Repetir esta búsqueda hasta
que se ingrese -1 como número de afiliado.
'''

def ingresar_paciente() -> int:
    '''
    Permite ingresar pacientes

    Contrato:
        - Pide un entero por teclado y valída que sea un numero de afiliado (int 4 digitos) o -1 para salir.

    Precondiciones:
        - No recibe parámetros.

    Postcondiciones:
        - Retorna un número de afiliado.
        - Retorna -1 para abandonar el ingreso.
    '''

    while True:
        try:
            paciente = int(input('Ingrese el número de afiliado (-1 para finalizar): '))
            if 999 < paciente < 10_000 or paciente == -1:
                return paciente

            print('El número de afiliado debe ser de 4 dígitos.')
        except ValueError:
            print('Error al cargar dato numérico')


def es_urgencia() -> bool:
    """
    Contrato:
        - Determina el tipo de turno (normal o de urgencia).
    
    Precondiciones:
        - No recibe parámetros.

    Postcondiciones:
        - Devuelve True si es urgencia
        - Devuelve False si es un turno normal.
    """

    while True:
        try:
            salida = int(input('Turno o urgencia? (1 para turno, 0 para urgencia): '))

            if salida in [1, 0]:
                return not salida
            print('Error, vuelve a intentar.')

        except ValueError:
            print('Error al cargar dato numérico')


def buscar_paciente(afiliado: int, lista_t: list[int], lista_u: list[int]) -> tuple[int, int]:
    """
    Busca un paciente en las listas de turnos y urgencia y devuelve las veces que aparece en ambas.

    Precondiciones:
        - Un número entero referencia a numero de afiliado. Tiene que tener 4 dígitos.
        - 2 listas de enteros.

    Postcondiciones:
        - Una tupla de 2 enteros donde idx 1 refiere a turnos normales y idx 2 refiere a turnos de urgencia del paciente.
    """

    turno = 0
    urgencia = 0

    for paciente in lista_t:
        if paciente == afiliado:
            turno += 1

    for paciente in lista_u:
        if paciente == afiliado:
            urgencia += 1

    return turno, urgencia


def menu() -> None:
    """Menu principal"""

    print('1. Cargar paciente')
    print('2. Ver listado de turnos.')
    print('3. Ver listado de urgencias.')
    print('4. Buscar paciente por número de afiliado.')
    print('0. Salir')


def main() -> None:
    """Programa principal."""

    print('='*50)
    print('Buen dia\nBienvenido a tu programa de gestión de pacientes.')

    listado_urgencias = []
    listado_turnos = []

    print('='*50)
    print('MENU')
    print('='*50)

    op = ''

    while op != '0':
        menu()
        op = input('Ingrese opción: ')

        match op:
            case '1':
                while True:
                    num_afiliado = ingresar_paciente()
                    if num_afiliado == -1:
                        break
                    urgente = es_urgencia()
                
                    if urgente:
                        listado_urgencias.append(num_afiliado)
                    else:
                        listado_turnos.append(num_afiliado)

            case '2':
                print('Listado de pacientes con turno:')
                print(listado_turnos)

            case '3':
                print('Listado de pacientes por urgencia:')
                print(listado_urgencias)

            case '4':
                afiliado = 0

                while afiliado != -1:
                    afiliado = ingresar_paciente()

                    if afiliado == -1:
                        break

                    turnos, urgencia = buscar_paciente(afiliado, listado_turnos, listado_urgencias)

                    if not turnos and not urgencia:
                        print(f'El afiliado número {afiliado} no tiene historial registrado.')

                    elif turnos:
                        print(f'El afiliado número {afiliado} fue atendido {turnos} vez/veces')

                    elif urgencia:
                        print(f'El afiliado número {afiliado} fue atendido {urgencia} vez/veces')

            case '0':
                print('Saliendo del programa ... ')


if __name__ == '__main__':
    main()
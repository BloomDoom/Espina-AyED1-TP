"""
El método index permite buscar un elemento dentro de una lista, devolviendo la
posición que éste ocupa. Sin embargo, si el elemento no pertenece a la lista se
produce una excepción de tipo ValueError. Desarrollar un programa que cargue
una lista con números enteros ingresados a través del teclado (terminando con -1)
y permita que el usuario ingrese el valor de algunos elementos para visualizar la
posición que ocupan, utilizando el método index. Si el número no pertenece a la
lista se imprimirá un mensaje de error y se solicitará otro para buscar. Abortar el
proceso al tercer error detectado. No utilizar el operador in durante la búsqueda.
"""


def cargar_lista(lista: list[int]) -> bool:
    """
    Contrato:
        - Dada una lista, permite su carga por teclado de números enteros.

    Precondiciones:
        - Recibe una lista vacía, o de enteros.

    Postcondiciones:
        - Retorna True si hubo carga de datos en la lista.
        - Retorna False si no hubo carga de datos en la lista.
        - Si retorna True, la lista ha mutado.
    """

    carga: bool = False
    
    while True:
        try:
            n = int(input('Ingrese un número a añadir a la lista (-1 para salir): '))
            if n == -1:
                break
            lista.append(n)
            carga = True

        except ValueError:
            print('Solo se permite la carga de números enteros.')

    if carga:
        return True
    
    return False


def main() -> None:
    """Programa principal."""
    
    lista: list[int] = []

    print()
    print('Bienvenido al programa.')
    print('Vamos a cargar una lista con valores enteros.')
    print('Luego buscaremos los valores dentro de ella.')
    print()

    if cargar_lista(lista):

        contador = 0
        while contador < 3:
            while True:
                try:
                    valor = int(input('\nIngrese el valor a buscar: '))
                    break
                except ValueError:
                    print('Intente ingresando un número entero.')
            
            try:
                
                i = lista.index(valor)
            
            except ValueError:
                contador += 1
                print('No existe tal valor en la lista.')
                print(f'Intento {contador}/3.')
                print()

            else:
                print(f'El valor se encontró en la posición {i + 1}')

        print('¡Hasta la próxima!')


if __name__ == "__main__":
    main()
'''
Escribir una función para eliminar una subcadena de una cadena de caracteres, a
partir de una posición y cantidad de caracteres dadas, devolviendo la cadena resul-
tante. Escribir también un programa para verificar el comportamiento de la misma.
Escribir una función para cada uno de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas
'''

def con_slicing(s: str, inicio: int, cant: int) -> str:
    """
    Contrato:
        - A partir de una cadena recibida, se corta una rebanada desde 'inicio' hasta llegar a la cantidad deseada.
        - En caso de haber menos que la cantidad deseada, se elimina hasta el final de la cadena.

    Precondiciones:
        - Una cadena.
        - Un entero; índice válido de la cadena.
        - Un entero; largo deseado de la subcadena a eliminar.

    Postcondiciones:
        - Una cadena.
    """
    salida = s[:inicio] + s[inicio + cant:]
    
    return salida


def sin_slicing(s: str, inicio: int, cant: int) -> str:
    """
    Contrato:
        - A partir de una cadena recibida, se corta una rebanada desde 'inicio' hasta llegar a la cantidad deseada.
        - En caso de haber menos que la cantidad deseada, se elimina hasta el final de la cadena.

    Precondiciones:
        - Una cadena.
        - Un entero; índice válido de la cadena.
        - Un entero; largo deseado de la subcadena a eliminar.

    Postcondiciones:
        - Una cadena.
    """
    salida = ''
    for i in range(inicio):
        salida += s[i]

    for i in range(inicio + cant, len(s)):
        salida += s[i]

    return salida


def main() -> None:
    """Programa principal."""
    centrar = 80
    
    print('='*centrar)
    print(f"{'Bienvenido al programa para cortar frases!':^{centrar}}")
    print(f"{'Cortaremos la frase según el índice que vos digas.':^{centrar}}")

    s = input('Ingrese la frase a cortar: ')

    while True:
        try:
            inicio = int(input('Ingrese el índice de inicio de corte: '))
            cant = int(input('Ingrese la cantidad de caractéres: '))
            break
        except ValueError:
            print('Error en la carga de datos, pruebe con dígitos.')

    print('Decide si lo quieres hacer con slicing o sin slicing.')
    con = bool(input('Escribe algo para hacerlo con slicing, o presiona enter para hacerlo sin slicing: '))

    print('La frase recortada es:')
    
    if con:
        print('Con slicing:')
        print(con_slicing(s, inicio, cant))
    else:
        print('Sin slicing:')
        print(sin_slicing(s, inicio, cant))

if __name__ == '__main__':
    main()

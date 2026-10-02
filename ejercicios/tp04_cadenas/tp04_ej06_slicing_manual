'''
Desarrollar una función que extraiga una subcadena de una cadena de caracteres,
indicando la posición y la cantidad de caracteres deseada. Devolver la subcadena
como valor de retorno. Escribir también un programa para verificar el comporta-
miento de la misma. Ejemplo, dada la cadena "El número de teléfono es 4356-
7890" extraer la subcadena que comienza en la posición 25 y tiene 9 caracteres,
resultando la subcadena "4356-7890". Escribir una función para cada uno de los si-
guientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas
'''



def con_slicing(s: str, inicio: int, cant: int) -> str:
    """
    Contrato:
        - A partir de una cadena recibida, se corta una rebanada desde 'inicio' hasta llegar a la cantidad deseada.
        - En caso de haber menos que la cantidad deseada, se devuelve hasta el final de la cadena.

    Precondiciones:
        - Una cadena.
        - Un entero; índice válido de la cadena.
        - Un entero; largo deseado de la subcadena.

    Postcondiciones:
        - Una cadena; subcadena de 's' de largo igual o menor a 'cant'.
    """
    return s[inicio:inicio + cant]


def sin_slicing(s: str, inicio: int, cant: int) -> str:
    """
    Contrato:
        - A partir de una cadena recibida, se corta una rebanada desde 'inicio' hasta llegar a la cantidad deseada.
        - En caso de haber menos que la cantidad deseada, se devuelve hasta el final de la cadena.

    Precondiciones:
        - Una cadena.
        - Un entero; índice válido de la cadena.
        - Un entero; largo deseado de la subcadena.

    Postcondiciones:
        - Una cadena; subcadena de 's' de largo igual o menor a 'cant'.
    """
    salida = ''

    if inicio + cant > len(s):
        fin = len(s)
    else:
        fin = inicio + cant
    
    for i in range(inicio, fin):
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
    con = bool(input('Escribe algo para hacerlo con, o presiona enter para hacerlo sin: '))

    print('La frase recortada es:')
    
    if con:
        print('Con slicing:')
        print(con_slicing(s, inicio, cant))
    else:
        print('Sin slicing:')
        print(sin_slicing(s, inicio, cant))

if __name__ == '__main__':
    main()

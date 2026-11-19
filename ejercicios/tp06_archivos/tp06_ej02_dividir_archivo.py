"""
Escribir un programa que permita dividir un archivo de texto cualquiera en partes
que se puedan enviar por correo electrónico. El tamaño máximo de las partes se
ingresa por teclado. Los nombres de los archivos generados deben respetar el
nombre original con el agregado de un sufijo que indique de qué parte se trata.
Tener en cuenta que ningún registro puede ser dividido; la partición debe efectuar-
se después del delimitador del mismo. Mostrar un mensaje de error si el proceso no
pudiera llevarse a cabo. Recordar que no se permite cargar el archivo completo en
memoria.
"""


def particionar_txt(archivo: str, limite: int) -> int:
    """
    Contrato:
        - Dado un archivo '.txt' se lo particiona según cantidad
        ingresada por teclado.

    Precondiciones:
        - String; Archivo a trabajar. DEBE estar en el mismo directorio.
        - Int; cantidad máxima de partición.

    Postcondiciones:
        - Int; la cantidad de particiones.
        - No modifica el archivo madre.
        - Crea la cantidad de particiones necesarias para cumplir el
        objetivo. Cada partición esta enumerada.
    """

    nombre, ext = archivo.split('.')[0], archivo.split('.')[1]
    n_part = 0
    
    try:
        arch = open(archivo, 'r', encoding='utf-8-sig')

    except FileNotFoundError:
        print('No se encontró el archivo en el directorio actual.')

    else:
        with arch:
            lineas: str = ''
            
            for linea in arch:
                if len(linea + lineas) <= limite:
                    lineas += linea

                else:
                    n_part += 1
                    with open(nombre + f' ({n_part}).' + ext, 'w', encoding='utf-8') as a:
                        a.write(lineas)
                        lineas = ''

    return n_part


def main() -> None:
    """Programa principal."""

    print()
    print('En este programa vamos a particionar un archivo en N partes.')
    print('Las partes provienen del tamaño de cada partición.')
    
    while True:
        try:
            n = int(input('Ingrese el tamaño de las particiones: '))
            if n > 0:
                break
            print('La partición debe tener un tamaño positivo.')
        except ValueError:
            print('Intente con un número.')

    print()
    print('Ahora, ingrese el archivo a particionar.')
    print('Recuerde que se debe encontrar en el directorio actual.')
    archivo = input('Ingrese el archivo con su extensión correspondiente: ')
    particiones = particionar_txt(archivo, n)
    print()
    print(f'La cantidad de particiones creadas es: {particiones}')


if __name__ == '__main__':
    main()
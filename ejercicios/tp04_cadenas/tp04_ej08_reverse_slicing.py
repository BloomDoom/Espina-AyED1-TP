'''
Desarrollar una función que devuelva una subcadena con los últimos N caracteres
de una cadena dada. La cadena y el valor de N se pasan como parámetros.
'''

def cortar_cadena(s: str, n: int) -> str:
    """
    Contrato:
        - Recorta los últimos n caracteres de una cadena recibida.

    Precondiciones:
        - Una cadena.
        - Un entero.

    Postcondiciones:
        - Una cadena de 0 <= tamaño <= n 
    """
    return s[-n:len(s)]


def main() -> None:
    """Programa principal."""
    centrar = 80
    
    print('='*centrar)
    print(f"{'Bienvenido al programa para cortar frases!':^{centrar}}")
    print(f"{'Cortaremos el final de la frase.':^{centrar}}")

    s = input('Ingrese la frase a cortar: ')

    while True:
        try:
            cant = int(input('Ingrese la cantidad de caractéres a conservar, contando desde el final: '))
            break
        except ValueError:
            print('Error en la carga de datos, pruebe con dígitos.')

    print('La frase recortada es:')
    
    print(cortar_cadena(s, cant))

if __name__ == '__main__':
    main()

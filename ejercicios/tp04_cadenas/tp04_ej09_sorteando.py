'''
Escribir una función que reciba como parámetro una cadena de caracteres en la que
las palabras se encuentran separadas por uno o más espacios. Devolver otra
cadena con las palabras ordenadas según su longitud, dejando un espacio entre
cada una. Los signos de puntuación no deben ser tenidos en cuenta al medir la
longitud de las palabras, pero deberán conservarse en la cadena final.
'''

def ordenar_por_longitud(s: str) -> str:
    """
    Contrato:
        - Mediante una cadena recibida, cuenta las palabras separadas por uno o más espacios.
        - Devuelve una cadena con las palabras ordenadas según su longitud.
        - No considera signos de puntuación para su longitud.
        - Se considera signos de puntuación todo lo que isalnum() considere 'False'.

    Precondiciones:
        - Una cadena; una frase de palabras separadas con espacios.

    Postcondiciones;
        - Una cadena; palabras ordenadas según su longitud de menor a mayor.
    """

    return " ".join(sorted(s.split(), key= lambda palabra: len([letra for letra in palabra if letra.isalnum()]))) # Llegué a esta compresión de código luego de mucho trabajo..


def main() -> None:
    """Programa principal."""
    centrar = 80
    
    print('='*centrar)
    print(f"{'Bienvenido al programa para ordenar palabras por longitud!':^{centrar}}")
    print(f"{'... sin tener en cuenta los signos de puntuación.':^{centrar}}")
    print()
    s = input('Ingrese la frase a trabajar: ')
    print()
    print('El resultado del trabajo:')
    print()
    print(ordenar_por_longitud(s))
    print()
    print('='*centrar)

if __name__ == '__main__':
    main()
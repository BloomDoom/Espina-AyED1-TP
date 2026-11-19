"""
Ingresar una frase desde el teclado y usar un conjunto para eliminar las
palabras repetidas, dejando un solo ejemplar de cada una.
Finalmente mostrar las palabras ordenadas según su longitud.
Los signos de puntuación no deben afectar el proceso.
"""

import string


def main() -> None:
    """Programa principal."""
    print('Le voy a pedir una frase.')
    signos = string.punctuation + '¿' + '¡'
    frase = input('Ingrese una frase: ').lower()
    for signo in signos:
        frase = frase.replace(signo, ' ')
    frase = frase.split()
    print('Ahora le voy a sacar las palabras repetidas.')
    print('...')
    frase_sin_repetir = set(frase)
    print('Listo!')
    print('Ahora las voy a ordenar de menor a mayor.')
    frase_limpia = sorted(frase_sin_repetir, key=len)
    print(frase_limpia)


if __name__ == '__main__':
    main()
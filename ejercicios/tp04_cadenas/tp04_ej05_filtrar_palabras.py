'''
Escribir una función filtrar_palabras() que reciba una cadena de caracteres conte-
niendo una frase y un entero N, y devuelva otra cadena con las palabras que ten-
gan N o más caracteres de la cadena original. Escribir también un programa para
verificar el comportamiento de la misma. Hacer tres versiones de la función, para
cada uno de los siguientes casos:
a. Utilizando sólo ciclos normales
b. Utilizando listas por comprensión
c. Utilizando la función filter
'''


def filtrar_palabras(s: str, n: int) -> str:
    """
    Contrato:
        - Filtra palabras segun N longitud y la devuelve.

    Precondiciones:
        - Una cadena.
        - Un entero positivo.

    Postcondiciones:
        - Un string, puede estar vacío.
    """

    sub_s = []
    sub_s = s.split()
    new_s = []

    for each in sub_s:
        if len(each) > n:
            new_s.append(each)

    out = ' '.join(new_s)
    
    return out


def main() -> None:
    """Programa principal."""
    centrar = 80
    
    print('='*centrar)
    print(f"{'Bienvenido al programa para filtrar palabras!':^{centrar}}")
    print(f"{'Filtraremos las palabras de la frase según el largo que vos digas.':^{centrar}}")

    s = input('Ingrese la frase a filtrar: ')

    while True:
        try:
            n = int(input('Ingrese la cantidad de palabras para el filtro: '))
            if n >= 0:
                break
            print('Ingrese un número positivo.')
        except ValueError:
            print('Error en la carga de datos, pruebe con un dígito.')

    print(f'Las palabras con longitud mayor a {n}:')
    palabras = filtrar_palabras(s, n).split()

    for palabra in palabras:
        print(f'La palabra {palabra} tiene {len(palabra)} letras!')


if __name__ == '__main__':
    main()
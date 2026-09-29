'''
Desarrollar una función que determine si una cadena de caracteres es capicúa, sin
utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que permita
verificar su funcionamiento.
'''
def es_capicua(s: str) -> bool:
    """
    Contrato:
        - Determina si una cadena es capicúa o no.

    Precondiciones:
        - Una cadena

    Postcondiciones:
        - True si la cadena es capicúa.
        - Una cadena vacía se considera capicúa.
        - False si la cadena no es capicúa.
    """
    len_s = len(s)

    if not len_s:
        return True

    for i in range(len_s):
        if s[i] != s[-(i + 1)]:
            return False
    return True

def main() -> None:
    """Programa principal."""
    s = input('Ingrese un texto, le diré si es capicúa o no: ')

    capicua = es_capicua(s)

    if capicua:
        print(f'El texto {s} es capicúa!!')
    else:
        print(f'El texto {s} no es capicúa :()')


if __name__ == '__main__':
    main()
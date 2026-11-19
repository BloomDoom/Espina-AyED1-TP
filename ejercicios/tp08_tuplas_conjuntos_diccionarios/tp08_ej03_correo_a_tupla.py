"""
Desarrollar un programa que utilice una función que reciba como parámetro una
cadena de caracteres conteniendo una dirección de correo electrónico y devuelva
una tupla con las distintas partes que componen dicha dirección. Ejemplo:
alguien@uade.edu.ar -> (alguien, uade, edu, ar). La función debe detectar
formatos de fecha inválidos y devolver una tupla vacía.
"""


def correo_a_tupla(correo: str) -> tuple[str, ...]:
    """
    Contrato:
        - Dado un correo, se lo procesa y se separan las partes.
        - Las partes se retornan como tupla.

    Precondiciones:
        - El correo debe tener al menos un @ y al menos un .(dot).

    Postcondiciones:
        - La tupla contiene las partes sin sus separadores.
    """
    if '@' not in correo or '.' not in correo:
        return ()
    
    usuario = correo.split('@')
    partes = usuario[1].split('.')
    return (usuario[0],) + tuple(partes)


def main() -> None:
    """
    Se solicita un correo por teclado, se procesa y se muestra una
    tupla con sus partes.
    """

    correo = input('Ingrese un correo electrónico válido: ')
    
    tupla = correo_a_tupla(correo)
    if not tupla:
        print('Formato inválido.')
        return
    
    print('Las partes del correo ingresado son:')
    print(tupla)


if __name__ == '__main__':
    main()
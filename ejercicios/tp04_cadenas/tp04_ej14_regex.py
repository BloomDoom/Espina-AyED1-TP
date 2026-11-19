'''
Se solicita crear un programa para leer direcciones de correo electrónico y verificar
si representan una dirección válida. Por ejemplo usuario@dominio.com.ar. Para que
una dirección sea considerada válida el nombre de usuario debe poseer solamente
caracteres alfanuméricos, la dirección contener un solo carácter @, el dominio debe
tener al menos un carácter y tiene que finalizar con .com o .com.ar.
Repetir el proceso de validación hasta ingresar una cadena vacía. Al finalizar mos-
trar un listado de todos los dominios, sin repetirlos y ordenados alfabéticamente,
recordando que las direcciones de mail no distinguen mayúsculas ni minúsculas.
'''

import re


def _es_email(correo:str) -> bool:
    """
    Contrato:
        - Determina si es un correo electrónico válido.
        - Es válido cuando se compone de esta manera:
            - Nombre de usuario debe poseer solamente caracteres alfanuméricos.
            - La dirección contener un solo carácter @.
            - El dominio debe tener al menos un carácter.
            - Tiene que finalizar con .com o .com.ar.
        
    Precondiciones:
        - Un string; correo electrónico.

    Postcondiciones:
        - True si es válido.
        - False si no es válido.
    """

    patron = r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.com(\.ar)?$'

    return bool(re.match(patron, correo))


def validar_correo() -> None:
    """
    Contrato:
        - Permite ingresar correos electrónicos y validarlos.

    Precondiciones:
        - No tiene.
    
    Postcondiciones:
        - No tiene.
    """
    centrar = 80
    correos: list[str] = []
    son_correos: list[bool] = []
    correo = 'while'    # Me aseguro entrar al while al menos 1 vez.
    
    print('='*centrar)
    print(f"{'Bienvenido al programa para corroborar correos electrónicos!':^{centrar}}")
    print()
    
    while correo:
        correo = ''
        correo = input('Ingrese el correo a validar (ENTER para salir): ')
        if correo:
            correos.append(correo)

    for correo in correos:
        son_correos.append(_es_email(correo))

    salidas = zip(correos, son_correos)

    for mail, val in salidas:
        if val:
            print(f'El correo {mail} es válido.')
        else:
            print(f'El correo {mail} es inválido.')


def main() -> None:
    """Programa principal."""
    validar_correo()


if __name__ == '__main__':
    main()
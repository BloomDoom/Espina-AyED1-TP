'''
Escribir un programa para crear una lista por comprensión con los naipes de la ba-
raja española. La lista debe contener cadenas de caracteres. Ejemplo: ["1 Oros", "2
Oros"... ]. Imprimir la lista por pantalla.
'''

def baraja_espaniola() -> list[str]:
    """
    Contrato:
        - Crea y devuelve una baraja de naipes española.
        - Orden: Del 1 al 12, Oros, Bastos, Espadas y Copas.
    
    Precondiciones:
        - No recibe parámetros.

    Postcondiciones:
        - Una lista de str.
    """
    
    return [n + ' ' + palo for palo in ('Oros', 'Bastos', 'Espadas', 'Copas') for n in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')]

print(baraja_espaniola())


def main() -> None:
    """Programa principal."""
    centrar = 80
    
    print('='*centrar)
    print(f"{'Bienvenido al programa para crear un mazo español por comprensión!':^{centrar}}")
    print()
    print('El resultado del trabajo:')
    print(baraja_espaniola())
    print('='*centrar)
    

if __name__ == '__main__':
    main()
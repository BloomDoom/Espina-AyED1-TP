'''
Generar e imprimir una lista por comprensión entre A y B con los múltiplos de 7
que no sean múltiplos de 5. A y B se ingresar desde el teclado.
'''
def main() -> None:
    """ Programa principal. """

    print('='*50)
    print('Generaré una lista de números entre 2 limites que vos digas.')
    a = int(input('Ingrese límite inferior (inclusivo): '))
    b = int(input('Ingrese límite superior (exclusivo): '))
    print('Encuentre lo que todos tienen en común:')
    print([n for n in range(a, b) if n%7 == 0 and n%5 != 0])
    print('='*50)


if __name__ == '__main__':
    main()
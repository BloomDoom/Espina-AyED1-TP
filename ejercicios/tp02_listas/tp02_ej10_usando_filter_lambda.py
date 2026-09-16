from random import randint as ri


def main() -> None:    
    '''
    Programa principal.

    Generar una lista con números al azar entre 1 y 100 y crear una nueva lista con los
    elementos de la primera que sean impares. El proceso deberá realizarse utilizando
    la función filter(). Imprimir las dos listas por pantalla.
    '''
    print('='*50)
    print('Lista')
    lista = [ri(1, 100) for x in range(20)]

    impares = list(filter(lambda n: n%2, lista))


if __name__ == '__main__':
    main()

'''
Utilizar la técnica de listas por comprensión para construir una lista con todos los
números impares comprendidos entre 100 y 200.
'''

def main() -> None:
    """Funcion principal."""

    impares_del_100_al_200 = [x for x in range(101, 200, 2)]
    print('='*100)
    print(impares_del_100_al_200)
    print('='*100)


if __name__ == '__main__':
    main()
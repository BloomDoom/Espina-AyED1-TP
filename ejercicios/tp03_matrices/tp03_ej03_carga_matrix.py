'''
Desarrollar un programa para rellenar una matriz de N x N con números enteros al
azar comprendidos en el intervalo [0,N2), de tal forma que ningún número se repi-
ta. Imprimir la matriz por pantalla.
'''
from random import randint as ri


def main() -> None:
    """Programa principal."""
    while True:
        try:
            n = int(input('Ingrese un número entero positivo: '))
            if n > 0:
                m = [[] for n in range(n)]
                break
            else:
                print('Error, vuelva a intentar.')
        except ValueError:
            print('Error en la carga de datos.')

    usados = []
    for r in m:
        while len(r) < len(m):
            valor = ri(0, n**2 - 1)
            if valor not in usados:
                r.append(valor)
                usados.append(valor)
    print(m)

if __name__ == '__main__':
    main()
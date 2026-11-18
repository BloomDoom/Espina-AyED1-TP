"""
En geometría un vector es un segmento de recta orientado que va desde un punto
A hasta un punto B. Los vectores en el plano se representan mediante un par orde-
nado de números reales (x, y) llamados componentes. Para representarlos basta
con unir el origen de coordenadas con el punto indicado en sus componentes:
Dos vectores son ortogonales cuando son perpendiculares entre sí. Para determi-
narlo basta calcular su producto escalar y verificar si es igual a 0. Ejemplo:
A = (2,3) y B = (-3,2) => 2 * (-3) + 3 * 2 = -6 + 6 = 0 => Son ortogonales
Escribir una función que reciba dos vectores en forma de tuplas y devuelva un valor
de verdad indicando si son ortogonales o no. Desarrollar también un programa que
permita verificar el comportamiento de la función.
"""

def es_ortogonal(par1: tuple[float, float], par2: tuple[float, float]) -> bool:
    """Determina si 2 vectores son ortogonales."""
    if len(par1) != 2 or len(par2) != 2:
        return False

    x1, y1 = par1
    x2, y2 = par2

    a = x1 * x2
    b = y1 * y2
    calculo = a + b

    return not calculo


def main() -> None:
    """
    Programa principal.
    Verifica si la funcion es_ortogonal funciona correctamente.
    Los datos son ingresados por teclado.
    """
    print('Corroboraremos si 2 pares ordenados son ortogonales entre sí.')
    print('A continuación, le voy a pedir que ingrese 4 valores.')
    valores: list[float] = []
    while len(valores) < 4:
        try:
            x = float(input('Ingrese un valor: '))
        except ValueError:
            print('Ingrese un dato numérico.')
        else:
            valores.append(x)

    par1 = valores[0], valores[1]
    par2 = valores[2], valores[3]

    print('Los pares son:')
    print(par1)
    print(par2)
    print()
    if es_ortogonal(par1, par2):
        print('Los pares son ortogonales entre sí!')
    else:
        print('Los pares no son ortogonales entre sí.')


if __name__ == '__main__':
    main()
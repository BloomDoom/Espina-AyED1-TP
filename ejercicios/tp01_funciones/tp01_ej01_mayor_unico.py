'''Desarrollar una función que reciba tres números enteros positivos y devuelva el
mayor de los tres, sólo si éste es único (es decir el mayor estricto). Devolver -1 en
caso de no haber ninguno. No utilizar operadores lógicos (and, or, not). Desarrollar
también un programa para ingresar los tres valores, invocar a la función y mostrar
el máximo hallado, o un mensaje informativo si éste no existe.'''

def ingresar_valor() -> tuple:
    n = int(input("Ingrese un numero entero positivo: "))
    m = int(input("Ingrese un numero entero positivo: "))
    l = int(input("Ingrese un numero entero positivo: "))

    return n, m, l

def mayor_de_3(n: int, m: int, l: int) -> int:
    '''
    Contrato: Recibe tres numeros enteros y devuelve el mayor estricto, en caso de no encontrarlo, devuelve -1.
    Precondiciones: Recibir tres numeros enteros positivos.
    Postcondiciones: Devuelve el mayor estricto, -1 en caso de empate.
    '''

    menor_a_mayor = sorted([n, m, l])

    if menor_a_mayor[-1] == menor_a_mayor[-2]:
        return -1
    return menor_a_mayor[-1]
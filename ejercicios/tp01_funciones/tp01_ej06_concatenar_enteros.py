'''Desarrollar una función que reciba como parámetros dos números enteros positivos
y devuelva como valor de retorno el número que resulte de concatenar ambos
parámetros. Por ejemplo, si recibe 1234 y 567 debe devolver 1234567. No se per-
mite utilizar facilidades de Python no vistas en clase'''

def concatenar_enteros(n: int, m: int) -> int:
    '''
    Contrato:
        Une dos enteros n, m -> de manera que quedan nm (4, 3 -> 43).
    Precondiciones:
        Los enteros deben ser de orden natural.
    Postcondiciones:
        Un numero entero.
    '''
    assert isinstance(n, int) and isinstance(m, int), 'El parametro debe ser un numero entero.'
    assert n >=0 and m >= 0, 'Los parametros deben ser positivos.'

    return int(f'{n}{m}')
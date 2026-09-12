'''Escribir funciones lambda para:
    
    a. Informar si un número es oblongo. Se dice que un número es oblongo cuando
    se puede obtener multiplicando dos números naturales consecutivos. Por ejemplo
    6 es oblongo porque resulta de multiplicar 2 * 3.

    b. Informar si un número es triangular. Un número se define como triangular si
    puede expresarse como la suma de un grupo de números naturales consecutivos 
    comenzando desde 1. Por ejemplo 10 es un número triangular porque se
    obtiene sumando 1+2+3+4.

Ambas funciones lambda reciben como único parámetro el número a evaluar y de-
vuelven True o False. No se permite utilizar ayudas externas a las mismas.'''

def es_oblongo(n: int) -> bool:
    '''
        Contrato: Recibe un numero natural y devuelve un booleano.
        Precondicion: El parametro recibido debe ser un numero de orden natural, 0 se acepta como oblongo (0 * 1 = 0).
        Postcondicion: Devuelve True si el parametro recibido es oblongo, para todo lo demas retorna False.
    '''
    for i in range(int(n ** 0.5) + 1):
        if i * (i + 1) == n:
            return True
    return False

es_oblongo_lambda = lambda n: any(i * (i + 1) == n for i in range(int(n ** 0.5) + 1))

def es_triangular(n: int) -> bool:
    '''
        Contrato: Recibe un numero natural, analiza si este es triangular o no.
        Precondicion: El parametro recibido debe ser un numero de orden natural.
        Postcondicion: Devuelve True si el parametro recibido es triangular, para todo lo demas retorna False.
    '''
    contador = 0
    acumulador = 0
    
    while acumulador <= n:
        contador += 1
        acumulador += contador
        if acumulador == n:
            return True
    return False

es_triangular_lambda = lambda n: any((i * (i + 1)) // 2 == n for i in range(n + 1))
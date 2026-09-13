'''Resolver el siguiente problema utilizando funciones:
Un productor frutihortícola desea contabilizar sus cajones de naranjas según el peso
para poder cargar los camiones de reparto. La empresa cuenta con N camiones, y
cada uno puede transportar hasta media tonelada (500 kilogramos). En un cajón
caben 100 naranjas con un peso de entre 200 y 300 gramos cada una. Si el peso
de alguna naranja se encuentra fuera del rango indicado se la clasifica para
procesar como jugo. Desarrollar un programa para ingresar la cantidad de naranjas
cosechadas e informar cuántos cajones se pueden llenar, cuántas naranjas son para
jugo y si hay algún sobrante de naranjas que deba considerarse para el siguiente
reparto. Simular el peso de cada unidad generando un número entero al azar entre
150 y 350.
Además, se desea saber cuántos camiones se necesitan para transportar la cose-
cha, considerando que la ocupación del camión no debe ser inferior al 80%; en
caso contrario el camión no serán despachado por su alto costo.'''

from random import randint as ri


def simular_peso(n: int) -> list[int]:
    '''
    Simula el peso de una naranja.

    Contrato:
       - Carga enésimos numeros entre 150 y 350 simulando ser el peso de una naranja.
    
    Precondiciones:
        - Recibe un único parámetro entero igual o mayor a cero.

    Postcondiciones:
        - Retorna una lista donde sus elementos son enteros entre 150 y 350 inclusive. La cantidad de elementos depende del parámetro recibido.
    '''

    assert n >= 0, 'No puede haber naranjas negativas :('

    peso_n = [ri(150, 350) for i in range(n)]

    return peso_n

def categorizar_naranjas(lista_naranjas: list[int]) -> tuple[list, list]:
    '''
    Categoriza naranjas según su peso.
    
    Contrato:
       - Separa las naranjas en 2 grupos, entre 200 y 300 inclusive forman un grupo, el resto forman otro.
       - Retorna una tupla de listas donde la primer lista son las naranjas de transporte y la segunda las naranjas de jugo.
    
    Precondiciones:
        - Recibe un único parámetro lista donde sus elementos son los pesos de las naranjas y la cantidad su longitud.
    
    Postcondiciones:
        - Retorna una tupla de dos elementos tipo lista donde sus elementos son los pesos de las naranjas y la cantidad su longitud.
    
    '''
    nar = []
    jugo = []

    for naranja in lista_naranjas:
        if 200 <= naranja <= 300:
            nar.append(naranja)
        else:
            jugo.append(naranja)

    return nar, jugo

def llenar_cajon(lista_naranjas: list[int]) -> tuple[list[int], int]:
    '''
    Llena cajones de naranjas donde cada 100 naranjas es un cajón, tambien se ocupa de las naranjas sobrantes y el peso de cada cajón.
    
    Contrato:
        - Recibe una cantidad de naranjas con su peso y las organiza en cajones.
        - Devuelve una tupla donde el primer elemento es una lista de cajones llenos con su peso y el segundo el sobrante de naranjas (0-99).

    Precondiciones:
        - Recibe una lista de enteros.

    Postcondiciones:
        - Una tupla de 2 elementos donde el primero es una lista de enteros y el segundo un entero.
    '''
    cant_naranjas = len(lista_naranjas)
    # cajones, = cant_naranjas // 100               ### Así haría un estudiante de IaA
    # sobrante = cant_naranjas % 100                ### Así haría un estudiante de IaA
    cajones, sobrante = divmod(cant_naranjas, 100)  ### Así hace un estudiante de AyED1
    lista_cajones = []
    naranjas = 0

    while cajones:
        peso_cajón = 0
        for naranja in lista_naranjas[naranjas:naranjas + 100]:
            peso_cajón += naranja
        naranjas += 100
        lista_cajones.append(peso_cajón)
        cajones -= 1

    return lista_cajones, sobrante


def main() -> None:
    '''Programa principal'''

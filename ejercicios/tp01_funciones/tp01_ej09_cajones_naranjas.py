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

    return [ri(150, 350) for i in range(n)]

def categorizar_naranjas(lista_naranjas: list[int]) -> tuple[list[int], list[int]]: # YAGNI
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

def llenar_cajon(lista_naranjas: list[int]) -> tuple[list[int], list[int]]:
    '''
    Llena cajones de naranjas donde cada 100 naranjas es un cajón, tambien se ocupa de las naranjas sobrantes y el peso de cada cajón.
    
    Contrato:
        - Recibe una cantidad de naranjas con su peso y las organiza en cajones.
        - Devuelve una tupla donde el primer elemento es una lista de cajones llenos con su peso, y, el segundo el sobrante de naranjas (0-99).

    Precondiciones:
        - Recibe una lista de enteros.

    Postcondiciones:
        - Una tupla de 2 elementos donde el primero y el segundo son una lista de enteros.
    '''
    cant_naranjas = len(lista_naranjas)
    # cajones, = cant_naranjas // 100               ### Así haría un estudiante de IaA
    # sobrante = cant_naranjas % 100                ### Así haría un estudiante de IaA
    cajones, sobrante = divmod(cant_naranjas, 100)  ### Así hace un estudiante de AyED1
    lista_cajones = []
    naranjas = 0

    for _ in range(cajones):
        peso_cajón = 0
        for naranja in lista_naranjas[naranjas:naranjas + 100]:
            peso_cajón += naranja
        naranjas += 100
        lista_cajones.append(peso_cajón)

    return lista_cajones, lista_naranjas[-sobrante:]


def llenar_camion(lista_cajones: list[int]) -> tuple[list[int], list[int]]:
    '''
    Carga camiones con cajones de naranjas, el camión se considera cargado cuando su peso oscila entre 400kg y 500kg.
    
    Contrato:
        - Necesita una lista de enteros positivos como parametro para funcionar coherentemente.
    
    Precondicion:
        - Una lista de enteros con elementos.

    Postcondicion:
        - Una tupla con dos listas de enteros. La primera representa la cantidad de camiones y la segunda los cajones sobrantes.
    '''
    MAX_CARGA = 500000          ### 500kg es el máximo de carga de cada camión.
    MIN_CARGA = 400000          ### 400kg es el mínimo de carga del último camión.

    lista_camiones = [0]
    i = 0                       ### Número del camión - 1.
    cajones_en_camion = 0

    for cajon in lista_cajones:
        
        if lista_camiones[i] + cajon <= MAX_CARGA:
            lista_camiones[i] += cajon
            cajones_en_camion += 1
        elif MIN_CARGA <= lista_camiones[i] <= MAX_CARGA:
            i += 1
            lista_camiones.append(0)
            cajones_en_camion = 0

    if MIN_CARGA <= lista_camiones[-1] <= MAX_CARGA:
        return lista_camiones
    elif lista_camiones[-1] < MIN_CARGA:
        del lista_camiones[-1]
        cajones_sobrantes = [x for x in lista_cajones[-cajones_en_camion:]]

    return lista_camiones, cajones_sobrantes
  

def main() -> None:         ###Noto mucho YAGNI que hice.. lo mejoraré mas adelante.
    '''Programa principal'''

    print('='*50)
    print('Bienvenido.')
    print('Carga tus naranjas.')
    print('Yo hago los números.')

    while True:
        n = int(input('Ingrese la cantidad de naranjas cosechadas en digitos: '))
        if n >= 0:
            break
        print('Carga incorrecta.')

    naranjas = simular_peso(n)
    naranja_carga, naranja_jugo = categorizar_naranjas(naranjas)

    print()
    print(f'Tiene {len(naranja_carga)} naranjas para cargar en los cajones.')
    print(f'Tiene {len(naranja_jugo)} naranjas para hacer jugo.')
    print()

    cajones, naranjas_sobrantes = llenar_cajon(naranja_carga)

    print(f'Hemos podido cargar {len(cajones)} cajones exitosamente.')
    print(f'\nLe sobran {len(naranjas_sobrantes)} naranjas, ¿Quiere meterlas en un cajón?')
    print('1. SI')
    print('0. NO')
    print()

    while True:
        op = int(input('Ingrese opción (1 para SI, 0 para NO): '))
        if op == 0 or op == 1:
            break
        print('Ingrese una opción correcta.')

    if op:
        cajones.append(sum(naranjas_sobrantes))
        print()
        print(f'Ahora tienes {len(cajones)} cajones de naranjas.')
        print()

    camiones, cajones_sobrantes = llenar_camion(cajones)

    print()
    print(f'Se necesitan {len(camiones)} camiones para transportar la cosecha.')

    if cajones_sobrantes:
        print(f'Le sobran {len(cajones_sobrantes)} cajones.')

    print()
    print('Hasta la próxima cosecha.')
    print('Gracias por confiar en mi, Adios :D')
    print()

    print('='*50)


if __name__ == '__main__':
    main()
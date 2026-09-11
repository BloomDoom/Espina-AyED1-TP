'''Una persona desea llevar el control de los gastos realizados al viajar en el subte-
rráneo dentro de un mes. Sabiendo que dicho medio de transporte utiliza un es-
quema de tarifas decrecientes (detalladas en la tabla de abajo) se solicita desarro-
llar una función que reciba como parámetro la cantidad de viajes realizados en un
determinado mes y devuelva el total gastado en viajes. Realizar también un pro-
grama para verificar el comportamiento de la función.'''

def calcular_gasto(viajes: int, valor: int = 4_000) -> float:
    '''
        Contrato:
        Precondicion:
        Postcondicion:
    '''
    precio_con_desc = [
        valor * 0.60,   #40% de descuento
        valor * 0.70,   #30% de descuento
        valor * 0.80    #20% de descuento
        ]

    gasto = 0

    for _ in range(len(precio_con_desc) + 1):
        if viajes > 40:
            exceso = viajes - 40
            gasto += exceso * precio_con_desc[0]
            viajes -= exceso
        elif viajes > 30:
            exceso = viajes - 30
            gasto += exceso * precio_con_desc[1]
            viajes -= exceso
        elif viajes > 20:
            exceso = viajes - 20
            gasto += exceso * precio_con_desc[2]
            viajes -= exceso
        else:
            gasto += viajes * valor
            break
    return gasto
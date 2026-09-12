'''Un comercio de electrodomésticos necesita para su línea de cajas un programa que
le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan
dos números enteros, correspondientes al total de la compra y al dinero recibido.
Informar cuántos billetes de cada denominación deben ser entregados como vuelto,
de tal forma que se minimice la cantidad de billetes. Considerar que existen billetes
de $5000, $1000, $500, $200, $100, $50 y $10. Emitir un mensaje de error si el
dinero recibido fuera insuficiente o si el cambio no pudiera entregarse debido a falta
de billetes con denominaciones adecuadas. Ejemplo: Si la compra es de $3170 y se
abona con $5000, el vuelto debe contener 1 billete de $1000, 1 billete de $500, 1
billete de $200, 1 billete de $100 y 3 billetes de $10.'''

def generar_vuelto(total: int, pago: int) -> tuple[tuple[int, int], ...]:
    '''
        Contrato: Genera el vuelto en la menor cantidad de billetes posibles de denominacion detallada en la variable bills.
        Precondicion: Que el total y el pago no sean 0, y que el pago sea igual o mayor que el total a pagar.
        Postcondicion:  Casos nulos -> Una tupla vacia | Los casos nulos son o por falta de denominacion o no necesidad de vuelto.
                        Caso valido -> Una tupla de tuplas con pares ordenados de cantidad de billetes y su respectiva denominacion de mayor a menor denominacion.
    '''
    assert total > 0, 'El monto debe ser un numero positivo'
    assert pago > 0, 'El pago recibido debe ser un numero positivo'
    assert pago >= total, 'El pago debe ser igual o mayor que el monto a pagar'

    vuelto = pago - total

    if not vuelto:
        print('No hay vuelto que dar')
        return ()

    bills = (5000, 1000, 500, 200, 100, 50, 10)
    denominaciones = len(bills)
    cant_bills = [0] * denominaciones
    
    
    for n in range(denominaciones):
        while vuelto >= bills[n]:
            cant_bills[n] += 1
            vuelto -= bills[n]

    if vuelto:
        print('No hay vuelto adecuado con la denominacion existente')
        return ()
    return tuple(zip(cant_bills, bills))

def main():
    '''Programa principal'''
    while True:
        total = int(input('Ingrese el precio del producto: '))
        if total > 0:
            break
    while True:
        pago = int(input('Ingrese el pago del cliente: '))
        if pago >= total:
            break

    cant_y_denominacion = generar_vuelto(total, pago)

    for i in range(len(cant_y_denominacion)):
        if cant_y_denominacion[i][0]:
            print(f'{cant_y_denominacion[i][0]} billetes de {cant_y_denominacion[i][1]}')
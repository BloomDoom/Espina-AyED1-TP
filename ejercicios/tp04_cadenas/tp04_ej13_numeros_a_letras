'''
Muchas aplicaciones financieras requieren que los números sean expresados tam-
bién en letras. Por ejemplo, el número 2153 puede escribirse como "dos mil ciento
cincuenta y tres". Escribir un programa que utilice una función para convertir un
número entero entre 0 y 1 billón (1.000.000.000.000) a letras. ¿En qué cambiaría
la función si también aceptara números negativos? ¿Y números con decimales?
'''

# Tardé dias en resolver este problema, me rompi la cabeza, aprendi bastante, sigue incompleto..
# Lo mejor que me llevo de acá es que, vale, realmente vale la pena diseñar primero, y codear después.

def _aplicar_escala_millon(n: int) -> str:
    """
    Contrato:
        - Determina si aplica la escala millón, de serlo, la aplica.

    Precondiciones:
        - Un entero.

    Postcondiciones:
        - Un string.
    """
    longitud = len(str(n))

    if longitud <= 3:
        return _tres_digitos(n)
    
    if longitud <= 6:
        return _aplicar_escala_mil(n)

    if n < 2_000_000:
        return f'un millón {_aplicar_escala_mil(n%1_000_000)}'
            
    return f'{_aplicar_escala_mil(n//1_000_000)} millones {_aplicar_escala_mil(n%1_000_000)}'


def _aplicar_escala_mil(n: int) -> str:
    """
    Contrato:
        - Determina si aplica la escala mil, de serlo, la aplica.

    Precondiciones:
        - Un entero.

    Postcondiciones:
        - Un string.
    """

    un = (1, 21, 31, 41, 51, 61, 71, 81, 91)
    
    if n < 1_000:
        return _tres_digitos(n)

    if n < 1_000_000:
        if n == 1_000:
            return 'mil'

        if n < 2_000:
            return f'mil {_tres_digitos(n%1_000)}'

        if (n%100_000)//1_000 in un:
            return f'{_tres_digitos(n//1_000)[:-3] + 'ún'} mil {_tres_digitos(n%1_000)}'

    return f'{_tres_digitos(n//1_000)} mil {_tres_digitos(n%1_000)}'


def _tres_digitos(n: int) -> str:
    """
    Contrato:
        - Recibe un entero positivo menor a mil y lo convierte a string.
        - El string de retorno es lower case.
        - En caso de 0, se devuelve un string vacío
    
    Precondiciones:
        - Un entero donde 0 < n < 1000.

    Postcondiciones:
        - Un string; número recibido pasado a palabras.
    """

    del_1_al_29 = (
        '', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve',
        'diez', 'once', 'doce', 'trece', 'catorce', 'quince', 'dieciséis', 'diecisiete', 'dieciocho', 'diecinueve', 
        'veinte', 'veintiuno', 'veintidós', 'veintitrés', 'veinticuatro', 'veinticinco', 'veintiséis', 'veintisiete', 'veintiocho', 'veintinueve'
        )
    decenas = ('', 'diez', 'veinte', 'treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa') # decenas[0] se mantiene vacío para mantener lógica numérica.
    centenas = ('cien', 'ciento', 'doscientos', 'trescientos', 'cuatrocientos', 'quinientos', 'seiscientos', 'setecientos', 'ochocientos', 'novecientos', )

    u = n % 10              # Unidad
    d = (n // 10) % 10      # Decena
    c = n // 100            # Centena
    du = n % 100            # Decena y unidad
    
    if n == 000:
        return ''
    
    if not n:
        return 'cero'
    
    if 1 <= n <= 29:
        return del_1_al_29[n]

    if n < 100:
        if not u:
            return decenas[d]
        
        return decenas[d] + ' y ' + del_1_al_29[u]

    if n == 100:
        return centenas[0]

    if 0 < du < 30:
        return centenas[c] + ' ' + del_1_al_29[du]

    if d == 0 and u == 0:
        return centenas[c]
    
    if u:
        return centenas[c] + ' ' + decenas[d] + ' y ' + del_1_al_29[u]

    return centenas[c] + ' ' + decenas[d]


def numeros_a_letras() -> None:
    """Programa principal."""
    centrar = 80
    
    print('='*centrar)
    print(f"{'Bienvenido al programa transformar numeros a letras!':^{centrar}}")
    print()
    seguir = 'yo escucho y sigo!'
    while seguir:
        while True:
            try:
                n = int(input('Ingrese el número a traducir: '))
                if 0 <= n <= 1_000_000_000_000:
                    break
                print('Ingrese un número positivo (tope: 1 billón).')
            except ValueError:
                print('Error en la carga de datos, pruebe con un dígito.')
        print()
        print('El resultado del trabajo:')
        if n:
            if n == 1_000_000_000_000:
                print('un billón !!')
            else:
                print(_aplicar_escala_millon(n))
        else:
            print('cero')

        print('Otra vez?')
        seguir = input('Escribe algo para continuar, o ENTER para salir e ir a la explicación final: ')

    print()
    print('Para aceptar números negativos, deberia corroborar si es menor a 0.')
    print('De serlo, le aplico abs() y guardo una flag es_negativo = True.')
    print('Al dar salida por pantalla corroboro if es_negativo.')
    print('De serlo, simplemente escribo menos delante del mismo calculo que si no lo fuera.')
    print()
    print('Y si aceptara decimales, deberia separarlos y aplicar un procedimiento similar' )
    print('al del número entero, marcando la terminacion del mismo con la palabra coma.')
    print('='*centrar)
    

def main() -> None:
    """Programa principal."""
    numeros_a_letras()


if __name__ == '__main__':
    main()
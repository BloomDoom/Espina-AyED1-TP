"""
Se dispone de dos formatos diferentes de archivos de texto en los que se almace-
nan datos de empleados, detallados más abajo. Desarrollar un programa para con-
vertir cada uno de los formatos suministrados, grabando los datos obtenidos en
otro archivo con formato CSV. Los archivos de entrada pueden generarse con Block
de Notas o cualquier otro editor, copiando y pegando los ejemplos proporcionados.
Ambos archivos tienen tres campos por registro: Apellido y Nombre, Fecha de alta
y Domicilio.
Formato 1: Los campos tienen longitud fija con un espacio de separación
entre ellos.
(Regla) 1 2 3 4 5 6
012345678901234567890123456789012345678901234567890123456789012
Pérez Juan 20080211 Corrientes 348
González Ana M 20080115 Juan de Garay 1111 3er piso dto A
Formato 2: Todos los campos de este archivo están precedidos por un
número de dos dígitos que indica la longitud del campo que sigue.
10Pérez Juan082008021114Corrientes 348
14González Ana M082008011533Juan de Garay 1111 3er piso dto A
NOTAS:
∑ Los espacios que se encuentren al final de las cadenas en el formato 1 deberán
ser eliminados.
∑ El formato 2 debe generalizarse para que soporte registros con cualquier canti-
dad de campos.
"""


ANCHOS = {'nombre': 20, 'fecha': 8, 'domicilio': 33}


def _crear_formato1(nombre_archivo: str) -> None:
    """Crea el archivo txt con el formato 1."""
    registros: list[list[str]] = [
        ['Pérez Juan', '20080211', 'Corrientes 348'],
        ['González Ana M', '20080115', 'Juan de Garay 1111 3er piso dto A']
        ]

    try:
        with open(nombre_archivo, 'wt', encoding='utf-8') as arch:
            for nombre, fecha, domicilio in registros:
                arch.write(f'{nombre.ljust(ANCHOS['nombre'])} ')
                arch.write(f'{fecha.ljust(ANCHOS['fecha'])} ')
                arch.write(f'{domicilio.ljust(ANCHOS['domicilio'])}\n')

    except FileNotFoundError:
        print('No se encontro el archivo.')


def _crear_formato2(nombre_archivo: str) -> None:
    """Crea el archivo txt con el formato 2."""
    registros: list[list[str]] = [
        ['Pérez Juan', '20080211', 'Corrientes 348'],
        ['González Ana M', '20080115', 'Juan de Garay 1111 3er piso dto A']
        ]

    try:
        with open(nombre_archivo, 'wt', encoding='utf-8') as arch:
            for registro in registros:
                for dato in registro:
                    n = str(len(dato))
                    arch.write(f'{n.zfill(2)}{dato}')
                arch.write('\n')

    except FileNotFoundError:
        print('No se encontro el archivo.')


def _leer_formato1(linea: str) -> list[str]:
    """
    Contrato:
        - Lee el formato 1 y devuelve una lista con sus registros.

    Precondiciones:
        - Una linea del formato 1.

    Postcondiciones:
        - Una lista con los registros listos para trabajar.
    """
    fin_nombre = ANCHOS['nombre']
    fin_fecha = ANCHOS['fecha'] + ANCHOS['nombre'] + 1

    return [
        linea[:fin_nombre].rstrip(),
        linea[fin_nombre + 1:fin_fecha].rstrip(),
        linea[fin_fecha + 1:].rstrip()
        ]


def _leer_formato2(linea: str) -> list[str]:
    """
    Contrato:
        - Lee el formato 2 y devuelve una lista con sus registros.

    Precondiciones:
        - Una linea del formato 2.

    Postcondiciones:
        - Una lista con los registros listos para trabajar.
    """
    registro: list[str] = []
    i = 0
    linea = linea.rstrip('\n')
    while i < len(linea):
        largo = int(linea[i:i + 2])
        i += 2
        registro.append(linea[i:i + largo])
        i += largo
    
    return registro


def registros_a_csv(registros: list[list[str]], archivo: str, encabezado: list[str]) -> bool:
    """
    Contrato:
        - Dada una matriz de datos, se crea un archivo csv que los contenga.

    Precondiciones:
        - Los registros deben tener la misma cantidad de elementos.

    Postcondiciones:
        - Se crea un archivo .csv con los datos recibidos.
        - Retorna True si se pudo realizar con éxito.
        - Retorna False si hubo un error.
    """

    if not registros or not archivo:
        return False
    
    
    with open(archivo, 'wt', encoding='utf-8') as arch:
        
        arch.write(f'{','.join(encabezado)}\n')
        
        for registro in registros:
            arch.write(f'{','.join(registro)}\n')

    return True


def main() -> None:
    """Programa principal."""
    
    archivo_csv_1: str = 'registros_formato1.csv'
    archivo_csv_2: str = 'registros_formato2.csv'
    encabezado: list[str] = ['Nombre', 'Fecha', 'Domicilio']
    
    _crear_formato1('empleados_formato1.txt')
    _crear_formato2('empleados_formato2.txt')

    registros1: list[list[str]] = []
    registros2: list[list[str]] = []
    
    with open('empleados_formato1.txt', 'rt', encoding='utf-8-sig') as arch:
        for linea in arch:
            registro = _leer_formato1(linea)
            registros1.append(registro)

    with open('empleados_formato2.txt', 'rt', encoding='utf-8-sig') as arch:
        for linea in arch:
            registro = _leer_formato2(linea)
            registros2.append(registro)

    se_pudo1 = registros_a_csv(registros1, archivo_csv_1, encabezado)
    se_pudo2 = registros_a_csv(registros2, archivo_csv_2, encabezado)

    if se_pudo1 and se_pudo2:
        print('El programa corrió con éxito !!')
    else:
        print('Error de capa 8.')


if __name__ == '__main__':
    main()
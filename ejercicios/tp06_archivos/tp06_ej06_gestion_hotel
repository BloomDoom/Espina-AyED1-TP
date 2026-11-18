"""
6. Un hotel necesita un programa para gestionar la operación de sus habitaciones. El hotel
cuenta con 10 pisos y 6 habitaciones por piso. Por cada huésped o grupo familiar que se alo-
ja en el mismo se registra la siguiente información:
∑ DNI del cliente (número entero)
∑ Apellido y Nombre
∑ Fecha de ingreso (DDMMAAAA)
∑ Fecha de egreso (DDMMAAAA)
∑ Cantidad de ocupantes
Se solicita desarrollar un programa para realizar las siguientes tareas:
∑ Registrar el ingreso de huéspedes al hotel, hasta que se ingrese un número de DNI -1.
Esta información deberá grabarse en un archivo CSV donde cada registro incluirá todos
los campos indicados más arriba. Tener en cuenta que los números de DNI no pueden
repetirse y que la fecha de salida debe ser mayor a la de entrada.
∑ Finalizado el ingreso de huéspedes se solicita:
a. Leer el archivo de huéspedes y asignar la habitaciones a cada uno. El piso y
habitación son asignados arbitrariamente, y no puede asignarse una habitación ya
otorgada.
b. Mostrar el piso con mayor cantidad de habitaciones ocupadas.
c. Mostrar cuántas habitaciones vacías hay en todo el hotel.
d. Mostrar el piso con mayor cantidad de personas.
e. Mostrar cuál será la próxima habitación en desocuparse. La fecha actual se ingresa
por teclado. Mostrar todas las que correspondan.
f. Mostrar un listado de todos los huéspedes registrados en el hotel, ordenado por
cantidad de días de alojamiento.
"""

from random import randint as ri
from datetime import date


PISOS = 10
HABITACIONES = 6


def registrar_huespedes(archivo: str) -> None:
    """
    Contrato:
        - Registra huespedes pidiendo sus datos según enunciado

    Precondiciones:
        - Nombre de archivo válido.

    Postcondiciones:
        - Crea un archivo CSV segun nombre recibido por parámetro.
        - De ya existir un archivo con ese nombre, se sobreescribirá.
    """
    dnis: set[int] = set()

    
    with open(archivo, 'wt', encoding='utf-8') as arch:
        while True:
            try:
                dni = int(input('Ingrese DNI (-1 para salir): '))
                if dni < 1:
                    break
                ocupantes = int(input('Ingrese cantidad de huespedes: '))

            except ValueError:
                print('Error, ingrese datos numéricos.')
                continue
            
            nombre = input('Ingrese apellido y nombre: ')
            fecha_ingreso = input('Ingrese fecha de ingreso (DDMMAAAA): ')
            fecha_egreso = input('Ingrese fecha de egreso (DDMMAAAA): ')

            if not _validar_dni(dni, dnis):
                print(f'ERROR: El DNI {dni} ya se encuentra registrado.')
                continue

            if not _validar_fecha(fecha_ingreso, fecha_egreso):
                print(f'ERROR: La salida no puede ser anterior a la llegada.')
                continue
            
            dni, ocupantes = str(dni), str(ocupantes)

            arch.write(f"{','.join([dni, nombre, fecha_ingreso, fecha_egreso, ocupantes])}\n")
            dnis.add(int(dni))


def _validar_dni(dni: int, dnis: set[int]) -> bool:
    """
    Contrato:
        - Valida si el DNI ya se encuentra registrado.
    
    Precondiciones:
        - Existe un conjunto con los DNIS ya registrados.

    Postcondiciones:
        - Si el DNI ya se encuentra registrado, devuelve False.
        - Si el DNI es nuevo, se registra y se devuelve True.
    """

    if dni in dnis:
        return False
    return True


def _validar_fecha(ingreso: str, egreso: str) -> bool:
    """
    Contrato:
        - Valida si la fecha es lógicamente correcta.
        - La fecha debe tener 8 caracteres.

    Precondiciones:
        - Las fechas deben ser strings.

    Postcondiciones:
        - True si ingreso es < a egreso.
        - False si egreso es > a ingreso.
        - False si las fechas no coinciden con el largo DDMMAAAA
        - False si existe error de casteo.

    """
    if len(ingreso) != 8 or len(egreso) != 8:
        return False
    
    try:
        n_ingreso = int(_fecha_ordenable(ingreso))
        n_egreso = int(_fecha_ordenable(egreso))
    except ValueError:
        return False
    
    return n_ingreso < n_egreso


def _fecha_ordenable(fecha: str) -> str:
    """Pasa una fecha de DDMMAAAA a AAAAMMDD."""
    fecha_ordenada = fecha[4:] + fecha[2:4] + fecha[:2]
    return fecha_ordenada


def crear_hotel() -> list[list]:
    """Inicializa el hotel."""
    return [[None] * HABITACIONES for _ in range(PISOS)]


def leer_huespedes(archivo: str) -> list[list]:
    """
    Contrato:
        - Dado el archivo de huespedes.csv transforma sus contenido en una matriz.
    """
    huespedes: list[list[str]] = []
    huesped: list = []

    with open(archivo, 'rt', encoding='utf-8-sig') as arch:
        for linea in arch:
            huesped = linea.rstrip().split(',')
            huesped[0], huesped[4] = int(huesped[0]), int(huesped[4])
            huespedes.append(huesped)

    return huespedes


def asignar_habitaciones(hotel: list[list], huespedes: list[list]) -> None:
    """
    Contrato:
        - Asigna habitaciones a los huespedes de manera aleatoria.

    Precondiciones:
        - El hotel tiene un tope lógico.
    Postcondiciones:
        - Asigna huespedes tanto como el hotel lo permita.
    """
    asignados = 0

    for huesped in huespedes:
        if asignados == PISOS * HABITACIONES:
            print(f'No hay lugar disponible para {huesped[1]}.')
            continue
        while True:
            piso = ri(0, PISOS - 1)
            habitacion = ri(0, HABITACIONES - 1)
            if hotel[piso][habitacion] is None:
                hotel[piso][habitacion] = huesped
                asignados += 1
                break


def piso_mas_ocupado(hotel: list[list]) -> int:
    """Busca cual es el primer piso con mayor ocupación y lo devuelve."""

    mejor_piso = 0
    max_piso = 0
    for i, piso in enumerate(hotel):
        contador = 0
        for habitacion in piso:
            if habitacion:
                contador += 1
        if contador > max_piso:
            mejor_piso = i
            max_piso = contador
    return mejor_piso


def habitaciones_vacias(hotel: list[list]) -> int:
    """Devuelve la cantidad de habitaciones vacías."""
    contador = 0
    for piso in hotel:
        for habitacion in piso:
            if not habitacion:
                contador += 1
    return contador


def piso_mas_personas(hotel: list[list]) -> int:
    """Devuelve el piso con mayor cantidad de huéspedes."""
    mejor_piso = 0
    max_huespedes = 0
    for i, piso in enumerate(hotel):
        huespedes = 0
        for habitacion in piso:
            if habitacion:
                huespedes += habitacion[4]
        if huespedes > max_huespedes:
            max_huespedes = huespedes
            mejor_piso = i
    return mejor_piso


def proxima_a_desocuparse(hotel: list[list], hoy: str) -> None:
    """Muestra por pantalla la primer próxima habitación a desocuparse."""
    fechas: list[str] = []
    for piso in hotel:
        for habitacion in piso:
            if habitacion:
                if _fecha_ordenable(hoy) <= _fecha_ordenable(habitacion[3]):
                    fechas.append(_fecha_ordenable(habitacion[3]))

    if not fechas:
        print('No hay habitaciones a desocuparse desde la fecha ingresada.')
        return
    
    prox_fecha = min(fechas)
    
    print(f"La próxima fecha a desocuparse es: {prox_fecha}.")


def _a_date(fecha: str) -> date:
    """Transforma una fecha en objeto date"""
    dia, mes, anio = int(fecha[:2]), int(fecha[2:4]), int(fecha[4:])

    return date(anio, mes, dia)


def dias_estadia(huesped: list) -> int:
    """Calcula y devuelve la cantidad de dias que se queda un huesped."""

    ingreso = _a_date(huesped[2]) 
    egreso = _a_date(huesped[3])

    return (egreso - ingreso).days


def main() -> None:
    """Programa principal."""
    archivo_huespedes = 'huespedes.csv'
    registrar_huespedes(archivo_huespedes)
    hotel = crear_hotel()
    huespedes = leer_huespedes(archivo_huespedes)
    asignar_habitaciones(hotel, huespedes)

    for piso in hotel:
        print(piso)

    print(f"Piso con más habitaciones ocupadas: {piso_mas_ocupado(hotel) + 1}")
    print(f"Habitaciones vacías: {habitaciones_vacias(hotel)}")
    print(f"Piso con más personas: {piso_mas_personas(hotel) + 1}")

    hoy = input('Ingrese la fecha de hoy (DDMMAAAA): ')
    proxima_a_desocuparse(hotel, hoy)

    huespedes_ordenados = sorted(huespedes, key=dias_estadia)

    print('Los huespedes ordenados por dias de estadia: ')
    for huesped in huespedes_ordenados:
        print(huesped)


if __name__ == '__main__':
    main()
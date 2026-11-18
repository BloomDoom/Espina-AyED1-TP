"""
Desarrollar las siguientes funciones utilizando tuplas para representar fechas y ho-
rarios, y luego escribir un programa que las vincule:
a. Ingresar una fecha desde el teclado, verificando que corresponda a una fecha
válida.
b. Sumar N días a una fecha.
c. Ingresar un horario desde teclado, verificando que sea correcto.
d. Calcular la diferencia entre dos horarios. Si el primer horario fuera mayor al
segundo se considerará que el primero corresponde al día anterior. En ningún
caso la diferencia en horas puede superar las 24 horas.
"""
import datetime as dt


def ingresar_fecha() -> tuple[int, int, int]:
    """
    Contrato:
        - Permite que el usuario ingrese una fecha por teclado.

    Precondiciones:
        - No recibe parámetros.

    Postcondiciones:
        - Devuelve una tupla en orden dia, mes, año.
    """
    while True:
        while True:
            try:
                dia = int(input('Ingrese el dia: '))
                if 0 < dia < 32:
                    break
            except ValueError:
                print('Ingrese un dia válido en dígitos.')

        while True:
            try:
                mes = int(input('Ingrese el mes: '))
                if 0 < mes < 13:
                    break
            except ValueError:
                print('Ingrese un mes válido en dígitos.')

        while True:
            try:
                anio = int(input('Ingrese el año: '))
                if 0 < anio < 2222:
                    break
            except ValueError:
                print('Ingrese un año válido en dígitos.')

        try:
            dt.date(anio, mes, dia)
            return dia, mes, anio
        
        except ValueError:
            print('No es una fecha válida, intente nuevamente.')


def sumar_dias(fecha: tuple[int, int, int], dias: int) -> tuple[int, int, int]:
    """
    Contrato:
        - Suma dias a una fecha.

    Precondiciones:
        - Una fecha válida en formato tupla.
        - Se pueden sumar dias negativos.

    Postcondiciones:
        - Devuelve una nueva tupla con la fecha en orden dia, mes, anio
    """
    dia, mes, anio = fecha
    f = dt.date(anio, mes, dia)

    fecha_nueva = f + dt.timedelta(days=dias)

    return fecha_nueva.day, fecha_nueva.month, fecha_nueva.year


def ingresar_horario() -> tuple[int, int]:
    """
    Contrato:
        - Permite ingresar un horario (horas, minutos) por teclado.
        - Valida que sea un horario válido.

    Precondiciones:
        - No recibe parámetros.

    Postcondiciones:
        - Devuelve una tupla (hora, minuto).
    """

    while True:
        try:
            hora = int(input('Ingrese una hora (formato 24hs): '))
            if 0 <= hora <= 23:
                break
        except ValueError:
            print('Ingrese una hora válida.')
    
    while True:
        try:
            minuto = int(input('Ingrese minutos: '))
            if 0 <= minuto <= 59:
                break
        except ValueError:
            print('Ingrese minutos válidos.')

    return hora, minuto


def diferencia_entre_horarios(horario1: tuple[int, int], horario2: tuple[int, int]) -> tuple[int, int]:
    """
    Contrato:
        - Calcula la diferencia entre 2 horarios.

    Precondiciones:
        - Los horarios deben respetar el formato hora, minuto.
        
    Postcondiciones:
        - Devuelve hora, minutos de diferencia.
    """

    hora1, minutos1 = horario1
    hora2, minutos2 = horario2

    minutos1 += hora1 * 60
    minutos2 += hora2 * 60

    dif = minutos2 - minutos1
    if dif < 0:
        dif += 1440
    dif_hora = dif // 60
    dif_minutos = dif % 60

    return dif_hora, dif_minutos


def main() -> None:
    """
    A. Ingresar una fecha desde el teclado, verificando que corresponda
    a una fecha válida.
    
    B. Sumar N días a una fecha.
    
    C. Ingresar un horario desde teclado, verificando que sea correcto.
    
    D. Calcular la diferencia entre dos horarios. Si el primer horario
    fuera mayor al segundo se considerará que el primero corresponde al
    día anterior. En ningún caso la diferencia en horas puede superar
    las 24 horas.
    """
    print('Bienvenido.')
    print('Vamos a resolver las 4 consignas.')
    print('A.')
    fecha = ingresar_fecha()
    dia, mes, anio = fecha
    print(f'Fecha ingresada: {dia}/{mes}/{anio}')
    print()
    print()
    print('B.')

    while True:
        try:
            n = int(input('Ingrese los dias a sumar: '))
            break
        except ValueError:
            print('ERROR: Ingrese un dato numérico.')
    dia, mes, anio = sumar_dias(fecha, n)
    print()
    print(f"La nueva fecha es: {dia}/{mes}/{anio}.")
    print()
    print()
    print('C.')
    horario1 = ingresar_horario()
    print(f"{horario1[0]}:{horario1[1]}")
    print()
    print()
    print('D.')
    print('Ingrese un nuevo horario: ')
    horario2 = ingresar_horario()
    dif_hora, dif_minutos = diferencia_entre_horarios(horario1, horario2)
    print('La diferencia es de:')
    print(f"HORAS: {dif_hora}")
    print(f"MINUTOS: {dif_minutos}")


if __name__ == '__main__':
    main()
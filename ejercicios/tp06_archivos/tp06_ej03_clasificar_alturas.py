"""
Una institución deportiva necesita clasificar a sus atletas para
inscribirlos en los próximos juegos panamericanos.
Para eso encargó la realización de un programa que incluya las
siguientes funciones:

grabar_rango_alturas(): Graba en un archivo las alturas de los atletas
de distintas disciplinas, los que se ingresan desde el teclado.
Cada dato se debe grabar en una linea distinta.

grabar_promedio(): Graba en un archivo los promedios de las alturas de
los atletas, leyendo los datos del archivo generado en el paso anterior.
La disciplina y el promedio debe grabarse en lineas diferentes.

mostrar_mas_altos(): Muestra por pantalla las disciplinas deportivas
cuyos atletas superan la estatura promedio general.

Obtener los datos del segundo archivo.
"""

def _ingresar_cadena(msg: str) -> str:
    """
    Contrato:
        - Permite ingresar datos por teclado.

    Precondiciones:
        - Recibe un string, mensaje de input.

    Postcondiciones:
        - str; devuelve el dato ingresado por teclado.
    """
    return input(msg)


def grabar_rango_alturas(deportes: list[str], altura_file: str) -> bool:
    """
    Contrato:
        - Graba en un archivo (si no existe, lo crea) las alturas de los distintos atletas de las distintas disciplinas.

    Precondiciones:
        - Un conjunto de str: Conjunto de disciplinas a grabar.

    Postcondiciones:
        - True si se pudo realizar las acciones correctamente.
        - False si hubo error de grabado o no hay acciones a realizar.
    """
    if not deportes:
        return False

    with open(altura_file, "wt", encoding="utf-8") as arch:
        
        for deporte in deportes:
            arch.write(deporte + "\n")
            print(f"Deporte: {deporte}")

            while True:
                altura = _ingresar_cadena("Ingrese la altura del atleta (-1 para salir): ")

                if altura == "-1":
                    break
                
                arch.write(altura + "\n")

        return True


def grabar_promedio(deportes: list[str], altura_file: str, prom_file: str) -> bool:
    """
    Contrato:
        - Graba en un archivo (si no existe, lo crea) el promedio de las
        alturas de los atletas de las distintas disciplinas.

    Precondiciones:
        - Un conjunto de str: Conjunto de disciplinas a grabar.

    Postcondiciones:
        - True si se pudo realizar las acciones correctamente.
        - False si hubo error de grabado o no hay acciones a realizar.
    """
    if not deportes:
        return False
    
    try:
        with open(altura_file, "rt", encoding="utf-8-sig") as arch:
            with open(prom_file, "wt", encoding="utf-8") as prom:

                prom.write(arch.readline())
                acumulador = 0
                contador = 0

                for linea in arch:
                    if linea.strip() in deportes:
                        if contador:
                            prom.write(str(acumulador/contador) + "\n")
                        else:
                            prom.write("0\n")
                        acumulador = 0
                        contador = 0
                        prom.write(linea)

                    else:
                        acumulador += float(linea)
                        contador += 1
                
                if contador: 
                    prom.write(str(acumulador/contador) + "\n")
                else:
                    prom.write("0\n")

    except FileNotFoundError:
        print(f"El archivo {altura_file} no existe en este directorio.")

    return True


def mostrar_mas_altos(deportes: list[str], altura_file: str, promedio_file: str) -> bool:
    """
    Contrato:
        - Muestra los atletas que superan la altura promedio de su deporte.

    Precondiciones:
        - Un conjunto de strings; los deportes existentes.
        - El archivo de alturas.
        - El archivo de promedio.

    Postcondiciones:
        - True si se pudo realizar las acciones correctamente.
        - False si hubo error de grabado o no hay acciones a realizar.
    """
    if not deportes:
        return False

    disciplina_promedio = {}
    try:
        with open(promedio_file, "rt", encoding='utf-8-sig') as prom:
            while True:
                disciplina = prom.readline()

                if not disciplina:
                    break

                promedio = prom.readline()
                
                try:
                    disciplina_promedio[disciplina.strip()] = float(promedio)
                except ValueError:
                    print(f'La disciplina {disciplina.strip()} no tiene alturas registradas.')

    except FileNotFoundError:
        print(f'No se encontró el archivo {promedio_file}.')
        return False

    mas_altos = {}
    deporte_actual = deportes[0]
    try:
        with open(altura_file, "rt", encoding='utf-8-sig') as alt:
            for linea in alt:
                if linea.strip() in deportes:
                    deporte_actual = linea.strip()
                    mas_altos[deporte_actual] = []

                else:   
                    try:
                        altura = float(linea.strip())
                    except ValueError:
                        print(f'La disciplina {deporte_actual} no tiene alturas registradas.')
                        break
                    
                    if altura > disciplina_promedio[deporte_actual]:
                        mas_altos[deporte_actual].append(altura)

                    

    except FileNotFoundError:
        print(f'No se encontró el archivo {altura_file}.')
        return False

    for deporte, alturas in mas_altos.items():
        print(f'Los que superan el promedio de su disciplina ({deporte}) son:')
        print(alturas)
        print()

    return True


def main() -> None:
    """Programa principal."""
    deportes = ["Fútbol", "Básquetbol", "Waterpolo", "Judo"]
    altura_file = "alturas_por_deporte.txt"
    prom_file = "promedio_por_deporte.txt"
    
    si_alturas = grabar_rango_alturas(deportes, altura_file) 
    si_promedios = grabar_promedio(deportes, altura_file, prom_file)
    si_mas_altos = mostrar_mas_altos(deportes, altura_file, prom_file)



if __name__ == "__main__":
    main()
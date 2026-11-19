"""
Escribir un programa que lea un archivo de texto conteniendo un conjunto de ape-
llidos y nombres en formato "Apellido, Nombre" y guarde en el archivo
ARMENIA.TXT los registros de aquellas personas cuyo apellido termina con la cade-
na "IAN", en el archivo ITALIA.TXT los terminados en "INI" y en ESPAÑA.TXT los
terminados en "EZ". Descartar el resto. Ejemplo:
Arslanian, Gustavo –> ARMENIA.TXT
Rossini, Giuseppe –> ITALIA.TXT
Pérez, Juan –> ESPAÑA.TXT
Smith, John –> descartar
El archivo puede ser creado mediante el Block de Notas o el cualquier otro editor.
"""


def crear_archivo() -> bool:
    """Crea un archivo con nombres y apellidos en formato csv"""

    try:
        with open('ejercicios/tp06_archivos/personas.csv', 'w', encoding='utf-8') as arch:
            nombres = [
                'Arslanian, Gustavo',
                'Rossini, Guiseppe',
                'Pérez, Juan',
                'Smith, John',
                'Gonzalez, Karen',
                'Espina, Agustin',
                'Francisco, Mariano',
                'Sini, Tini',
                'Fian, Gian'
            ]
            arch.write('\n'.join(nombres))
        return True
    except:
        return False

def clasificar_personas() -> None:
    """Clasifica según nacionalidad."""

    paises = {'IAN': 'ARMENIA.TXT', 'INI': 'ITALIA.TXT', 'EZ': 'ESPAÑA.TXT'}

    with open('ejercicios/tp06_archivos/personas.csv', 'r', encoding='utf-8-sig') as arch:
        
        for linea in arch:
            for terminacion, pais in paises.items():
                apellido = linea.split(',')[0]
                if apellido.upper().endswith(terminacion):
                    with open(f'ejercicios/tp06_archivos/{pais}', 'a', encoding='utf-8') as p:
                        p.write(linea)


def main() -> None:
    """Programa principal."""
    crear_archivo()
    clasificar_personas()


if __name__ == '__main__':
    main()
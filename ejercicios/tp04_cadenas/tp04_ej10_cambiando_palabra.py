'''
Desarrollar una función para reemplazar todas las apariciones de una palabra por
otra en una cadena de caracteres y devolver la cadena obtenida y un entero con la
cantidad de reemplazos realizados. Tener en cuenta que sólo deben reemplazarse
palabras completas, y no fragmentos de palabras. Escribir también un programa
para verificar el comportamiento de la función.
'''

def reemplazar_palabra(cadena: str, a_cambiar: str, reemplazo: str) -> str:
    """
    Contrato:
        - Reemplaza una palabra por otra en una cadena.

    Precondiciones:
        - Una cadena a trabajar.
        - Una cadena; palabra a reemplazar.
        - Una cadena; reemplazo.

    Postcondiciones:
        - Una cadena.
    """
    lista = cadena.lower().split()
    salida = []
    
    for palabra in lista:
        if palabra == a_cambiar:
            salida.append(reemplazo)
            continue
        salida.append(palabra)

    return ' '.join(salida)


def main() -> None:
    """Programa principal."""
    centrar = 80
    
    print('='*centrar)
    print(f"{'Bienvenido al programa para reemplazar palabras por otras!':^{centrar}}")
    print()
    s = input('Ingrese la frase a trabajar: ')
    a_cambiar = input('Ingrese la palabra a reemplazar: ')
    reemplazo = input('Ingrese la palabra que reemplazaría la anterior: ')
    print()
    print('El resultado del trabajo:')
    print(reemplazar_palabra(s, a_cambiar, reemplazo))
    print('='*centrar)
    

if __name__ == '__main__':
    main()
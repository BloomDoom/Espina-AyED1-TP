"""
Crear una función contarvocales(), que reciba una palabra y cuente cuántas vocales
contiene, identificando la cantidad de cada una. Devolver un diccionario con los
resultados. Luego desarrollar un programa para leer una frase e invocar a la
función por cada palabra que contenga la misma. Imprimir las palabras y la
cantidad de vocales hallada.
"""
def contar_vocales(palabra: str) -> dict[str, int]:
    """
    Contrato:
        - Cuenta cuantas vocales tiene cada palabra.

    Precondiciones:
        - La palabra debe ser un string con contenido.

    Postocondiciones:
        - Devuelve un diccionario vocal:cantidad.
    """

    vocales: tuple[str, ...] = ('a', 'e', 'i', 'o', 'u')
    salida: dict[str, int] = {vocal:0 for vocal in vocales}
    for letra in palabra.lower():
        if letra in vocales:
            for vocal in vocales:
                if vocal == letra:
                    salida[vocal] += 1
    return salida


def main() -> None:
    """Programa principal."""
    print('Contaremos las vocales que tenga una frase que vos digas, '
          'palabra por palabra.')

    frase = input('Ingresa una frase: ').split()
    frase_procesada: dict[str, dict[str, int]] = {}
    
    if not frase:
        print('No ingresaste ninguna frase :(')
        return
    
    for palabra in frase:
        dicc = contar_vocales(palabra)
        frase_procesada[palabra] = dicc
    
    print()
    print('Ahora analizaremos la palabra.')
    print('Analizando. . . .')
    print()
    
    for palabra in frase:
        print(f"Palabra: {palabra}")
        for vocal, cantidad in frase_procesada[palabra].items():
            if cantidad != 1:
                print(f"La vocal {vocal} aparece {cantidad} veces.")
            else:
                print(f"La vocal {vocal} aparece {cantidad} vez.")
        print()


if __name__ == '__main__':
    main()
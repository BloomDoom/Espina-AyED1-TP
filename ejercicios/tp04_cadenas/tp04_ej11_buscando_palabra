'''
Escribir un programa que cuente cuántas veces se encuentra una subcadena dentro
de otra cadena, sin diferenciar mayúsculas y minúsculas. Tener en cuenta que los
caracteres de la subcadena no necesariamente deben estar en forma consecutiva
dentro de la cadena, pero sí respetando el orden de los mismos. Ejemplo:
Cadena:
Platero es pequeño, peludo, suave; tan blando por fuera, que se diría todo de algodón, que no lleva
huesos. Sólo los espejos de azabache de sus ojos son duros cual dos escarabajos de cristal negro.
Sub-cadena: UADE
Cantidad encontrada: 4 (Las coincidencias están resaltadas en la cadena siguiente)
Platero es pequeño, peludo, suave; tan blando por fuera, que se diría todo de algodón, que no lleva
huesos. Sólo los espejos de azabache de sus ojos son duros cual dos escarabajos de cristal negro.
'''

def buscar_palabra(frase: str, palabra: str) -> tuple[int, str]:
    """
    Contrato:
        - En base a una 'frase' recibida, busca la cantida de veces que aparece la 'palabra' recibida.
        - Devuelve la cantidad de veces que se encontró de manera consecutiva y la frase remarcando las coincidencias.

    Precondiciones:
        - Una cadena; frase a trabajar.
        - Una cadena; palabra a buscar en la frase.

    Postcondiciones:
        - Una tupla; siendo el primer elemento un entero (cantidad de coincidencias), y el segundo una cadena (frase remarcada).
    """

    j = 0
    indices: list[int] = []
    
    for i, letra in enumerate(frase.upper()):
        if letra == palabra[j].upper():
            indices.append(i)
            j += 1
        if j == len(palabra):
            j = 0

    while j > 0:
        indices.pop()
        j -= 1
    
    salida = ''

    for i in indices:
        salida += frase[j:i] + "\033[1m" + frase[i].upper() + "\033[0m"
        j = i + 1
    
    salida += frase[j:]

    return len(indices) // len(palabra), salida


def main() -> None:
    """Programa principal."""
    centrar = 80
    
    print('='*centrar)
    print(f"{'Bienvenido al programa para buscar palabras en una frase!':^{centrar}}")
    print()
    frase = input('Ingrese la frase a trabajar: ')

    while True:
        palabra = input('Ingrese la palabra a buscar: ')
        if palabra:
            break
        print('Ingrese una palabra a buscar.')

    print()
    print('El resultado del trabajo:')
    
    coincidencias, texto = buscar_palabra(frase, palabra)

    if coincidencias != 1:
        print(f'Se encontró la palabra completa {coincidencias} veces.')
    else:
        print(f'Se encontró la palabra completa {coincidencias} vez.')
    print(texto)
    print('='*centrar)
    

if __name__ == '__main__':
    main()
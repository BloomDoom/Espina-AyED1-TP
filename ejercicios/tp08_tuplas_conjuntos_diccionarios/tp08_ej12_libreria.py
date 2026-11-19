"""
Una librería almacena su lista de precios en un diccionario. Diseñar un programa
para crearlo, incrementar los precios de los cuadernos en un 15%, imprimir un
listado con todos los elementos de la lista de precios e indicar cuál es el ítem más
costoso que venden en el comercio.
"""

def main() -> None:
    """Libreria principal."""

    cuadernos: dict[str, float] = {
        'Rojo': 1500,
        'Verde': 1700,
        'Azul': 2000,
        'Amarillo': 1300,
        'Blanco': 1100,
        'Plateado': 2300,
        'Dorado': 3000
    }
    print('Bienvenido a tu libreria.')
    print()
    print('Tenes estos cuardernos por el momento:')
    for color, precio in cuadernos.items():
        print(f"Color: {color} // Precio: {precio}")

    print()
    print('Los precios de los cuadernos subieron un 15%!')
    print()
    print('Actualizando. . . .')
    print()

    for color in cuadernos.keys():
        cuadernos[color] *= 1.15

    print('Listo!')
    print()
    print('La lista de precios actualizados de los cuadernos:')
    for color, precio in cuadernos.items():
        print(f"Color: {color} // Precio: {precio:.2f}")

    print()
    print('El ítem mas caro de la libreria es:')
    max_precio = 0
    max_color = ''
    for color, precio in cuadernos.items():
        if precio > max_precio:
            max_precio = precio
            max_color = color
    print(f"El cuaderno {max_color} con un precio de {max_precio:.2f}.")


if __name__ == '__main__':
    main()
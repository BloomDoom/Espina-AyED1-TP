"""
Escribir un programa que juegue con el usuario a adivinar un número. El programa
debe generar un número al azar entre 1 y 500 y el usuario debe adivinarlo. Para
eso, cada vez que se introduce un valor se muestra un mensaje indicando si el nú-
mero que tiene que adivinar es mayor o menor que el ingresado. Cuando consiga
adivinarlo, se debe imprimir en pantalla la cantidad de intentos que le tomó hallar
el número. Si el usuario introduce algo que no sea un número se mostrará un
mensaje en pantalla y se lo contará como un intento más.
"""

from random import randint as ri


def _ingresar_valor() -> tuple[int, int]:
    """Permite al usuario ingresar un número entero por teclado"""

    contador = 1
    while True:
        try:
            return int(input("Ingrese un número entero: ")), contador

        except ValueError:
            print("Intenta nuevamente con un número.")
            print("¡No desperdicies intentos!")
            contador += 1


def juego() -> None:
    """
    Contrato:
        - Juego de adivinanza para el usuario.
        - Se elije un número aleatorio entre 1 y 500.
        - El usuario juega a adivinarlo.

    Precondiciones:
        - No recibe parámetros.

    Postcondiciones:
        - No retorna nada.
    """

    print()
    print("¡Bienvenido al random guesser!")
    print("En este juego tienes que tratar de adivinar un número.")
    print("El mismo se encuentra entre 1 y 500.")
    print("¿Podras adivinarlo en 1 intento?")
    print("¡Exitos!")
    print()
    seguir = True

    while seguir:
        print("¿Que número tengo en mente?")
        adiviname = ri(1, 500)
        intentos = 0

        while True:
            n, intento = _ingresar_valor()
            intentos += intento

            if n < adiviname:
                print("El número ingresado es menor.")

            elif n > adiviname:
                print("El número ingresado es mayor.")

            elif n == adiviname:
                print("¡Acertaste!")
                if intentos > 1:
                    print(f"Te tomó {intentos} intentos")
                    break
                else:
                    print("¡Lo lograste en el primer intento! ¡Felicitaciones!")
                    break
        seguir = not (input("ENTER para seguir jugando, ingresa algo para salir: "))


def main() -> None:
    """Programa principal."""
    juego()


if __name__ == "__main__":
    main()

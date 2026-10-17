"""
Todo programa Python es susceptible de ser interrumpido mediante la
pulsación de las teclas Ctrl-C, lo que genera una excepción del tipo
KeyboardInterrupt. Realizar un programa para imprimir los números
enteros entre 1 y 100000, y que solicite confirmación al usuario antes
de detenerse cuando se presione Ctrl-C.
"""


def main() -> None:
    """Programa principal."""

    for n in range(1, 100_001):
        try:
            print(n)

        except KeyboardInterrupt:
            detenerse = input(
                'Presione ENTER para seguir. Ingrese algo para detener: '
                )
            if detenerse:
                break


if __name__ == '__main__':
    main()
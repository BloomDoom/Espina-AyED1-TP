'''
Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos),
donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valores de la lista.
'''

def main() -> None:
     """
     Funcion principal.
     
     - Crea una lista con los cuadrados de los números entre 1 y N (incluyente).
     - Pide que N lo ingrese el usuario
     - Imprime los últimos 10 valores de la lista.
     """
     print('='*50)
     print('Bienvenido.')
     print()
     n = int(input('Ingrese un número entero: '))

     cuadrados = [x**2 for x in range(1, n + 1)]
     print('Los últimos 10 valores de la lista son:')
     print(cuadrados[-10:])


if __name__ == '__main__':
    main()
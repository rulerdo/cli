import sys

def saludo(nombre: str):

    print('Hola',nombre)


def encuentra_pares(x: int):

    lista_pares = list()

    for num in range(x + 1):
        if num % 2 == 0:
            lista_pares.append(num)

    print(f'Numeros pares en el rango 0-{x}: {lista_pares}')


if __name__ == '__main__':

    try:

        nombre = sys.argv[1]
        x = int(sys.argv[2])
        saludo(nombre)
        encuentra_pares(x)

    except:
        print('ERROR DE EJECUCION!\n    python syscli.py [nombre] [x]')

from argparse import ArgumentParser

def obtener_args():

    parser = ArgumentParser(description="Argumentos para el programa que saluda y encuentra pares")
    parser.add_argument("--nombre",required=True, help="Nombre de usuario")
    parser.add_argument("--limite",required=True, help="Limite superior del rango de numeros a calcular", type=int)

    args = parser.parse_args()

    return args


def saludo(nombre: str):

    print('Hola',nombre)


def encuentra_pares(x: int):

    lista_pares = list()

    for num in range(x + 1):
        if num % 2 == 0:
            lista_pares.append(num)

    print(f'Numeros pares en el rango 0-{x}: {lista_pares}')

args = obtener_args()
# print(args)

nombre = args.nombre
x = args.limite
saludo(nombre)
encuentra_pares(x)
# Importamos funcion ArgumentParser
from argparse import ArgumentParser

# Funcion para procesar los argumentos
def obtener_args():

    # Definicion de los argumentos
    parser = ArgumentParser(description="Argumentos para el programa que saluda y encuentra pares")
    parser.add_argument("--nombre",'-n', required=True, help="Nombre de usuario")
    parser.add_argument("--limite", '-l', required=True, help="Limite superior del rango de numeros a calcular", type=int)
    parser.add_argument("--apellido", "-a", help="Apellido de usuario")
    parser.add_argument("--genero", "-g", choices=["F", "M", "NB"], default="NB", help="Genero del usuario")
    parser.add_argument("--verbose", "-v", action="store_true", help="Presenta detalle de calculos en la terminal")

    # Parseo de los argumentos
    args = parser.parse_args()

    return args
    
# Funcion para saludar al usuario
def saludo(args):

    # Obtenemos la informacion que necesitamos de los argumentos
    n = args.nombre
    a = args.apellido if args.apellido else ''
    g = args.genero

    # Diccionario para saludar al usario considerando el genero
    hola = {
        'F': 'Hola estimada',
        'M': 'Hola estimado',
        'NB': 'Hola estimade',
    }

    # Impresion del saludo
    print(hola[g],n,a)

# Funcion para encontrar los numeros pares
def encuentra_pares(args):

    # Obtenemos la informacion que necesitamos de los argumentos
    x = args.limite
    v = args.verbose

    # Lista para guardar los numeros pares
    lista_pares = list()

    # Logica para encontrar numeros pares
    for num in range(x + 1):

        if (num % 2) == 0:

            if v: print(f'{num}: es un numero par') # Evaluamos si el usuario quiere el modo verbose
            lista_pares.append(num)

        else:

            if v: print(f'{num}: es un numero inpar') # Evaluamos si el usuario quiere el modo verbose

    # Impresion de los numeros pares encontrados
    print(f'Numeros pares en el rango 0-{x}: {lista_pares}')


if __name__ == '__main__':

    # Ejecucion de nuestras funciones
    args = obtener_args()
  
    saludo(args)
    encuentra_pares(args)

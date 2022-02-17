def saludo(nombre: str):

    print('Hola',nombre)
    
def encuentra_pares(x: int):

    lista_pares = list()

    for num in range(x + 1):
        if num % 2 == 0:
            lista_pares.append(num)

    print(f'Numeros pares en el rango 0-{x}: {lista_pares}')

nombre = 'Rulerdo'
x = 13

saludo(nombre)
encuentra_pares(x)

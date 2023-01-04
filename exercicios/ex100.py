from random import randint
números = list()
def sorteia(lista):
    print(f'Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        sort = randint(0,9)
        lista.append(sort)
        print(sort, end= ' ')
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


sorteia(números)
somaPar(números)
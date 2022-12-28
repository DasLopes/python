'''Faça um programa que ajude um jogador da MEGA SENA a criar papites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''

print('-' * 40)
print('{:^10}'.format('JOGA NA MEGA SENA'))
print('-' * 40)

from random import randint
numSort = []
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=' * 5, f'SORTEANDO {jogos} JOGOS', '-=' * 5)
for c in range(1, jogos+1):
    print(f'Jogo {c}: ', end='')
    while len(numSort) < 6:    
        num = randint(1,60)
        if num not in numSort:
            numSort.append(num)
    numSort.sort()
    print(f'{numSort}')
    numSort.clear()
print('-=' * 6, '< BOA SORTE! > ', '-=' * 6)
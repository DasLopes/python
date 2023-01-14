'''
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''

from random import randint

cont = 0
while True:
    print('=-' * 15)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('=-' * 15)
    computador = randint(0, 9)
    num = int(input('Diga um valor: '))
    tot = computador + num
    while True:
        jogador = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
        if jogador in 'PI':
            break
    if tot % 2 == 0:
        resp = 'PAR'
    else:
        resp = 'ÍMPAR'
    print('--' * 15)
    print(f'Você jogou {num} e o computador {computador}.')
    print(f'Total de {tot} deu {resp}.')
    print('--' * 15)
    if jogador == 'P' and resp == 'PAR' or jogador == 'I' and resp == 'ÍMPAR':
        print('você VENCEU')
        print('Vamos jogar novamente...')
        cont += 1
    else:
        print('Você PERDEU!')
        break
print('=-' * 15)
print(f'GAME OVER! Você venceu {cont} vezes.')

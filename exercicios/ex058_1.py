'''Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0, 10. só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
versão do professor'''

from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você conseguir adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    palpites += 1
    jogador = int(input('Qual é seu palpite? '))
    if jogador == computador:
        acertou = True
    else:
        if computador > jogador:
            print('O computador pensou em um número maior')
        else:
            print('O computador pensou em um número menor.')        
print('acertou com {} tentativas. Parabéns!'.format(palpites))
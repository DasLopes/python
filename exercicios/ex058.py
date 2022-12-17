'''Faça o computador pensar em um número entre 0 e 10. O jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''

import random, time

computador = random.randrange(0, 10)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)

jogador = -1
palpites = 0

while computador != jogador:
    jogador = int(input('Em que número eu pensei? '))
    print('PROCESSANDO...')
    time.sleep(0.2)
    palpites += 1
print('Você ganhou com {} tentativas.'.format(palpites))

'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''

from random import choice

lista = ['pedra', 'papel', 'tesoura']
computador = choice(lista)

jogador = str(input('Jokenpô: '))
if computador == jogador:
    print('Jogue novamente')
elif computador == 'pedra' and jogador == 'tesoura':
    print('computador ganhou')
elif computador == 'pedra' and jogador == 'papel':
    print('jogador ganhou')
elif computador == 'papel' and jogador == 'pedra':
    print('computador ganhou')
elif computador == 'papel' and jogador == 'tesoura':
    print('jogador ganhou')
elif computador == 'tesoura' and jogador == 'papel':
    print('computador ganhou')
elif computador == 'tesoura' and jogador == 'pedra':
    print('jogador ganhou')
else:
    print('Você deve digitar (pedra, papel ou tesoura)')

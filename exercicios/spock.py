'''As regras de Pedra-papel-tesoura-lagarto-Spock são:

Tesoura corta papel
Tesoura decapita lagarto
Papel cobre pedra
Papel refuta Spock
Pedra esmaga lagarto
Pedra amassa tesoura
Lagarto envenena Spock
Lagarto come papel
Spock esmaga (ou derrete) tesoura
Spock vaporiza pedra
'''

#from random import randint
import random
lista = ['pedra', 'tesoura', 'papel', 'lagarto', 'spock']
computador = random.choice(lista)
print(computador)
print('Você tem 3 tentativas...')
tentativas = 3
ganhou = False
while tentativas != 0 and ganhou != True:
    jogador = 'papel'#str(input('Faça sua escolha: ')).strip().lower()
    if jogador == 'pedra':
        if computador == 'papel':
            print('Papel cobre pedra. Tente novamente.')
        elif computador == 'tesoura':
            ganhou = True
            print('Pedra amassa tesoura')
        elif computador == 'lagarto':
            print('Pedra esmaga lagarto')
            ganhou = True
        elif computador == 'spock':
            print('Spock vaporiza pedra. Tente novamente.')
        else:
            print('Empate. ganhou mais uma chace.')
            tentativas += 1
    elif jogador == 'papel':
        if computador == 'pedra':
            print('Papel cobre pedra. Tente novamente.')
            ganhou = True
        elif computador == 'tesoura':            
            print('Tesoura corta papel')
        elif computador == 'lagarto':
            print('Lagarto come papel')            
        elif computador == 'spock':
            print('Papel refuta Spock')
            ganhou = True
        else:
            print('Empate. ganhou mais uma chace.')
            tentativas += 1
    else:
        print('Você digitou {}.'.format(jogador))
        print('Opções válidas: pedra, papel, tesoura, lagarto, spock')
    tentativas -= 1
if tentativas == 0:
    print('Não foi dessa vez')
else:
    print('Parabéns. Você ganhou com {} tentativas.'.format(tentativas))





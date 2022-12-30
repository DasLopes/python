'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''
from random import randint
from operator import itemgetter
jogo = {
    'jogador1': randint(1,6),
    'jogador2': randint(1,6),
    'jogador3': randint(1,6),
    'jogador4': randint(1,6)
}
print('Valores sorteados:')
for j, p in jogo.items():
    print(f'{j} tirou {p} no dado')
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
ranking = []
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
for i, v in enumerate(ranking):
    print(f'  {i+1}º lugar: {v[0]} com {v[1]}')

'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''

cadastro = dict()
gols = list()
cadastro['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {cadastro["nome"]} jogou? '))
for c in range(0, partidas):
    gols.append(int(input(f'\tQuantos gols na partida {c}? ')))    
cadastro['gols'] = gols[:]
cadastro['total'] = sum(gols)
print('-=' * 30)
print(cadastro)
print('-=' * 30)
for k, v in cadastro.items():
    print(f'O {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {cadastro["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(gols):
    print(f'\t=> Na partica {i}, fez {v} gols.')
print(f'Foi um total de {cadastro["total"]} gols.')
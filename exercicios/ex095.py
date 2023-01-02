'''
Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''
cadastro = dict()
gols = list()
jogadores = list()
while True:
    cadastro.clear()
    gols.clear()
    cadastro['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {cadastro["nome"]} jogou? '))
    for c in range(0, partidas):
        gols.append(int(input(f'\tQuantos gols na partida {c + 1}? ')))    
    cadastro['gols'] = gols[:]
    cadastro['total'] = sum(gols)
    jogadores.append(cadastro.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
    if resp in 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in cadastro.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:    
    cod = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if cod == 999:
        break        
    if cod >= len(jogadores):
        print(f'ERRO! Não existe jogador número {cod}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[cod]["nome"]}')
        for k, v in enumerate(jogadores[cod]['gols']):
            print(f'No jogo {k + 1} fez {v} gols.')
    print('-' * 40)
print('<<< volte sempre >>>')

cadastro = dict()
gols = list()
jogadores = [{'nome': 'Ronaldinho', 'gols': [2, 3, 2], 'total': 7}, {'nome': 'Ronaldo', 'gols': [3,1], 'total': 4}, {'nome': 'Vampeta', 'gols': [0, 0, 2, 2], 'total': 4}, {'nome': 'Kaká', 'gols': [3], 'total': 3}]

'''while True:
    cadastro['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {cadastro["nome"]} jogou? '))
    for c in range(0, partidas):
        gols.append(int(input(f'\tQuantos gols na partida {c}? ')))    
    cadastro['gols'] = gols[:]
    cadastro['total'] = sum(gols)
    jogadores.append(cadastro.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
    if resp in 'N':
        break'''
print()
print('-=' * 30)
print('cod\tnome\t\tgols\t\ttotal')
print('-' * 50)
for c in range(0, len(jogadores)):
    print(f'{c}\t{jogadores[c]}')
print('-' * 50)


while True:
    while True:
        cod = int(input('Mostrar dados de qual jogador? (999 para parar) '))
        if cod < len(jogadores) or cod == 999:
            break
    if cod == 999:
        break
    print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[cod]["nome"]}')
    for c in jogadores[cod]:
        if c in gols:
            for i in c:
                print(f'{i} - {c[i]}')

'''print(f'O jogador {cadastro["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(gols):
    print(f'\t=> Na partica {i}, fez {v} gols.')
print(f'Foi um total de {cadastro["total"]} gols.')'''
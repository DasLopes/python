'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Santos.
'''

lista = 'Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico Paranaense', 'Atlético Mineiro', 'Fortaleza', 'São Paulo', 'América', 'Botafogo', 'Santos', 'Goiás', 'Red Bull Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético', 'Avaí', 'Juventude'

print('-=' * 20)
print(f'Lista de times do Brasileirão: {lista}')
print('-=' * 20)
print(f'Os 5 primeiros são {lista[:5]}')
print('-=' * 20)
print(f'Os 4 últimos são {lista[-4:]}')
print('-=' * 20)
print(f'Times em ordem alfabética: {sorted(lista)}')
print('-=' * 20)
print(f'O Santos está na {lista.index("Santos")+1}ª posição')

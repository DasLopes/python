nome = str(input('Qual é o seu nome? '))
if nome == 'Robson':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo' or nome == 'Miguel':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claúdia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))
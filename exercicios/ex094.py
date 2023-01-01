dict = dict()
list = list()
while True:
    dict['nome'] = str(input('Nome: '))
    while True:
        dict['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if dict['sexo'] in 'MF':
            break
    dict['idade'] = int(input('Idade: '))
    list.append(dict.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
    if resp in 'N':
        break
print(f'dict: {dict}')
print(f'list: {list}')
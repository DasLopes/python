'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
a) Quantos pessoas cadastrados.
b) A média de idade.
c) Uma lista com mulheres.
d) Uma lista com idade acima da média.
'''

dict = {}
list = []
totIdade = 0
totMulheres = []
while True:
    dict.clear()
    dict['nome'] = str(input('Nome: '))
    while True:
        dict['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if dict['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')    
    dict['idade'] = int(input('Idade: '))
    totIdade += dict['idade']
    list.append(dict.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp in 'N':
        break
média = totIdade / len(list)
print('-=' * 30)
print(f'a) Ao todo temos {len(list)} pessoas cadastradas.')
print(f'b) A média de idade é de {média:.1f} anos.')
print('c) As mulheres cadastradas foram ', end='')
for c in list:
    if c['sexo'] in 'F':
        print(f'{"nome"} ', end='')
print()
print('d) Lista das pessoas que estão acima da média:')
for c in list:
    if c['idade'] >= média:
        print('     ', end='')
        for k, v in c.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
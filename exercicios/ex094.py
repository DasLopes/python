dict = {}
list = []
totIdade = 0
totMulheres = []
while True:
    dict['nome'] = str(input('Nome: '))
    while True:
        dict['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if dict['sexo'] in 'MF':
            break
        else:
            print('ERRO! Por favor, digite apenas M ou F.')
    if dict['sexo'] in 'F':
        totMulheres.append(dict['nome'])
    dict['idade'] = int(input('Idade: '))
    totIdade += dict['idade']
    list.append(dict.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        else:
            print('ERRO! Responda apenas S ou N.')
    if resp in 'N':
        break
média = totIdade / len(list)
print('-=' * 30)
print(f'a) Ao todo temos {len(list)} pessoas cadastradas.')
print(f'b) A média de idade é de {média:.1f} anos.')
print(f'c) As mulheres cadastradas foram {totMulheres}')
print('d) Lista das pessoas que estão acima da média:')
for c in range(0, len(list)):
    if list[c]['idade'] > 24:
        print(list[c])

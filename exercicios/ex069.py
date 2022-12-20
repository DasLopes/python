'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

a) Quantas pessoas tem mais de 18 anos.
b) Quanto homens foram cadastrados.
c) Quantas mulheres tem menos de 20 anos.'''
pessoaMaior18 = totHomens = totMulher20 = 0
while True:
    print('-' * 30)
    print(' ' * 5, 'CADASTRE UMA PESSOA')
    print('-' * 30)
    
    idade = int(input('Idade: '))
    while True:
        sexo = str(input('Sexo: [M/F] '))
        if sexo in 'MmFf':
            break    
    while True:
        continuar = str(input('Quer continuar? [S/N]'))
        if continuar in 'SsNn':
            break
    if idade > 18:
        pessoaMaior18 += 1
    if sexo in 'Mm':
        totHomens += 1
    if sexo in 'Ff':
        if idade < 20:
            totMulher20 += 1
    if continuar in 'Nn':
        break    
print('====== FIM DO PROGRAMA ======')
print(f'Total de pessoas com mais de 18 anos: {pessoaMaior18}')
print(f'Ao todo temos {totHomens} homens cadastrados.')
print(f'E temos {totMulher20} mulheres com menos de 20 anos.')
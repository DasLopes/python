'''
Desenvolva um programa que leia o nome, idade, e sexo de 4 pessoas. No final do programa, mostre:

A média de idade do grupo.
Qual é o nome do homem mais velho.
Quantas mulheres tem menos de 20 anos idade.

Versão: Professor
'''

somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ''
totMulher20 = 0

for c in range(1, 5):
    print('---- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaIdade += idade
    if c == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totMulher20 += 1
médiaIdade = somaIdade / 4
print('A média de idade do grupo é de {} anos'.format(médiaIdade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maiorIdadeHomem, nomeVelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totMulher20))

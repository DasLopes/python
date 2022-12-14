'''
Desenvolva um programa que leia o nome, idade, e sexo de 4 pessoas. No final do programa, mostre:

A média de idade do grupo.
Qual é o nome do homem mais velho.
Quantas mulheres tem menos de 20 anos idade.
'''
totIdade = 0
pessoas = 4
maior = 0
nomeMaior = ' '
qtdMulheres = 0
for c in range(1, pessoas + 1):
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Qual o sexo: [M/F')).strip().upper()

    totIdade += idade
    if sexo == 'M':
        if c == 1:
            maior = idade
            nomeMaior = nome
        else:
            if maior < idade:
                maior = idade
                nomeMaior = nome
    else:
        if idade < 20:
            qtdMulheres += 1

media = totIdade / pessoas
print('O grupo tem uma média de {} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior, nomeMaior))
print('A lista tem {} mulheres abaixo de 20 anos.'.format(qtdMulheres))
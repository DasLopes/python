'''
Desenvolva um programa que leia o nome, idade, e sexo de 4 pessoas. No final do programa, mostre:

A média de idade do grupo.
Qual é o nome do homem mais velho.
Quantas mulheres tem menos de 20 anos idade.
'''
totIdade = 0
pessoas = 2
maior = 0
nomeMaior = ' '
qtdMulheres = 0
for c in range(0, pessoas):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Qual o sexo: ')).upper()

    totIdade += idade
    if sexo == 'M':
        if c == 0:
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
print('O Sr. {} é o homem mais velho.'.format(nomeMaior))
print('A lista tem {} mulheres abaixo de 20 anos.'.format(qtdMulheres))
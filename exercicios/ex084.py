'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

a) Quantas pessoas foram cadastradas.
b) Uma listagem com as pessoas mais pesadas.
c) Uma listagem com as pessoas mais leves.'''

pessoas = []
dados = []
maiorpeso = menorpeso = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))    
    if len(pessoas) == 0:
        maiorpeso = menorpeso = dados[1]
    else:
        if dados[1] > maiorpeso:
            maiorpeso = dados[1]            
        if dados[1] <= menorpeso:
            menorpeso = dados[1]        
    pessoas.append(dados[:])
    dados.clear()
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar in 'N':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi de {maiorpeso}Kg peso de ', end='')
for p in pessoas:
    if p[1] == maiorpeso:
        print(f'{p[0]}', end=' ')
print(f'\nO menor peso foi de {menorpeso}Kg peso de ', end='')
for p in pessoas:
    if p[1] == menorpeso:
        print(f'{p[0]}', end=' ')
'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
from datetime import date
anoAtual = date.today().year
menor = 0
maior = 0
for c in range(0, 7):
    anoNasc = int(input('Em que ano nasceu? '))
    idade = anoAtual - anoNasc
    if idade < 18:
        menor += 1
    else:
        maior += 1
print('{} pessoas são menores de idade.'.format(menor))
print('{} pessoas são maiores de idade'.format(maior))
'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

Observação: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print('=' * 40)
print(' ' * 15, 'BANCO CEV')
print('=' * 40)

saque = int(input('Que valor você quer sacar? R$'))

ced50 = saque // 50
ced20 = (saque % 50) // 20
ced10 = (saque % 20) // 10
ced1 = (saque % 10) // 1

if ced50 > 0:
    print(f'Total de {ced50} cédulas de R$50')
if ced20 > 0:
    print(f'Total de {ced20} cédulas de R$20')
if ced10 > 0:
    print(f'Total de {ced10} cédulas de R$10')
if ced1 > 0:
    print(f'Total de {ced1} cédulas de R$1')

print('=' * 40)
print('Volte sempre ao BANCO CEV!')
print('Tenha um bom dia!')
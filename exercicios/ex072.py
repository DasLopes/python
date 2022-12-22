'''Crie um programa que tenha um tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.

Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

lista = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'


while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if num < 0 or num > 20:
            print('Tente novamente. ', end='')
        else:
            print(f'Você digitou o número {lista[num]}')
            break    
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar in 'N':
        break

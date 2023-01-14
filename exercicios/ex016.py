'''
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
'''

'''from math import trunc
num = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}'.format(num, trunc(num)))
'''

'''
num = float(input('Digite um número: '))
print('O valor digitado foi {} e a sua porção inteira é {:.0f}.'.format(num, num))
'''

num = float(input('Digite um número: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))

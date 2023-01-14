'''
Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
'''

termo = int(input('Digite um número inteiro: '))
fib1 = 0
fib2 = 1
fib3 = 0
cont = 2
print('Sequência Fibonacci: 0 -> 1 -> ', end='')
while cont != termo:
    fib3 = fib1 + fib2
    fib1 = fib2
    fib2 = fib3
    print(fib3, ' -> ', end='')
    cont += 1
print('ACABOU')
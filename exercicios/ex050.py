'''
Desenvolva um programa que leia SEIS números inteiros e mostre a SOMA apenas daqueles que forem PARES. Se o valor digitado for ímpar, desconsidere-o.'''
s = 0
for c in range(0, 6):
    n = int(input('Digite um número: '))    
    if n % 2 == 0:
        s = s + n
print('Soma: {}'.format(s))
'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.
'''

fatorial = int(input('Digite um número: '))
print('Fatorial {}!: {} x '.format(fatorial, fatorial), end='')
cont = fatorial
while cont != 1:
    fatorial = fatorial * (cont - 1)
    cont -= 1
    print(cont, 'x ', end='')
print(' = ', fatorial)
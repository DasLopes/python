'''Faça um programa que leia um número qualquer e mostre o seu fatorial

Ex:
5!=5x4x3x2x1=120'''

fatorial = int(input('Digite um número: '))
print('Fatorial: ', fatorial, ' ', end='')
cont = fatorial
while cont != 1:
    fatorial = fatorial * (cont - 1)
    cont -= 1
    print(cont, ' ', end='')
print(' = ', fatorial)
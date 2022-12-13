'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''

#n = int(input('Digite um número: '))
for c in range(1,50):
    if c != 1:
        if c == 2 or c == 3 or c == 5 or c == 7:
            print(c, end=' ')
        else:
            if c % 2 != 0 and c % 3 != 0 and c % 5 != 0 and c % 7 != 0:
                print(c, end=' ')
        
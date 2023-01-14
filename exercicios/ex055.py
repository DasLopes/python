'''
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
'''
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Peso {}ª pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if maior < peso:
            maior = peso
        else:
            menor = peso
print('Maior: {}'.format(maior))
print('Menor: {}'.format(menor))
'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA (progressão aritmética). No final, mostre os 10 primeiros termos dessa progressão.
ex: (1, 4, 7, 10, 13, ...) a1 é igual a 1 e a razão r é igual a 3.
'''
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão

for c in range(primeiro, décimo + razão, razão):
    print('{} '.format(c), end='=> ')
print('ACABOU')
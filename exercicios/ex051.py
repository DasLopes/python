'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA (progressão aritmetica). No final, mostre os 10 primeiros termos dessa progressão.
ex: (1, 4, 7, 10, 13, ...) a1 é igual a 1 e a razão r é igual a 3.
'''
a = 1
r = 3
print('1 ->', end='')
for c in range(1, 10):
    a = r + a
    print('{} -> '.format(a), end='')
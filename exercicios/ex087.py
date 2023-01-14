'''
Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''

from random import randint
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = randint(1,9)
print('-=' * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
pares = 0
for l in range(0,3):
    for c in range(0,3):
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
tercol = 0
for l in range(0,3):    
    tercol += matriz[l][2]    
maiseglin = 0
for c in range(0,3):
    if matriz[1][c] > maiseglin:
        maiseglin = matriz[1][c]
print('-=' * 30)
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {tercol}')
print(f'O maior valor da segunda linha é {maiseglin}')

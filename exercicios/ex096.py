'''
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
'''

def area(l, c):
    s = l * c
    print(f'A área de um terreno {l:.1f} x {c:.1f} é de {s:.1f}m².')


print('  Controle de Terrenos')
print('-' * 30)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l,c)
'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
'''

#import ex107.moeda as moeda #codigo editado pelo vsconde
import moeda

num = float(input('Digite o preço: R$'))
print(f'A metade de R${num} é {moeda.metade(num)}')
print(f'O dobro de R${num} é {moeda.dobro(num)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(num, 10)}')
print(f'Reduzindo 10%, temos R${moeda.diminuir(num, 10)}')
'''
Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
'''

import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de R${moeda.moeda(p)} é R${moeda.metade(p, True)}')
print(f'O dobro de R${moeda.moeda(p)} é R${moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p, 10, True)}')
print(f'Diminuindo 10%, temos R${moeda.diminuir(p, 10, True)}')
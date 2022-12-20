'''n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
#print('A soma vale {}'.format(s))
print(f'A soma vale {s}')'''

nome = 'José'
idade = 33
salário = 987.3
'''print(f'O {nome} tem {idade} anos.') #PYTHON 3.6+
print('O {} tem {} anos.'.format(nome, idade)) #PYTHON 3
print('O %s tem %d anos.' % (nome, idade)) #PYTHON 2'''

print(f'O {nome:^20} tem {idade} anos e ganha R${salário:.2f}') #nome alinhamento centralizado
print(f'O {nome:>20} tem {idade} anos e ganha R${salário:.2f}') #nome alinhado à direita
print(f'O {nome:<20} tem {idade} anos e ganha R${salário:.2f}') #nome alinhado à esquerda

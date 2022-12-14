'''
Refaça o desafio 009, mostrando uma tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
'''
n = int(input('Digite um número: '))
for c in range(1,11):
    print('{} x {:2} = {}'.format(n, c, n * c))
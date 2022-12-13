'''
Refaça o desafio 009, mostrando oa tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
'''
n = int(input('Digite um número: '))
for c in range(1,10+1):
    print('{} x {} = {}'.format(n, c, (n * c)))
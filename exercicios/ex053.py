'''
Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.
exemplos:
apos a sopa
a sacada da casa
a torre da derrota
o lobo ama o bolo
anoratam a data da maratona
'''
frase = 'a torre da derrota'.strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = junto[::-1]
print('O inverso de "{}" é "{}".'.format(junto, inverso))
if frase == inverso:
    print('A frase é um palindromo')
else:
    print('A frase não é um palindromo')

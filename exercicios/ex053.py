'''
Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.
exemplos:
apos a sopa
a sacada da casa
a torre da derrota
o lobo ama o bolo
anoratam a data da maratona
'''
frase1 = 'apos a sopa'.upper()
frase2 = frase1[::-1]
print(frase1, ' = ', frase2)
if frase1 == frase2:
    print('palindromo')
else:
    print('não forma palindromo')

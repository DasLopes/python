'''
Faça um programa que calcule a soma entre TODOS OS NÚMEROS ÍMPARES que são MÚLTIPLOS DE TRÊS e que se encontram no intervalo de 1 até 500.
'''
soma = 0
cont = 0
for c in range(1,501, 2):    
    if c % 3 == 0:
        cont += 1
        soma += c
print('Entramos {} números.'.format(cont))        
print('A soma é: {}'.format(soma))
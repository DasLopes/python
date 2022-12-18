'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

num = 0
cont = 0
soma = 0
flag = 0
while flag != 999:
    
    num = int(input('Digite um número: '))    
    if num == 999:
        flag = num
    else:
        cont += 1
        soma += num

print('Os número digitados foram {} e a soma entre eles foi {}.'.format(cont, soma))
print('')
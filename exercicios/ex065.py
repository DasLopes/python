'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor dos valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

continuar = 'S'
cont = maior = menor = tot = 0
while continuar in 'Ss':    
    num = int(input('Digite um número inteiro: '))
    tot += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if maior < num:
            maior = num
        if menor > num:
            menor = num
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while continuar not in 'SsNn':
        print('opção inválida')
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
media = tot / cont
print('Você digitou {} números e a média foi {}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))

'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor dos valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

continuar = 'SIM'
cont = 0
maior = 0
menor = 0
tot = 0
while continuar == 'SIM':    
    num = int(input('Digite um número inteiro: '))
    tot += num
    if cont == 0:
        maior = num
        menor = num
    else:
        if maior < num:
            maior = num
        elif menor > num:
            menor = num
    continuar = str(input('Deseja continuar? [SIM/NÃO]')).upper()
    cont += 1
media = tot / cont
print('A média dos números digitados foi: {}'.format(media))
print('O maior número digitado foi: {}'.format(maior))
print('O menor número digitado foi: {}'.format(menor))
'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
a) Quantos números foram digitados.
b) A lista de valores, ordenada de forma decrescente.
c) Se o valor 5 foi digitado e está ou não na lista.'''
lista = []
cont = 0
while True:
    cont += 1
    n = int(input('Digite um valor: '))
    lista.append(n)
    while True:
        r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if r in 'SN':
            break
    if r in 'N':
        break
print(f'Você digitou {cont} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
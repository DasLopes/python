'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

lista = []
maior = menor = 0
for c in range(0,5):
    lista.append(int(input('Digite um número: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print(f'Você digitou os valors {lista}')
print(f'O maior número encontrado foi {maior} nas posições: ', end='')
for c, l in enumerate(lista):
    if l == maior:
        print(c, end=' ')
print(f'\nO menor número encontrado foi {menor} nas posições: ', end='')
for c, l in enumerate(lista):
    if l == menor:
        print(c, end=' ')

'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''
from random import randint
lista = []
for l in range(0,5):
    lista.append(randint(0,9))
print(lista)
maior = menor = 0
posMenor = posMaior = 0
for c, l in enumerate(lista):
    if c == 0:
        maior = l
        menor = l
    else:
        if maior < l:
            maior = l
            posMaior = c
        if menor > l:
            menor = l
            posMenor = c
print(f'O maior número {maior} foi encontrado na posição {posMaior}.')
print(f'O menor número {menor} foi encontrado na posição {posMenor}.')
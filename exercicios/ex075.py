'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

a) Quantas vezes apareceu o valor 9.
b) Em que posição foi digitado o primeiro valor 3.
c) Quais foram os números pares.'''

lista = (   int(input('Digite um número: ')), 
            int(input('Digite outro número: ')),
            int(input('Digite mais um número: ')),
            int(input('Digite o último número: ')))
print(f'Você digitou os valores {lista}')
print(f'O valor 9 apareceu {lista.count(9)} vezes')
if 3 in lista:
    print(f'o valor 3 apareceu na {lista.index(3)+1}ª posição')
else:
    print('O valor 3 não foi encontrado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for p in lista:
    if p % 2 == 0:
        print(p, end=' ')

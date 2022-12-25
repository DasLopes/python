'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

lista = []
cont = 0

while True:
    lista.append(int(input('Digite um número: ')))
    
    
    while True:
        continuar = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar in 'N':
        break
    cont += 1
print(f'Lista: {lista}')
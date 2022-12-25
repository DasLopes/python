'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

números = []
while True:
    n = int(input('Digite um número: '))
    if n not in números:
        números.append(n)
        print('Número adicionado com sucesso...')
    else:
        print('Número duplicado, não adicionado')

    while True:
        r = str(input('Desejar continuar? [S/N] ')).strip().upper()[0]
        if r in 'SN':
            break
    if r in 'N':
        break
números.sort()
print(f'Você digitou os valores {números}')
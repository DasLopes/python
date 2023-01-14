'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
'''

print('-' * 40)
print(' ' * 10, 'LOJA SUPER BARATÃO')
print('-' * 40)
totCompra = cont = contMenor = menorPreço = 0
while True:
    contMenor += 1
    nome = str(input('Nome do Produto:'))
    preço = float(input('Preço: R$'))
    totCompra += preço
    if preço > 1000:        
        cont += 1
    if contMenor == 1:
        menorPreço = preço
    else:
        if preço < menorPreço:
            menorPreço = preço
            nomeMenorPreço = nome
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar in 'N':
        break
print('-' * 10, 'FIM DO PROGRAMA', '-' * 10)
print(f'O total da compra foi R${totCompra:.2f}')
print(f'Temos {cont} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomeMenorPreço} que custa R${menorPreço}')
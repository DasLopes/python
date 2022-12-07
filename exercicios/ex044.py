print('=' * 60)
print('Condições enquanto durar o estoque:')
print('=' * 60)

print('[ 1 ] À vista (dinheiro / cheque / pix) 10% de desconto')
print('[ 2 ] À vista no cartão: 5% de desconto')
print('[ 3 ] Em até 2x no cartão: preço normal')
print('[ 4 ] 3x ou mais no cartão: 20% de juros')
print('=' * 60)
#valor = float(input('Qual o valor do produto? '))
compra = 100
opção = int(input('Qual a forma de pagamento? '))

if opção == 1:
    desc = compra / 100 * 10
    valor = compra - desc
    print('Para a compra no valor de R${}, com a opção [ {} ] você obteve {}% de desconto.'.format(compra, opção, desc))
elif opção == 2:
    desc = compra / 100 * 5
    valor = compra - desc
    print('Para a compra no valor de R${}, com a opção [ {} ] você obteve {}% de desconto.'.format(compra, opção, desc))
elif opção == 3:
    desc = 0
    valor = compra
    print('Para a compra no valor de R${}, com a opção [ {} ] você obteve {}% de desconto.'.format(compra, opção, desc))
elif opção == 4:
    acres = compra / 100 * 20
    valor = compra + acres
    print('Para a compra no valor de R${}, com a opção [ {} ] você terá um acrescimo de {}%.'.format(compra, opção, acres))
else:
    print('Opção inválida')
    valor = 0

print('Valor da compra atualizado: R${:.2f}'.format(valor))

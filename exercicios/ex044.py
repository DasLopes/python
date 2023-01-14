'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
'''

print('{:=^40}'.format(' LOJAS AMARELINHAS '))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] À vista (dinheiro / cheque / pix) 10% de desconto')
[ 2 ] À vista no cartão: 5% de desconto')
[ 3 ] Em até 2x no cartão: preço normal')
[ 4 ] 3x ou mais no cartão: 20% de juros''')
opção = int(input('Qual a forma de pagamento? '))
if opção != 1 and opção !=2 and opção != 3 and opção != 4:
    print('Opção inválida')
elif opção == 1:    
    total = preço - (preço / 100 * 10)
elif opção == 2:
    total = preço - (preço / 100 * 5)
elif opção == 3:
    total = preço
    valorParc = total / 2
    print('Sua compra será parcelada em 2x de R${}.'.format(valorParc))
elif opção == 4:
    total = preço + (preço / 100 * 20)
    totParc = int(input('Em quantas vezes deseja parcelar? '))
    valorParc = total / totParc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(totParc, valorParc))
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, total))
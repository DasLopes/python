'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''

casa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o seu salário? '))
tempo = int(input('Em quantos anos deseja pagar? '))
prestacao = casa / (tempo * 12)
minimo = salario / 100 * 30
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, tempo))
print('A prestação será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Emprestímo APROVADO.')
else:
    print('Emprestímo NEGADO.')
'''
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
'''

salario = float(input('Qual é o salário do funcionário? R$ '))
novoSalario = salario + (salario / 100 * 15)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}.'.format(salario, novoSalario))

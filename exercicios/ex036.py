casa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o seu salário? '))
tempo = int(input('Em quantos anos deseja pagar? ')) * 12
prestacao = casa / tempo

print('A prestação do emprestimo será R${:.2f}.'.format(prestacao))
if prestacao > (salario / 100 * 30):
    print('Emprestímo negado.')
else:
    print('Emprestímo aprovado.')
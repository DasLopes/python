import uteis

num = float(input('Digite o preço: R$'))
print(f'A metade de R${num} é {uteis.metade(num)}')
print(f'O dobro de R${num} é {uteis.dobro(num)}')
print(f'Aumentando 10%, tem R$ {uteis.aumento(num)}')
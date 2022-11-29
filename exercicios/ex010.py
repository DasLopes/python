real = float(input('Quanto dinheiro você tem na carteira? R$ '))
cotacao = 5.40
dolar = real / cotacao
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))

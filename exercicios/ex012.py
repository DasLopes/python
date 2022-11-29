preco = float(input('Qual é o preço do produto? R$'))
desc = float(input('Qual é o percentual de desconto? '))
npreco = preco - (preco / 100 * desc)
print('O produto que custava R${:.2f}, na promoção com desconto de {:.2f}% vai custar R${:.2f}'.format(preco, desc, npreco))

import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de R${p} é R${moeda.metade}')
print(f'O dobro de R${p} é R${moeda.dobro}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p, 10)}')
print(f'Diminuindo 10%, temos R${moeda.diminuir(p, 10)}')
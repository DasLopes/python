saque = int(input('Que valor você quer sacar? R$'))

ced50 = saque // 50
ced20 = (saque - (ced50 * 50)) // 20
ced10 = ((saque - (ced50 * 50)) % 20) // 10
ced1 = ((saque - (ced50 * 50)) % 20) % 10

if ced50 > 0:
    print(f'Total de {ced50} cédulas de R$50')
if ced20 > 0:
    print(f'Total de {ced20} cédulas de R$20')
if ced10 > 0:
    print(f'Total de {ced10} cédulas de R$10')
if ced1 > 0:
    print(f'Total de {ced1} cédulas de R$1')

print('=' * 40)
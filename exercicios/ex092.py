'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''

from datetime import datetime
ficha = {}
ficha['nome'] = str(input('Nome: '))
ficha['idade'] = datetime.now().year - int(input('Ano de Nascimento: '))
ficha['ctps'] = int(input('carteira de Trabalho (0 não tem): '))
if ficha['ctps'] != 0:
    ficha['contratação'] = int(input('Ano de Contratação: '))
    ficha['Salário'] = float(input('Salário: R$'))
    ficha['aposentadoria'] = ficha['idade'] + ((ficha['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in ficha.items():
    print(f'{k} tem o valor {v}')

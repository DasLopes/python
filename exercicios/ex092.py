import datetime

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
ano = date.year
ficha = {}
ficha['nome'] = str(input('Nome: '))
ficha['idade'] = ano - int(input('Ano de Nascimento: '))
ficha['ctps'] = int(input('carteira de Trabalho (0 não tem): '))
if ficha['ctps'] != 0:
    ficha['contratação'] = int(input('Ano de Contratação: '))
    ficha['Salário'] = float(input('Salário: R$'))
    ficha['aposentadoria'] = (ficha['contratação'] + 65) - ano
print('-=' * 30)
for k, v in ficha.items():
    print(f'{k} tem o valor {v}')


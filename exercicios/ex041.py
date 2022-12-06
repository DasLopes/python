from datetime import date
anoAtual = date.today().year
anoNasc = int(input('Digite seu ano de nascimento: '))
idade = anoAtual - anoNasc

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade == 20:
    print('SÊNIOR')
else:
    print('MASTER')
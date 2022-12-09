from datetime import date
anoAtual = date.today().year
anoNasc = int(input('Digite seu ano de nascimento: '))
idade = anoAtual - anoNasc
print('O atleta em {} anos.'.format(idade))
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
from datetime import date
anoAtual = date.today().year
anoNasc = int(input('Em que ano nasceu? '))
sexo = str(input('Sexo: [m / f] '))
idade = anoAtual - anoNasc

if sexo == 'f':
    print('Quem nasceu em {} tem {} anos em {}.'.format(anoNasc, idade, anoAtual))
    print('Você não precisa se alistar')
elif sexo == 'm':
    print('Quem nasceu em {} tem {} anos em {}.'.format(anoNasc, idade, anoAtual))
    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        print('Ainda faltam {} anos para o alistamento'.format(saldo))
        ano = anoAtual + saldo
        print('Seu alistamento será em {}.'.format(ano))
    elif idade > 18:
        saldo = idade - 18
        print('Você já deveria ter se alistado há {} anos.'.format(saldo))
        ano = anoAtual - saldo
        print('Seu alistamento foi em {}.'.format(ano))
else:
    print('opção inválida')
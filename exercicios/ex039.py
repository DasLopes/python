from datetime import date
anoAtual = date.today().year
anoNasc = int(input('Em que ano nasceu? '))
idade = anoAtual - anoNasc

if idade < 18:
    print('Ainda vai se alistar no serviço militar')
    print('Faltam {} para seu alistamento'.format(18 - idade))
elif idade > 18:
    print('Já passou do tempo de se alistar')
    print('Você passou {} anos do seu alistamento'.format(idade - 18))
else:
    print('Chegou o ano do seu alistamento')
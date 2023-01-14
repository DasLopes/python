'''
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela. 
'''

ficha = {}
ficha['nome'] = str(input('Nome: '))
ficha['média'] = float(input(f'Média de {ficha["nome"]}: '))
if ficha['média'] < 5:
    ficha['situação'] = 'reprovado'
elif ficha['média'] < 7:
    ficha['situação'] = 'recuperação'
else:
    ficha['situação'] = 'aprovado'
print('-=' * 40)
for k, v in ficha.items():
    print(f'  - {k} é igual a {v}')

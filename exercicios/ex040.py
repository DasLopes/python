'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
'''

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Com as notas {} e {} sua média será {}'.format(nota1, nota2, media))
if media >= 7:
    print('APROVADO')
elif media < 5:
    print('REPROVADO')
else:
    print('RECUPERAÇÃO')
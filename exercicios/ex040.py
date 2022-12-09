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
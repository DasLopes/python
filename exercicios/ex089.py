'''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
'''

lista = []
completa = []
while True:    
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Nota1: ')))
    lista.append(float(input('Nota2: ')))
    completa.append(lista[:])
    lista.clear()
    while True:
        r = str(input('Continuar? [S/N]')).strip().upper()[0]
        if r in 'SN':
            break
    if r in 'N':
        break
print('-' * 30)
print('Nº\tNOME\t\tMÉDIA')
print('-' * 30)
for c in range(0, len(completa)):
    media = (completa[c][1] + completa[c][2]) / 2
    print(f'{c}\t{completa[c][0]}\t\t{media:.1f}')
print('-' * 30)
while True:
    num = int(input('Mostrar notas de qual aluno? (999 interrompe): '))       
    if num == 999:
        break
    print(f'Notas de {completa[num][num]} são {completa[num][1]:.1f}, {completa[num][2]:.1f}')
    
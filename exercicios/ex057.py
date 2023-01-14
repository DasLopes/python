'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''

sx = False
while sx == False:
    sexo = str(input('Digite o sexo: [M/F] ')).upper()
    if sexo == 'F' or sexo == 'M':
        sx = True    
print('Sexo {} registrado.'.format(sexo))
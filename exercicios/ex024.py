'''
Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
'''

cid = str(input('Em que cidade você nasceu? ')).strip().upper()
print('SANTO' in cid) #primeira solução
print(cid[:5] == 'SANTO') #segunda solução
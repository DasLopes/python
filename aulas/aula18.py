'''pessoas = [['pedro', 25], ['maria', 19], ['joão', 32]]
print(pessoas[0][0]) #pedro
print(pessoas[1][1]) #19
print(pessoas[2][0]) #joão
print(pessoas[1]) #['maria', 19]'''

################################################ PRATICA ########################################

'''teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''

############################################## PRATICA 2 ########################################

#galera = [['joão', 19], ['filó', 33], ['joaquim', 13], ['gerusa', 45]]
'''print(galera[0])
print(galera[0][0])
print(galera[0][1])
print(galera[1])
print(galera[1][0])
print(galera[1][1])
print(galera[2])
print(galera[2][0])
print(galera[2][1])
print(galera[3])
print(galera[3][0])
print(galera[3][1])'''

#for p in galera:
#    print(f'{p[0]} tem {p[1]} anos de idade.')

############################################ PRATICA 3 ##########################################

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'dado: {dado}')
print(f'Temos {totmai} maiores e {totmen} menores de idade.')
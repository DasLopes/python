################################ PRÁTICA 1 ################################
print('{:#^100}'.format(' PRÁTICA 1 '))

pessoas = {'nome': 'Robson', 'sexo': 'M', 'idade': 37}
print(pessoas) #{'nome': 'Robson', 'sexo': 'M', 'idade': 37}
print(pessoas['nome']) #Robson
print(pessoas['idade']) #37
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.') #O Robson tem 37 anos.
print(pessoas.keys()) #dict_keys(['nome', 'sexo', 'idade'])
print(pessoas.values()) #dict_values(['Robson', 'M', 37])
print(pessoas.items()) #dict_items([('nome', 'Robson'), ('sexo', 'M'), ('idade', 37)])
for k in pessoas.keys():
    print(k)
'''
nome
sexo
idade
'''
for v in pessoas.values():
    print(v)
'''
Robson
M
37
'''
del pessoas['sexo'] #apaga o item sexo com o seu conteúdo
pessoas['nome'] = 'Miguel' #substitui o conteúdo de nome 'robson' por 'miguel'
pessoas['peso'] = 72.5 #adiciona um elemento com o seu conteúdo
for k, v in pessoas.items():
    print(f'{k} = {v}')
'''
nome = Robson
sexo = M
idade = 37
'''
############################################### PRÁTICA 2 ############################################################
print('{:#^100}'.format(' PRÁTICA 2 '))

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(estado1) #{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
print(estado2) #{'uf': 'São Paulo', 'sigla': 'SP'}
print(brasil) #[{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}, {'uf': 'São Paulo', 'sigla': 'SP'}]
print(brasil[0]) #{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
print(brasil[1]) #{'uf': 'São Paulo', 'sigla': 'SP'}
print(brasil[0]['uf']) #Rio de Janeiro
print(brasil[1]['sigla']) #SP

############################################### PRÁTICA 3 ############################################################
print('{:#^100}'.format(' PRÁTICA 3 '))

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
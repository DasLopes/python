print('''Anotações''')

lanche = ['hamburger', 'suco', 'pizza', 'pudim']
print(lanche)
lanche[3] = 'picolé' #substitui o elemento da posição 3
print(lanche)
lanche.append('cuke') #adiciona um elemento após a última posição da lista
print(lanche)
lanche.insert(0, 'cachorro quente') #adiciona um elemento na posição 0, deslocando os demais para a direita
print(lanche)
del lanche[3] #apaga um elemento na 3 posição e reposiciona os demais
print(lanche)
lanche.pop(3) #apaga um elemento na posição 3 e reposiciona os demais
print(lanche)
lanche.remove('suco')
print(lanche) #remove um elemento, independente da posição na qual se encontra e reposiciona os demais
lanche.pop() #remove o último elemento da lista e seu indice
print(lanche)
if 'pizza' in lanche: #remove o item 'pizza' se ele estiver na lista
    lanche.remove('pizza')

valores1 = list(range(4, 11, 2)) #adiciona elementos de 4 a 11, pulando de 2 em 2 de forma ordenada
print(valores1)

valores2 = [8,2,5,4,9,3,0]
print(valores2)
valores2.sort() #coloca os elementos em ordem
print(valores2)
valores2.sort(reverse=True) #coloca os elementos em ordem inversa
print(valores2)
tamanho = len(valores2)
print(tamanho)


print('Parte prática 1')

num = [2,5,9,1,5,8,2]
num[2] = 3 #substitui o elemento da posição 2 pelo número 3
num.append(7) #adiciona o elemento 7 na última posição da lista
num.sort() #coloca todos os elementos da lista em ordem
num.sort(reverse=True) #coloca os elementos da lista em ordem reversa
num.insert(2, 2) #insere o valor 0 na posição 2
num.remove(2) #remove a primeira ocorrência encontrada (valor 2)
if 5 in num: #varre a lista e se encontra o elemento desejado, remove.
    num.remove(5)
else:
    print('não achei o número 5')
print(num)
print(f'Essa lista em {len(num)} elementos')

print('Parte prática 2')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for v in valores:
    print(f'{v}...', end='')

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

print('Parte prática 3')

a = [2,3,4,7]
b = a #IMPORTANTE: o Python cria uma ligação entre listas, ao alterar o conteúdo de uma, a outra também sofrerá alteração
c = a[:] #cria uma cópia de todos os elementos da lista a em c
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista C: {c}')

'''Anotações

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
'''

'Parte prática'


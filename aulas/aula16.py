# lanche = () [] {} comentario: no python podemos começar uma tupla de três maneiras
# importante: tuplas são imutáveis. Uma vez iniciado o programa, não se pode alterar seu conteúdo.

lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'batata frita')
print(lanche) # mostra a tupla inteira
print(lanche[1]) # mostra suco
print(lanche[-1]) #mostra o último elemento da tupla
print(lanche[-2]) #mostra o penúltimo elemento da tupla
print(lanche[1:3]) #mostra 'suco', 'pizza'; o elemento 3 é ignorado
print(lanche[2:]) #mostra do elemento 2 até o último
print(lanche[:2]) #mostra elementos desde do ínicio, ignorando o elemento 2
print(sorted(lanche)) #mostra o conteúdo da tupla em ordem alfa

for comida in lanche: #primeira solução
    print(f'Eu vou comer {comida}')
print('Comi muito!')

for cont in range(0, len(lanche)): #segunda solução
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi muito!')

for pos, comida in enumerate(lanche): #terceira solução
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi muito!')

print('=' * 80)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b #junta o conteúdo das tupla, mostrando na ordem apresentada; primeiro conteúdo da a e em seguida o conteúdo da b
print(c) # mostra o conteúdo das duas tuplas juntas
print(c.count(5)) #mostra quantas vezes apareceu o número 5 na tupla c
print(c.index(8)) #mostra a primeira ocorrência na qual apareceu o número 8

print('=' * 80)

pessoa = ('robson', 37, 'M', 1.75)
del(pessoa) #deleta tupla, variavel, lista, etc.
print(pessoa)
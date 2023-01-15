'''Estrutura de repetição for

laço c no intervalo(1,10) <- c é uma variavel de controle e pode ter qualquer nome

laço c no intervalo(1,10)
    passo
pega

codigo em python

for c in range(1,10):
    passo
pega


for c in range(0,6):
    print(c)
print('fim')

for c in range(6,0,-1):
    print(c)
print('fim')

for c in range(0,7,2):
    print(c)
print('fim')


n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('fim')


i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')


for c in range(0,3):
    n = int(input('Digite um valor: '))
print('fim')

'''

s = 0
for c in range(0,4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores {}'.format(s))
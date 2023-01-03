def lin():
    print('-' * 222)

def mensagem(msg):
    lin()
    print(msg)
    lin()



# Programa Principal
mensagem('   Curso em Vídeo')
mensagem('   APRENDA PYTHON')
mensagem('   PYTHON É MUITO BOM!')
mensagem('Oi')

############################################################### PRÁTICA 1 #####################################################################
def pratica(txt):
    print(f'{txt}' * 222)

pratica('§')

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')



soma((37+34), 30)
lin()
soma(8,9)
lin()
soma(2,1)
############################################################### PRÁTICA 2 #####################################################################

pratica('$')
def contador1(*num):
    for valor in num:
        print(valor, end='')
    print(' FIM')
print()

contador1(2,1,7)
contador1(8,0)
contador1(4,4,7,6,2)

def contador2(*n):
    tam = len(n)
    print(f'Recebi os valores {n} e são ao todo {tam} números')
print()


contador2(2,1,7)
contador2(8,0)
contador2(4,4,7,6,2)

pratica('&')
############################################################### PRÁTICA 3 #####################################################################
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6,3,9,1,0,2]
dobra(valores)
print(valores)

pratica('%')
############################################################### PRÁTICA 4 #####################################################################
def total(* valor):
    s = 0
    for num in valor:
        s += num
    print(f'Somando os valores {valor} temos {s}')

total(5,2)
total(2,9,4)
# Curso Python

'''
* Interactive Help
* docstring
* Argumentos opcionais
* Escopo de variáveis
* Retorno de resultados
'''

#help(print)

##print(input.__doc__)

########################################## docstrings ##############################################
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :para i: início da contagem
    :para f: fim da contagem
    :para p: passo da contagem
    :return: sem retorno
    """

'''
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM!')

help(contador)'''

################################# PARAMETROS OPCIONAIS ###################################
'''
def somar(a=0,b=0,c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :para a: primeiro valor
    :para b: segundo valor
    :para c: terceiro valor    
    """
    s = a + b + c
    print(f'{s}')

somar(3,2,5)
somar(8,4)
somar()
somar(c=3, a=2)
'''

#################################### ESCOPO DE VARIÁVEIS ########################################
'''
def teste():
    print(f'Na função teste, n vale {n}')
    x = 8
    print(f'Na função teste, x vale {x}')
#Programa Principal
n = 2
print(f'No programa pincipal, n vale {n}')
teste()
'''
#print(f'No programa principal, x vale {x}')

#VARIAVEL LOCAL: SÓ FUNCIONA DENTRO DA FUNÇÃO
#VARIAVEL GLOBAL: FUNCIONA DENTRO E FORA DE UMA FUNÇÃO, ELA GERALMENTE É DECLARADA FORA DA FUNÇÃO
'''
def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')
'''
#################################### FUNÇÕES COM RETORNO ########################################
'''
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(3,2,5)
r2 = somar(2,2)
r3 = somar(6)

print(f'Os resutlados foram {r1}, {r2} e {r3}.')
'''

#################################### PRÁTICA FUNÇÕES COM RETORNO ########################################
'''
def fatorial (num = 0):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')
'''

#################################### PRÁTICA FUNÇÕES COM RETORNO LÓGICO ########################################

def par(num = 0):
    if num % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')
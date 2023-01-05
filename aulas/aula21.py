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
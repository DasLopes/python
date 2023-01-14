'''
Vamos criar um menu em Python, usando modularização.
'''

from ex115.lib.interface import *
from ex115.lib.arquivo import *

arq = 'cadastro.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo.
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de sair do sistema.
        cabeçalho('Saindo do Sistema... Até logo!')
        break
    else:
        # Digitou uma opção errada no sistema.
        print('\033[31mERRO! Digite uma opção válida.\033[m')

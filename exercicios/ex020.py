# o mesmo professor do desafio anterior
# quer sortear a ordem de apresentação de
# trabalhos dos alunos.
# faça um programa que leia o nome dos alunos
# e mostre a ordem sorteada.

from random import shuffle

a1 = input('Nome do aluno: ')
a2 = input('Nome do aluno: ')
a3 = input('Nome do aluno: ')

alunos = [a1, a2, a3]
shuffle(alunos)
print('A ordem de apresentação será: ')
print(alunos)

'''
Faça um programa que mostre na tela uma contahem regressiva para o estouro de fogos de artificio, indo de 10 até 0, com com uma pausa de 1 segundo entre eles.
'''

from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)

'''
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
'''
from time import sleep
for c in range(1,50):
    if c % 2 == 0:
        sleep(0.2)
        print(c)
